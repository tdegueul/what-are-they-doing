#!/usr/bin/env python3
"""Collect up to 100 commits per day for a developer in a given month.

Usage:
    python script/collect-commits-per-day.py --developer steipete --month 2025-12

Output:
    data/{developer}/{YYYY-MM}/{YYYY-MM-DD}.json  — one file per day

When a day has more than 100 commits the script picks a random page so the
sample is not always the same 100.

Token is retrieved from the system keyring:
  service  = "login2"
  username = "github_token"
"""

import argparse
import json
import random
import sys
import time
from calendar import monthrange
from datetime import date
from pathlib import Path

import keyring
import requests

REPO_ROOT = Path(__file__).parent.parent
DATA_DIR = REPO_ROOT / "data"

# GitHub search API hard cap: 10 pages × 100 = 1 000 results
MAX_SEARCH_RESULTS = 1000
PER_PAGE = 100


def build_session(token: str) -> requests.Session:
    s = requests.Session()
    s.headers.update(
        {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.cloak-preview+json",
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


def fetch_day(
    handle: str, day: date, session: requests.Session
) -> tuple[list[dict], int]:
    """Return (commits, total_count) for a single day.

    If total_count > PER_PAGE a random page within the reachable range is used
    so repeated runs yield different samples.
    """
    date_str = day.isoformat()
    query = f"author:{handle} committer-date:{date_str}..{date_str}"
    url = "https://api.github.com/search/commits"

    # First request: discover total_count, collect page 1
    data = get_with_retry(
        session, url, {"q": query, "per_page": PER_PAGE, "page": 1}
    )
    total = data.get("total_count", 0)
    items = data.get("items", [])

    if total > PER_PAGE:
        max_page = min(total, MAX_SEARCH_RESULTS) // PER_PAGE
        page = random.randint(1, max_page)
        if page > 1:
            data = get_with_retry(
                session, url, {"q": query, "per_page": PER_PAGE, "page": page}
            )
            items = data.get("items", [])

    return items, total


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
        description="Collect up to 100 commits per day for a GitHub developer."
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

    out_dir = DATA_DIR / handle / month_str
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Collecting commits for @{handle}  {month_str}  ({num_days} days)")

    total_saved = 0
    for day_num in range(1, num_days + 1):
        day = date(year, month, day_num)
        day_str = day.isoformat()
        out_file = out_dir / f"{day_str}.json"

        commits, total_count = fetch_day(handle, day, session)

        payload = {
            "developer": handle,
            "date": day_str,
            "total_count": total_count,
            "sampled": len(commits),
            "commits": commits,
        }
        out_file.write_text(json.dumps(payload, indent=2) + "\n")
        total_saved += len(commits)

        indicator = f"(of {total_count})" if total_count > len(commits) else ""
        print(
            f"  {day_str}  {len(commits):>3} commits {indicator}"
            f"  → {out_file.relative_to(REPO_ROOT)}"
        )

        time.sleep(2)

    print(f"\nDone. {total_saved} commits saved to {out_dir.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()
