# Analysis of @steipete

This developer is the main contributor of clawbot/openclaw.

## Commits per month

```
steipete
  jan-2025: 0
  feb-2025: 0
  mar-2025: 0
  apr-2025: 464
  may-2025: 3214
  jun-2025: 8646
  jul-2025: 2885
  aug-2025: 2008
  sep-2025: 276
  oct-2025: 82
  nov-2025: 232423
  dec-2025: 1631069
  jan-2026: 3246519
  feb-2026: 630778
  mar-2026: 0
```

Top-10 repositories for @steipete — December 2025
Rank  Commits  Repository
-------------------------------------------------------
1        1000  jiangshaojie2020/clawdbot

### python script/collect-commits-per-day.py

Dec 2025

```
  2025-12-01    5 commits 
  2025-12-02 (of 24006)
  2025-12-03 (of 47757)
  2025-12-04 (of 5660)
  2025-12-05 (of 37657)
  2025-12-06 (of 66481)
  2025-12-07 (of 135232)
  2025-12-08 (of 99405)
  2025-12-09 (of 134434)
  2025-12-10 (of 46551)
  2025-12-11 (of 3054)
  2025-12-12 (of 69173)
  2025-12-13 (of 130327)
  2025-12-14 (of 124146)
  2025-12-15    3 commits 
  2025-12-16 (of 7561)
  2025-12-17 (of 75011)
  2025-12-18 (of 74161)
  2025-12-19 (of 44845)
  2025-12-20 (of 153525)
  2025-12-21 (of 57617)
  2025-12-22 (of 24701)
  2025-12-23 (of 37784)
  2025-12-24 (of 52114)
  2025-12-25 (of 19233)
  2025-12-26 (of 57584)
  2025-12-27 (of 22256)
  2025-12-28 (of 7658)
  2025-12-29 (of 22601)
  2025-12-30 (of 40117)
  2025-12-31 (of 8375)
```

## Does he ever sleep?

```
$ python script/histogram-commit-time.py data/
Commit time histogram (UTC) — data
Total commits: 2908  |  peak hour: 00:xx UTC

  00  │██████████████████████████████████████████████████  236
  01  │██████████████████████████████████                  160
  02  │█████████████████████████████████                   154
  03  │████████████████████████████                        134
  04  │██████████████████████                              102
  05  │████████████                                        57
  06  │████                                                19
  07  │██                                                  10
  08  │████                                                19
  09  │██████████                                          46
  10  │██████████████████████                              106
  11  │██████████████████████                              102
  12  │██████████████████████████████                      141
  13  │█████████████████████                               97
  14  │██████████████████████████████                      141
  15  │█████████████████                                   78
  16  │█████████████████████████████                       138
  17  │██████████████████████████████████████              180
  18  │█████████████████████████████████████████           192
  19  │█████████████████████████████████████               174
  20  │██████████████████████████████████                  160
  21  │███████████████████████████                         129
  22  │███████████████████████████████                     145
  23  │████████████████████████████████████████            188

```

## Conventional commit analysis

```
Conventional Commit Analysis — steipete-2025-12
=======================================================
  Total commits     : 2908
  Conventional      : 2761  (95%)
  Non-conventional  : 147
  Breaking changes  : 1

By type  (n=2761)
─────────────────
  fix                  ████████████████████████████████████ 32%       894
  chore                ███████████ 12%                                340
  feat                 █████████ 10%                                  283
  docs                 ████████ 10%                                   269
  test                 ████ 6%                                        163
  mac                  ███ 5%                                         140
  style                ███ 5%                                         130
  refactor             █ 3%                                           79
  macos                ██ 1%                                          37
  ci                   ██ 1%                                          35
  ui                   █ 1%                                           32
  cli                  █ 1%                                           29
  web                  █ 1%                                           28
  gateway              █ 1%                                           28
  webchat              █ 1%                                           26
```

## Commit signals

```
https://github.com/Dicklesworthstone/pi_agent_rust/blob/main/.github/workflows/ci.ymlctories
  2025-12-31  6517b05a  vietdev99/openclaw  feat commit changed code without tests; commit spans many files or directories
```

## Context switching

```
2025-12-01     5c   2r    1s  |.....                                                   |
2025-12-02   100c   4r   99s  |........................................................|
2025-12-03   100c   2r   75s  |BBBBBBBBBBDDDDDBBBBDDDDDBBBBBDDDDBBBBBDDDDDBBBBDDDDDDDDD|
2025-12-04   100c  15r   91s  |........................................................|
2025-12-05   100c   3r   99s  |........................................................|
2025-12-06   100c   2r   25s  |GGGGGGGGGGGGGGGGGGGGGGGGGGGGGBBBBGGGGGBBBBBBBBBBBBBBBBBB|
2025-12-07   100c   2r    1s  |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEGGGGGGGGGGGGGGGGGGGGGGGGG|
2025-12-08   100c   2r    1s  |AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCCCCCCCCCC|
2025-12-09   100c   1r    0s  |AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA|
2025-12-10   100c   2r   77s  |BBBBBDDDDDBBBBBDDDDBBBBBDDDDDBBBBDDDDDBBBBBDDDDDDDDDDDDD|
2025-12-11   100c  27r   99s  |........................................................|
2025-12-12   100c   3r   16s  |..DDDDDDDDDDDDDDDDDDDDDDDDDDDAAAADAAAAAAAAAAAAAAAAAAAAAA|
2025-12-13   100c   1r    0s  |EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE|
2025-12-14   100c   1r    0s  |BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|
2025-12-15     3c   1r    0s  |...                                                     |
2025-12-16   100c  10r   99s  |HEBAF.HGDCF.EBAC.HGBAF.EGDC.HEBAF.HGDCF.EBAC.HGBAF.EGDC.|
2025-12-17   100c   2r    3s  |CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCFFFFFFFF|
2025-12-18   100c   2r    5s  |AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCCCCCC|
2025-12-19   100c   3r   82s  |........................................................|
2025-12-20   100c   1r    0s  |BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|
2025-12-21   100c   2r   47s  |CCCCCCCCCCFFFFFCCCCFFFFFCCCCCFFFFFFFFFFFFFFFFFFFFFFFFFFF|
2025-12-22   100c   4r   99s  |........................................................|
2025-12-23   100c   3r   99s  |CFFFFCCCCCFFFFFCCCCFFFFFCCCCCFFFFCCCCCFFFFFCCCCFC...FFFF|
2025-12-24   100c   3r   62s  |ACCCCAAAACCCCCCCCCCCCCCCCCCCCCFFFCCCCCFFFFFCCCCFFFFFCCCC|
2025-12-25   100c   6r   84s  |........................................................|
2025-12-26   100c   2r   51s  |HHHHHHHHHHHHHHHHHHHHHHHHHHHHHEEEEHHHHHEEEEEHHHHEEEEEHHHH|
2025-12-27   100c   5r   99s  |........................................................|
2025-12-28   100c  13r   93s  |........................................................|
2025-12-29   100c   5r   97s  |..BADADBADADBABDCDCBABABDCDCDABABDCADCDCADCDCADADCADADCA|
2025-12-30   100c   3r   94s  |........................................................|
2025-12-31   100c  11r   99s  |........................................................|
```

