#!/bin/python3

import sys

field = sys.stdin.read()

nl = '\n'
rowstep = field.index(nl) + 1
pad = nl * (rowstep + 1)
field = pad + field + pad

ds = [1, rowstep, -1, -rowstep]

def is_hidden(op):
    height = field[op]
    for d in ds:
        p = op
        while True:
            p += d
            if field[p] == nl:
                return False
            if field[p] >= height:
                break

    return True

visible_trees = 0
for p in range(len(field)):
    if field[p] == nl: continue

    if is_hidden(p):
        if len(field) < 100:
            print(f" {field[p]} ", end='')
    else:
        if len(field) < 100:
            print(f"({field[p]})", end='')
        visible_trees += 1

    if not (p+1) % rowstep and len(field) < 100:
        print()

print(visible_trees)
