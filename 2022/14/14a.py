#!/bin/python3

import fileinput
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

def trend(a, b):
    if a == b: return 0
    if a > b: return -1
    return 1

rocks = set()

sandSource = Point(500, 0)
topleft = sandSource
bottomright = sandSource

def extendField(where):
    global topleft, bottomright
    topleft = Point(min(topleft.x, where.x), min(topleft.y, where.y))
    bottomright = Point(max(bottomright.x, where.x), max(bottomright.y, where.y))

for i, line in enumerate(fileinput.input()):
    corners = [Point(*eval(c.strip())) for c in line.split('->')]

    if i < 6 or not i % 10:
        print(f"{i=} {corners=}")

    while corners:
        here = corners.pop(0)
        extendField(here)
        if not corners:
            rocks.add(here)
            break

        rest = 1000
        while here != corners[0] and rest:
            rest -= 1
            cont = Point(trend(here.x, corners[0].x), trend(here.y, corners[0].y))
            rocks.add(here)
            print(here)
            here = Point(here.x + cont.x, here.y + cont.y)

print(f"{topleft=} {bottomright=}")
for y in range(topleft.y, bottomright.y+1):
    for x in range(topleft.x, bottomright.x+1):
        if Point(x, y) in rocks:
            print("#", end='')
        else:
            print(".", end='')

    print()
