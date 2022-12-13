#!/bin/python3

floor = 0
instructions = '(.)'
firstbasement = None
for i, c in enumerate(input(), 1):
    floor -= instructions.index(c) - 1
    if floor == -1:
        firstbasement = i
        break

print(f"{floor=} {firstbasement=}")
