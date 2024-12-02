#!/bin/python3

import fileinput
import collections

Point = collections.namedtuple('Point', ['x', 'y'])

def trend(a, b):
    if a == b: return 0
    if a > b: return -1
    return 1

rocks = set()
sand = set()

sandSource = Point(500, 0)
topleft = sandSource
bottomright = sandSource

def extendField(where):
    global topleft, bottomright
    topleft = Point(min(topleft.x, where.x), min(topleft.y, where.y))
    bottomright = Point(max(bottomright.x, where.x), max(bottomright.y, where.y))

def lost(where):
    return not (topleft.x <= where.x <= bottomright.x and topleft.y <= where.y <= bottomright.y)

def readField():
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
                here = Point(here.x + cont.x, here.y + cont.y)


preferredDrops = [Point(0, 1), Point(-1, 1), Point(1, 1)]

def dropSand(where):
    while not lost(where):
        for drop in preferredDrops:
            option = Point(where.x + drop.x, where.y + drop.y)
            if option not in rocks and option not in sand:
                there = option
                break

        if where == there:
            return where

        where = there


readField()

print(f"{topleft=} {bottomright=}")


for _ in range(1000):
    settled = dropSand(sandSource)

    if not settled:
        break

    sand.add(settled)

print()
for y in range(topleft.y, bottomright.y+1):
    for x in range(topleft.x, bottomright.x+1):
        if Point(x, y) in rocks:
            print("#", end='')
        elif Point(x, y) in sand:
            print("o", end='')
        else:
            print(".", end='')

    print()

print(f"{len(sand)=}")
