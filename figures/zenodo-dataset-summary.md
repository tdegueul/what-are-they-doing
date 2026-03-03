# Dataset Summary

## Overview
| Metric | Value |
| --- | --- |
| Tracked developers in registry | 7 |
| Developers with local monthly snapshots | 5 |
| Unsampled tracked developers | mavam, teamchong |
| Observation window | 2025-09-01 to 2026-02-28 |
| Distinct months with snapshots | 6 |
| Developer-month snapshots | 30 |
| Tracked repositories in registry | 260 |
| Tracked repositories with local snapshots | 229 |
| Total commits from daily totals | 72,888 |
| Embedded commit records | 68,407 |
| Commit-record coverage | 93.9% |
| Active developer-days | 559 |
| Peak aggregate day | 2026-02-22 (1,739 commits) |
| Commit records with >=1 agent signal | 35,548 / 68,407 (52.0%) |
| Commit records with >1 agent signal | 134 |
| Distinct detected agent labels | 8 |
| Most frequent detected agent | claude_code (35,477 hits) |
| Cached commit-detail files | 1,759 |

## Developer Coverage
| Developer | Status | Month span | Tracked repos | Commits | Commit records | Active days | Peak day | Agent commits | Agent % | Top agent |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dicklesworthstone | sampled | 2025-09..2026-02 | 100 | 42,549 | 38,424 | 127 | 1,115 | 29,610 | 77.1% | claude_code |
| mavam | registry-only | - | 21 | - | - | - | - | - | - | - |
| obra | sampled | 2025-09..2026-02 | 36 | 2,656 | 2,656 | 116 | 202 | 1,388 | 52.3% | claude_code |
| philipp-spiess | sampled | 2025-09..2026-02 | 15 | 801 | 801 | 69 | 43 | 2 | 0.2% | opencode |
| ruvnet | sampled | 2025-09..2026-02 | 9 | 5,660 | 5,304 | 117 | 350 | 4,483 | 84.5% | claude_code |
| steipete | sampled | 2025-09..2026-02 | 71 | 21,222 | 21,222 | 130 | 630 | 65 | 0.3% | codex |
| teamchong | registry-only | - | 10 | - | - | - | - | - | - | - |

## Agent Signals
| Agent | Hits | Share of commit records | Developers with signal |
| --- | --- | --- | --- |
| claude_code | 35,477 | 51.9% | 5 |
| codex | 142 | 0.2% | 4 |
| cursor | 44 | 0.1% | 3 |
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
