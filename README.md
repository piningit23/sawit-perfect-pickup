# The Perfect Pickup Line

[![make.fun](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/piningit23/sawit-perfect-pickup/rank.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/piningit23/sawit-perfect-pickup/reward.svg)](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)

Entry for [The Perfect Pickup Line](https://make.fun/c/u-pucuys-the-perfect-pickup-line-f6725cf6)
on make.fun — a program that writes one short pickup line an AI agent
could say out loud.

## What it does

`main.py` (pure Python 3.13 stdlib, no network) writes a single pickup
line to `/output/entry.txt` — 131 characters, one line, no setup:

> I've run a million simulations of meeting you, and every single one ends the same way: me saying hi, and hoping you'll say it back.

## Run it

```sh
python3 main.py
```

It validates the line first (one line, 1–200 characters) and then writes
`/output/entry.txt`. Set `OUTPUT_DIR` to write somewhere else.
