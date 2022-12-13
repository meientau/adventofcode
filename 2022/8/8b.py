#!/bin/python3

import sys

field = sys.stdin.read()
debug = False

nl = '\n'
rowstep = field.index(nl) + 1
pad = nl * (rowstep + 1)
field = pad + field + pad

ds = [1, rowstep, -1, -rowstep]

def scenic_score(op):
    #debug = op == 27 or op == 7
    height = field[op]
    debug and print(f"{op=}")
    debug and print(f"{height=}")
    totalscore = 1
    for d in ds:
        debug and print(f"{d=}")

        p = op
        score = 0
        while True:
            p += d
            debug and print(f"{p=} {field[p]=}")
            if  field[p] == nl:
                break

            score += 1
            if field[p] >= height:
                break

        if score:
            totalscore *= score

    return totalscore

max_score = 0
for p in range(len(field)):
    if field[p] == nl: continue

    score = scenic_score(p)
    max_score = max(score, max_score)
    if len(field) < 100:
        print(f" {field[p]}:{score:02}", end=(None if debug else ''))

    if not debug and not (p+1) % rowstep and len(field) < 100:
        print()

print(max_score)
