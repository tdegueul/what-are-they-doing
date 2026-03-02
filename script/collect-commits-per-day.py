#!/usr/bin/env python3
"""Collect commits per day for a developer in a given month.

Repos are discovered via the GitHub contributionsCollection GraphQL API
(same source as list_repos_by_user_with_events.py), so private repos are
included when the token has access.

Usage:
    python script/collect-commits-per-day.py --developer steipete --month 2025-12

Output:
    data/{developer}-{YYYY-MM}.json  — one file for the whole month

Token is retrieved from the system keyring:
  service  = "login2"
  username = "github_token"
"""

import argparse
import json
import sys
import time
from calendar import monthrange
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import keyring
import requests

REPO_ROOT = Path(__file__).parent.parent
DATA_DIR = REPO_ROOT / "data"

PER_PAGE = 100

GRAPHQL_QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      commitContributionsByRepository(maxRepositories: 100) {
        repository {
          nameWithOwner
        }
        contributions {
          totalCount
        }
      }
    }
  }
}
"""


def build_session(token: str) -> requests.Session:
    s = requests.Session()
    s.headers.update(
        {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )
    return s


def get_with_retry(session: requests.Session, url: str, params: dict) -> dict:
    """GET with automatic rate-limit back-off."""
    while True:
        resp = session.get(url, params=params)

        if resp.status_code in (403, 429):
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(reset - time.time(), 0) + 2
            print(f"    Rate limited. Waiting {wait:.0f}s …", file=sys.stderr)
            time.sleep(wait)
            continue

        resp.raise_for_status()
        return resp.json()


def fetch_repos_for_month(
    session: requests.Session, handle: str, year: int, month: int, num_days: int
) -> list[str]:
    """Return list of repo nameWithOwner strings the user contributed to in the given month."""
    from_dt = datetime(year, month, 1, tzinfo=timezone.utc)
    to_dt = datetime(year, month, num_days, 23, 59, 59, tzinfo=timezone.utc)

    resp = session.post(
        "https://api.github.com/graphql",
        json={
            "query": GRAPHQL_QUERY,
            "variables": {
                "login": handle,
                "from": from_dt.isoformat(),
                "to": to_dt.isoformat(),
            },
        },
    )
    resp.raise_for_status()
    data = resp.json()

    if "errors" in data:
        raise RuntimeError(f"GraphQL errors: {data['errors']}")

    contributions = (
        data["data"]["user"]["contributionsCollection"]["commitContributionsByRepository"]
    )
    return [entry["repository"]["nameWithOwner"] for entry in contributions]


def fetch_commits_for_repo_day(
    session: requests.Session, repo: str, handle: str, day: date
) -> list[dict]:
    """Fetch all commits by handle in repo on a single day."""
    since = f"{day.isoformat()}T00:00:00Z"
    until = f"{(day + timedelta(days=1)).isoformat()}T00:00:00Z"
    url = f"https://api.github.com/repos/{repo}/commits"

    commits = []
    page = 1
    while True:
        items = get_with_retry(
            session,
            url,
            {"author": handle, "since": since, "until": until, "per_page": PER_PAGE, "page": page},
        )
        if not items:
            break
        commits.extend(items)
        if len(items) < PER_PAGE:
            break
        page += 1
    return commits


def parse_month(value: str) -> tuple[int, int]:
    try:
        year_str, month_str = value.split("-")
        year, month = int(year_str), int(month_str)
        if not (1 <= month <= 12):
            raise ValueError
        return year, month
    except (ValueError, AttributeError):
        raise argparse.ArgumentTypeError(
            f"Invalid month '{value}'. Expected YYYY-MM, e.g. 2025-12"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Collect commits per day for a GitHub developer."
    )
    parser.add_argument("--developer", required=True, help="GitHub handle")
    parser.add_argument(
        "--month",
        required=True,
        type=parse_month,
        metavar="YYYY-MM",
        help="Month to collect, e.g. 2025-12",
    )
    args = parser.parse_args()

    handle: str = args.developer
    year, month = args.month
    month_str = f"{year}-{month:02d}"
    num_days = monthrange(year, month)[1]

    token = keyring.get_password("login2", "github_token")
    if not token:
        sys.exit(
            "No GitHub token found in keyring "
            "(service='login2', username='github_token')"
        )

    session = build_session(token)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_file = DATA_DIR / f"{handle}-{month_str}.json"

    print(f"Collecting commits for @{handle}  {month_str}  ({num_days} days)")

    # Step 1: discover repos from contributions API
    print("Fetching repo list from contributionsCollection …")
    repos = fetch_repos_for_month(session, handle, year, month, num_days)
    print(f"  {len(repos)} repo(s): {', '.join(repos)}")

    result = {
        "developer": handle,
        "month": month_str,
        "repos": repos,
        "days": {},
    }
    total_saved = 0

    # Step 2: for each day, collect commits across all repos
    for day_num in range(1, num_days + 1):
        day = date(year, month, day_num)
        day_str = day.isoformat()

        all_commits = []
        for repo in repos:
            commits = fetch_commits_for_repo_day(session, repo, handle, day)
            all_commits.extend(commits)
            if commits:
                time.sleep(0.5)

        total_saved += len(all_commits)
        result["days"][day_str] = {
            "total_count": len(all_commits),
            "sampled": len(all_commits),
            "commits": all_commits,
        }
        print(f"  {day_str}  {len(all_commits):>3} commits")
        time.sleep(1)

    out_file.write_text(json.dumps(result, indent=2) + "\n")
    print(f"\nDone. {total_saved} commits saved to {out_file.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
