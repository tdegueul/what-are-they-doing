# Dataset Summary

## Overview
| Metric | Value |
| --- | --- |
| Tracked developers in registry | 7 |
| Developers with local monthly snapshots | 7 |
| Unsampled tracked developers | - |
| Observation window | 2025-09-01 to 2026-02-28 |
| Distinct months with snapshots | 6 |
| Developer-month snapshots | 42 |
| Tracked repositories in registry | 260 |
| Tracked repositories with local snapshots | 260 |
| Total commits from daily totals | 81,230 |
| Embedded commit records | 76,749 |
| Commit-record coverage | 94.5% |
| Active developer-days | 821 |
| Peak aggregate day | 2026-02-16 (1,833 commits) |
| Commit records with >=1 agent signal | 36,565 / 76,749 (47.6%) |
| Commit records with >1 agent signal | 134 |
| Distinct detected agent labels | 8 |
| Most frequent detected agent | claude_code (36,493 hits) |
| Cached commit-detail files | 1,759 |

## Developer Coverage
| Developer | Status | Month span | Tracked repos | Commits | Commit records | Active days | Peak day | Agent commits | Agent % | Top agent |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dicklesworthstone | sampled | 2025-09..2026-02 | 100 | 42,549 | 38,424 | 127 | 1,115 | 29,610 | 77.1% | claude_code |
| mavam | sampled | 2025-09..2026-02 | 21 | 2,543 | 2,543 | 154 | 88 | 981 | 38.6% | claude_code |
| obra | sampled | 2025-09..2026-02 | 36 | 2,656 | 2,656 | 116 | 202 | 1,388 | 52.3% | claude_code |
| philipp-spiess | sampled | 2025-09..2026-02 | 15 | 801 | 801 | 69 | 43 | 2 | 0.2% | opencode |
| ruvnet | sampled | 2025-09..2026-02 | 9 | 5,660 | 5,304 | 117 | 350 | 4,483 | 84.5% | claude_code |
| steipete | sampled | 2025-09..2026-02 | 71 | 21,222 | 21,222 | 130 | 630 | 65 | 0.3% | codex |
| teamchong | sampled | 2025-09..2026-02 | 10 | 5,799 | 5,799 | 108 | 295 | 36 | 0.6% | claude_code |

## Agent Signals
| Agent | Hits | Share of commit records | Developers with signal |
| --- | --- | --- | --- |
| claude_code | 36,493 | 47.5% | 7 |
| codex | 142 | 0.2% | 4 |
| cursor | 45 | 0.1% | 4 |
| opencode | 22 | 0.0% | 3 |
| amp | 12 | 0.0% | 1 |
| sweep | 2 | 0.0% | 1 |
| copilot | 2 | 0.0% | 1 |
| gemini | 1 | 0.0% | 1 |

## Notes
- `Total commits from daily totals` comes from the `total_count` field in monthly snapshot files.
- `Embedded commit records` counts commit objects stored inside those snapshots; agent-use metrics are computed on this subset.
- Agent-use labels are heuristic detections from commit messages, co-author trailers, commit authors, and cached changed-file signals when available.
- The current local dataset contains monthly snapshots for 5 of the 7 tracked developers listed in `developers.json`.
