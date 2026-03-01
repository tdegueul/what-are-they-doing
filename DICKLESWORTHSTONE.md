# Dicklesworthstone

  - Tagline: "Building the tooling that lets dozens of AI agents ship complex projects in days."
  - Essentially a collection of 14 tools for agentic development
  - Interdependent repos

# Repositories
  - Many `.md` files tracking plans, current progress, etc.
  - Wtf is this sh*t? https://github.com/Dicklesworthstone/pi_agent_rust/blob/main/.github/workflows/ci.yml

```
Developer: @Dicklesworthstone
  Warning: commit search failed (HTTP 422).
  6 owned non-fork repo(s) found
  jan-2025: 0
  feb-2025: 0
  mar-2025: 0
  apr-2025: 0
  may-2025: 0
  jun-2025: 0
  jul-2025: 0
  aug-2025: 0
  sep-2025: 0
  oct-2025: 0
  nov-2025: 92  (Dicklesworthstone/markdown_web_browser:92)
  dec-2025: 990  (Dicklesworthstone/ntm:637, Dicklesworthstone/chat_shared_conversation_to_file:63, Dicklesworthstone/source_to_prompt_tui:18, Dicklesworthstone/markdown_web_browser:1, Dicklesworthstone/slb:271)
  jan-2026: 1091  (Dicklesworthstone/ntm:1002, Dicklesworthstone/chat_shared_conversation_to_file:11, Dicklesworthstone/source_to_prompt_tui:14, Dicklesworthstone/markdown_web_browser:22, Dicklesworthstone/slb:42)
  feb-2026: 655  (Dicklesworthstone/ntm:618, Dicklesworthstone/chat_shared_conversation_to_file:3, Dicklesworthstone/source_to_prompt_tui:8, Dicklesworthstone/markdown_web_browser:17, Dicklesworthstone/slb:9)
  mar-2026: 0


```

# Commits
  - Mostly co-authored by Claude code
  - Mostly using conventional commits

# Issues and PRs
  - No issues or PRs whatsoever

# Example software
  - https://frankentui.com/web
  - 

## commits

 python script/detect-agents.py data/Dicklesworthstone-2025-12.json 
Commits: 2337  |  with file cache: 0  |  agents loaded: 44

Agent Detection — Dicklesworthstone-2025-12
=======================================================
  Commits with ≥1 agent signal : 1472 / 2337  (63%)
  Commits with >1 agent signal : 9

Agents detected  (n=2337 commits)
─────────────────────────────────
  claude_code               ████████████████████████████████████ 63%       1472
  codex                      0%                                               9
  cursor                     0%                                               1

Example commits per agent
─────────────────────────

  claude_code  (1472 commits)
    87ad12b  chore(deps): Update Cargo.lock
    f73e342  style(amp): Minor formatting cleanup
    82b1120  test(e2e): Improve E2E, search caching, and CLI index tests

  codex  (9 commits)
    cb57dcd  feat: add robot mode for AI agent integration
    a7c8cd7  feat(testing): add test harness with structured logging (ntm-66c)
    15d20b7  feat(dashboard): add ticker panel and refactor panel system

  cursor  (1 commits)
    cb57dcd  feat: add robot mode for AI agent integration

## Context switching

```
2025-12-01    19c   2r    2s  |...................                                     |
2025-12-02     2c   2r    1s  |..                                                      |
2025-12-03     2c   1r    0s  |..                                                      |
2025-12-04     1c   1r    0s  |.                                                       |
2025-12-06    71c   3r    3s  |.........................................BB...BBBBBBBBBB|
2025-12-07   100c   3r   19s  |BBBBBBBBBBBBBBBBGGGCCBBBBBBBBBBBBCBBBCCCCCCCCCCCCCCCCCCC|
2025-12-08   100c   3r   21s  |CGGGGCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC|
2025-12-09    83c   4r   29s  |.BBBBB..B....B.BB.BBBB.B..B.BBBBBBB...BB...BBBBBBBBBBBBB|
2025-12-10   100c   1r    0s  |DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD|
2025-12-11   100c   2r   20s  |DDDDDDDDBDDDBBDBBBBBBDDDDDBDDDDDDBBBDBDDDDDDDDDDDDDDDDDB|
2025-12-12    41c   2r   11s  |DDBDBBDBBBBBDDDDDDDBBBBBBDDBDDBBBBBBBBBBB               |
2025-12-13   100c   4r   29s  |DBDDBBBBBBBBBBBDBBDBBBBBDBDBBBDBBBBBD.BDDDDDBBDDBBBBB...|
2025-12-14   100c   5r   49s  |BBBBGCCCBGC..GEEEEEEBEEEEEBEEBCBGCCCBGEGGEBEEEEEEBBBBBBB|
2025-12-15   100c   9r   49s  |..BBBBCCCBCBC.BCBGCCCCCCCCCGGCBBBBBBDDDGDDB.CBCGCBBGBBCC|
2025-12-16   100c   3r   40s  |CGGGGCCCCCGGGGGCCCCGGGGGGGGGGGGGGGGGGGGGGGEEEEEEEEEEEEEE|
2025-12-17   100c   2r    5s  |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE.EEEEEEEEEE....|
2025-12-18   100c   3r   13s  |HHHH..H..HH.HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH.HH..H..|
2025-12-19   100c  12r   49s  |....E.....E.......B..BHGCCCHCGHHHHHHH.HHHH.HHHHHHH.GHHHH|
2025-12-20   100c   1r    0s  |AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA|
2025-12-21   100c   1r    0s  |AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA|
2025-12-22   100c   1r    0s  |AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA|
2025-12-23   100c   4r    7s  |AAAAAAAAAAAAAAAAAAA.AAAAAAAAAAAAAAAAAAAAAAAAAADDDDBBBBBA|
2025-12-24    32c   3r    5s  |BAAAAAAAAAAAAAAAAAAAAAA...ABAAAA                        |
2025-12-25   100c   4r   21s  |BBBBBB.AA.A.AABBAAAAAAAAAAAA...AAAAAAAAAAAAAAA.AAAAAABA.|
2025-12-26    74c   9r   28s  |AAAA.EAAAA.EBAAAAAAEAABAAAAAAAAAAAAAAAA..AAADADCG.DDCDDD|
2025-12-27    12c   2r    1s  |............                                            |
2025-12-28   100c   4r   45s  |CGGGGCCCCCCCCCCCCCCCCCCCCCCCCGGGCGCGCCCCCGGCCCCG.AAAAAAA|
2025-12-29   100c   4r   19s  |AAAAAAAAAAAA.A.AAAAAAAAAAAAAAAAAAA.A...FAFFAAFAAFAAAAAFA|
2025-12-30   100c   1r    0s  |FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF|
2025-12-31   100c   4r   30s  |AAAFAFAFFAAFBAAAABAAGBABBBBBBBBBABBBBAAAFFBFFFBFFAAFFFFF|
```
