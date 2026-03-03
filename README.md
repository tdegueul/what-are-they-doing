# What are they doing? A Commit-Level Dataset of Hyperactive AI-augmented Developers on GitHub 

This dataset captures the commit activity of a curated set of highly active, agentic software developers on GitHub. For each developer, it provides full commit metadata and daily commit counts spanning the months around the agentic coding explosion.

The goal of this dataset is to enable studies of AI-augmented software engineering behavior, agent adoption patterns, repository switching, commit quality, and temporal activity rhythms. The dataset currently covers 7 developers.


> **If you use this dataset, please cite it as below.**

```bibtex
@dataset{whataretheydoing2026,
  author    = {Thomas Degueule and Bernd Freisleben and Shane McIntosh and Martin Monperrus and Aaron Randrianaina and Romain Robbes},
  title     = {What are they doing? A Commit-Level Dataset of Hyperactive AI-augmented Developers on GitHub},
  howpublished     = {Dataset on Zenodo},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {https://doi.org/10.5281/zenodo.18850301},
  url       = {https://github.com/tdegueul/what-are-they-doing}
}
```

This dataset has been produced at the Bellairs'26 Workshop on Continuous Software Engineering.

---

## Data Collection Methodology

Candidate developers are identified with the following sources:
- AI coding conversation on X/Twitter
- Github queries (see `script/find_agentic_ai_coders.py`)
- [Gitista](https://gitista.com/)
- [committers.top](https://committers.top/)

Selection is then performed as a qualitative curation process by a team of expert software engineering researchers. We do not rely on a single automatic rule. Instead, we combine automated evidence with manual assessment of each candidate developer and their repositories.

Our inclusion workflow has four steps:

1. **Initial screening.** We use public activity signals and commit-volume queries to identify unusually active developers who may be using AI coding tools.
2. **Heuristic agent detection.** We inspect the developer's commits with the heuristics from [`agent-mining`](https://github.com/labri-progress/agent-mining), including co-author trailers, agent-related commit message patterns, and agent-specific files or configuration traces.
3. **Manual repository and commit review.** We read repository contents, inspect commit histories, and examine commit messages, temporal activity patterns, and bursts of work across repositories.
4. **Expert judgment.** When explicit agent traces are absent or incomplete, we rely on researcher judgment to decide whether a developer should still be considered AI-augmented. In those cases, the decision is based on the overall pattern of evidence, including message style, cadence, sustained commit frequency, and repository-level context.

In other words, the dataset is intentionally **curated rather than mechanically filtered**. Explicit agent signals strengthen the evidence, but they are not required in every included case. Some developers leave strong machine-readable traces; others are included because expert review indicates that their working style is consistent with AI-augmented software engineering.

## Covered Developers

| Handle | Analysis | One liner presentation |
|---|---|---|
| [steipete](https://github.com/steipete)  | [./steipete.md](steipete.md) | TODO |
| [Dicklesworthstone](https://github.com/Dicklesworthstone) | [Dicklesworthstone.md](DICKLESWORTHSTONE.md)  | A developer with ~20(!) Claude Code Max subscriptions |
| [ruvnet](https://github.com/ruvnet)  | [ruvnet.md](ruvnet.md) | An independent consultant and developer harnessing the power of AI to build high-impact software (top of GitHub's trending repositories for at least 2 days) |
| [obra](https://github.com/obra)   |[obra.md](obra.md) | A developer who just started his own company and using AI to to build software |
| [philipp-spiess](https://github.com/philipp-spiess)  | [philipp-spiess.md](philipp-spiess.md) | An open-source contributor, proud vibe-coder and AI agent enthusiast |
| [mavam](https://github.com/mavam) | [mavam.md](mavam.md) | TODO |
| [teamchong](https://github.com/teamchong) | [teamchong.md](teamchong.md) | A developer with a super-human burst of commit productivity followed by a fall from grace |

Additional developpers:
| Handle | Analysis | One liner presentation |
|---|---|---|
| [Steve Yegge](https://github.com/steveyegge)| -- | Vibe-coded popular projects beads (issue tracking) and Gas Town (agent orchestration) |

### False Positives

Notes about inspected developers who appeared to be agent-supported but did not meet our qualitative inspection criteria appear in markdown files in the [false positive](false-positive) directory.

## Dataset statistics

TODO

---


## Dataset Contents

```
developers.json                    # Developer registry with metadata and repo data/
  {developer}-{YYYY}-{MM}.json     # Daily commit data per developer per month
  commits/{sha}.json               # Cached per-commit file-level details
```

### Developer Registry (`developers.json`)

Each entry contains:
- `handle` — GitHub username
- `repos` — list of repositories committed to in the last 90 days

### Monthly Commit Files (`data/{developer}-{YYYY}-{MM}.json`)

Each file contains:
- `developer` — GitHub handle
- `month` — `YYYY-MM`
- `days` — dict keyed by date (`YYYY-MM-DD`), each value containing:
  - `total_count` — number of commits that day
  - `sampled` — number of commits with full metadata fetched
  - `commits` — list of raw GitHub API commit objects

---

## Scripts

All scripts live in `script/` and read a GitHub token from the system keyring
(`service="login2"`, `username="github_token"`).

The [`agent-mining`](https://github.com/labri-progress/agent-mining) repository is included as a submodule and provides the agent-detection heuristics used by `detect-agents.py`.

A GitHub personal access token with `repo` and `read:user` scopes is required, stored in the system keyring:

```python
import keyring
keyring.set_password("login2", "github_token", "<your-token>")
```

### Data Collection

| Script | Description |
|---|---|
| `collect-commits-per-day.py` | Collects all commits for a developer in a given month via the GitHub GraphQL API. Writes `data/{developer}-{YYYY-MM}.json`. Usage: `python script/collect-commits-per-day.py --developer steipete --month 2025-12` |
| `collect-commit-per-month.py` | Collects monthly commit counts for every developer in `developers.json` by iterating over their non-fork repos (avoids fork inflation). Writes results back to `developers.json`. |
| `list_repos_by_user_with_events.py` | Fetches all repos where a developer committed in the last 3 months via the GitHub GraphQL  API. |
| `collect-tentative-names.py` | Searches GitHub commits for `noreply@anthropic.com` to discover candidate AI-heavy users; filters by commit count and repo count. |

### Analysis

| Script | Description |
|---|---|
| `analyze-commits.py` | Analyses commit messages using Conventional Commits conventions (type breakdown, scopes, breaking changes). Usage: `python script/analyze-commits.py data/steipete-2025-12.json` |
| `analyze-commit-quality.py` | Scores commits as "good" or "dirty" by fetching changed files from the GitHub API and applying heuristics (focused vs scattered, test coupling, diff size, etc.). Commit details are cached in `data/commits/{sha}.json`. Usage: `python script/analyze-commit-quality.py data/steipete-2025-12.json` |
| `analyze-repo-switching.py` | Analyses how a developer switches between repositories over time (concentration, consecutive switches, bouncebacks, day-by-day timeline). Usage: `python script/analyze-repo-switching.py developers.json --author steipete --month 2025-12` |
| `visualize-file-touches.py` | Fetches per-commit file details and prints a terminal report covering file categories, change sizes, language hotspots, test/docs coupling, and engineering-signal heuristics. Usage: `python script/visualize-file-touches.py developers.json --author steipete --month 2025-12` |
| `detect-agents.py` | Detects which coding agents (Claude Code, Cursor, etc.) are used in a developer's commits via agent-mining heuristics (co-author trailers, message patterns, config files). Usage: `python script/detect-agents.py data/steipete-2025-12.json` |
| `histogram-commit-time.py` | Prints a horizontal bar chart of commit counts by UTC hour from a monthly data file. Usage: `python script/histogram-commit-time.py data/steipete-2025-12.json` |
| `plot-commits-over-time-separate.py` | Same chart with one subplot per developer. Saves to `data/commits-over-time-separate.png`. |

### Typical Workflow

```bash
# 1. Collect monthly commit data
python script/collect-commits-per-day.py --developer steipete --month 2025-12

# 2. Analyse the collected data
python script/analyze-commits.py        data/steipete-2025-12.json
python script/analyze-commit-quality.py data/steipete-2025-12.json
python script/detect-agents.py          data/steipete-2025-12.json
python script/histogram-commit-time.py  data/steipete-2025-12.json
python script/analyze-repo-switching.py developers.json --author steipete --month 2025-12
python script/visualize-file-touches.py developers.json --author steipete --month 2025-12

# 3. Visualise trends
python script/plot-commits-over-time-separate.py
```

---


## Related Work

- Robbes et al. (2026). *Agentic Much? Adoption of Coding Agents on GitHub.* arXiv:2601.18341. First large-scale study (129,134 projects) of coding agent adoption on GitHub, finding an adoption rate of 15.85%–22.60% and that agent-assisted commits are larger and more feature/bugfix-oriented than human-only commits.
  - Paper: https://arxiv.org/pdf/2601.18341
  - Code/artifacts: https://github.com/labri-progress/agent-mining

- Yu et al. (2024). *Where Is Self-admitted Code Generated by Large Language Models on GitHub?* APSEC 2024, pp. 407–418. Studies self-admitted LLM-generated code in GitHub projects with >5 stars: 229 projects and 696 snippets across five languages.

- Alam et al. (2026). *Why Are AI Agent Involved Pull Requests (Fix-Related) Remain Unmerged? An Empirical Study.* Analyzes 8,106 fix-related PRs from five AI coding agents (AIDEV-POP dataset).

- Xu et al. (2025). *code_transformed: The Influence of Large Language Models on Code.* arXiv:2506.12014. Large-scale study of 20,000+ GitHub repos showing measurable shifts in coding style attributable to LLM influence.

---

## License

MIT

---

## Contact

Open an issue on the repository https://github.com/tdegueul/what-are-they-doing
