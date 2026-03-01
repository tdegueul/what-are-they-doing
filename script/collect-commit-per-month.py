#!/usr/bin/env python3
"""Collect GitHub commit counts per month for developers listed in developers.json.

Token is retrieved from the system keyring:
  service  = "login2"
  username = "github_token"

Date range: January 2025 through the current month.
Results are written back to developers.json.
"""

import json
import re
import sys
import time
from calendar import monthrange
from datetime import date
from pathlib import Path

import keyring
import requests

REPO_ROOT = Path(__file__).parent.parent
DEVELOPERS_FILE = REPO_ROOT / "developers.json"

START = (2025, 1)

MONTH_ABBR = ["jan", "feb", "mar", "apr", "may", "jun",
               "jul", "aug", "sep", "oct", "nov", "dec"]


def month_key(year: int, month: int) -> str:
    return f"{MONTH_ABBR[month - 1]}-{year}"


def iter_months(end: tuple[int, int]) -> list[tuple[int, int]]:
    """Yield (year, month) tuples from START through end, inclusive."""
    year, month = START
    end_year, end_month = end
    while (year, month) <= (end_year, end_month):
        yield year, month
        month += 1
        if month > 12:
            month = 1
            year += 1


def load_developers() -> list[dict]:
    text = DEVELOPERS_FILE.read_text()
    # Repair missing commas between adjacent JSON objects (} ... {)
    text = re.sub(r"\}\s*\{", "},{", text)
    return json.loads(text)


def count_commits(
    handle: str,
    year: int,
    month: int,
    session: requests.Session,
) -> int:
    last_day = monthrange(year, month)[1]
    since = f"{year}-{month:02d}-01"
    until = f"{year}-{month:02d}-{last_day}"
    query = f"author:{handle} committer-date:{since}..{until}"

    while True:
        resp = session.get(
            "https://api.github.com/search/commits",
            params={"q": query, "per_page": 1},
        )

        if resp.status_code == 200:
            return resp.json().get("total_count", 0)

        if resp.status_code == 422:
            # Validation error — treat as zero results
            return 0

        if resp.status_code in (403, 429):
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(reset - time.time(), 0) + 2
            print(f"    Rate limited. Waiting {wait:.0f}s …")
            time.sleep(wait)
            continue  # retry

        print(
            f"    Warning: HTTP {resp.status_code} for {handle} "
            f"{month_key(year, month)}: {resp.text[:200]}"
        )
        return -1


def main() -> None:
    token = keyring.get_password("login2", "github_token")
    if not token:
        sys.exit(
            "No GitHub token found in keyring "
            "(service='login2', username='github_token')"
        )

    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {token}",
            # Required for the commit search API
            "Accept": "application/vnd.github.cloak-preview+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )

    today = date.today()
    end = (today.year, today.month)
    months = list(iter_months(end))

    developers = load_developers()

    for dev in developers:
        handle = dev["handle"]
        print(f"\n{handle}")
        dev.setdefault("commits_per_month", {})

        for year, month in months:
            key = month_key(year, month)
            count = count_commits(handle, year, month, session)
            dev["commits_per_month"][key] = count
            print(f"  {key}: {count}")
            time.sleep(2)  # stay well within rate limits

    DEVELOPERS_FILE.write_text(json.dumps(developers, indent=2) + "\n")
    print("\nDone. developers.json updated.")


if __name__ == "__main__":
    main()
