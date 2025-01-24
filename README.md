# eda-nijin
 ![LGTM](https://i.lgtm.fun/2vtu.png)

### USE
```bash
$ pip install eda-nijin
$ eda-nijin
Usage: eda-nijin [OPTIONS] KEYWORD
Try 'eda-nijin --help' for help.
╭─ Error ─────────────────────────────────────────────────────────────────────────────────────────────╮
│ Missing argument 'KEYWORD'.                                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────╯
$ eda-nijin --help
 Usage: eda-nijin [OPTIONS] KEYWORD

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────╮
│ *    keyword      TEXT  [default: None] [required]                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────╮
│ --asc            --no-asc                     [default: no-asc]                          │
│ --rcnt                               INTEGER  [default: 12]                              │
│ --keyword-sum    --no-keyword-sum             [default: no-keyword-sum]                  │
│ --help                                        Show this message and exit.                │
╰──────────────────────────────────────────────────────────────────────────────────────────╯

$ eda-nijin 자유
100%|███████████████████████████████████████████████████████| 24/24 [00:02<00:00,  9.89it/s]
|    | president   |   count |
|---:|:------------|--------:|
|  0 | 박정희      |     513 |
|  1 | 이승만      |     438 |
|  2 | 노태우      |     399 |
|  3 | 김대중      |     305 |
|  4 | 문재인      |     275 |
|  5 | 김영삼      |     274 |
|  6 | 이명박      |     262 |
|  7 | 전두환      |     242 |
|  8 | 노무현      |     230 |
|  9 | 박근혜      |     111 |
| 10 | 최규하      |      14 |
| 11 | 윤보선      |       1 |
총 합계:12

$ eda-nijin 자유 --asc --rcnt 3 --keyword-sum
president  count  keyword_sum
      윤보선      1            6
      최규하     14           28
      박근혜    111          250
총 합계:3

```
### DEV
```bash
$ source .venv/bin/activate
$ pdm add pandas
$ pdm add -dG eda jupyter
```
### EDA
- run jupyterlab
```
$ jupyter lab
```
### REF
- [install jupyterlab](https://jupyter.org/install)
- https://pypi.org/project/president-speech/
