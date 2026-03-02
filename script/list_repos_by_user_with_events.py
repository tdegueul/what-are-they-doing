"""
Fetch all repos where @steipete committed in the last 3 months
using GitHub GraphQL contributionsCollection API.
"""

import os
import json
import requests
from datetime import datetime, timezone, timedelta
import keyring


GITHUB_TOKEN = keyring.get_password("login2", "github_token")
USERNAME = "steipete"

if not GITHUB_TOKEN:
    raise EnvironmentError("Set GITHUB_TOKEN environment variable")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json",
}

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      commitContributionsByRepository(maxRepositories: 100) {
        repository {
          nameWithOwner
          url
          isPrivate
        }
        contributions {
          totalCount
        }
      }
    }
  }
}
"""

def fetch_repos(username: str, from_dt: datetime, to_dt: datetime) -> list[dict]:
    variables = {
        "login": username,
        "from": from_dt.isoformat(),
        "to": to_dt.isoformat(),
    }
    response = requests.post(
        "https://api.github.com/graphql",
        headers=HEADERS,
        json={"query": QUERY, "variables": variables},
    )
    response.raise_for_status()
    data = response.json()

    if "errors" in data:
        raise RuntimeError(f"GraphQL errors: {data['errors']}")

    contributions = (
        data["data"]["user"]["contributionsCollection"]["commitContributionsByRepository"]
    )
    return contributions


def collect_all_repos(username: str) -> dict:
    to_dt = datetime.now(timezone.utc)
    from_dt = to_dt - timedelta(days=90)


    """Fetch all repos and return as a dict keyed by repo name."""
    repos = fetch_repos(username, from_dt, to_dt)
    repos.sort(key=lambda r: r["contributions"]["totalCount"], reverse=True)
    
    repos_dict = {}
    for entry in repos:
        name = entry["repository"]["nameWithOwner"]
        repos_dict[name] = {
            "url": entry["repository"]["url"],
            "commits": entry["contributions"]["totalCount"],
            "is_private": entry["repository"]["isPrivate"],
        }
    
    return repos_dict


def main():


    repos_dict = collect_all_repos(USERNAME)
    print(repos_dict)
    return

    if not repos_dict:
        print("No contributions found.")
        return

    print(f"Found {len(repos_dict)} repo(s):\n")
    print(f"{'Commits':<10} {'Repo'}")
    print("-" * 60)
    for name, info in repos_dict.items():
        count = info["commits"]
        private = " [private]" if info["is_private"] else ""
        print(f"{count:<10} {name}{private}")

    print(f"\nTotal repos: {len(repos_dict)}")


if __name__ == "__main__":
    main()