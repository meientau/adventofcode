#!/bin/python3

import sys
from collections import namedtuple

class Point(namedtuple('Point', ['u', 'v'])):
    # set __slots__ to an empty tuple to help keep memory requirements
    # low by preventing the creation of instance dictionaries.

    # __slots__ = ()


    def __add__(self, other):
        return Point(self.u + other.u, self.v + other.v)


class Houses:
    directions = {
        '^': Point(0, -1),
        'v': Point(0, 1),
        '<': Point(-1, 0),
        '>': Point(1, 0),
    }

    def __init__(self):
        self.houses_served = set()
        self.here = Point(0,0)

    def move(self, direction):
        self.houses_served.add(self.here)
        self.here += Houses.directions[direction]
        self.houses_served.add(self.here)

    def run(self, directions):
        for d in directions:
            self.move(d)

    def how_many_houses(self):
        return len(self.houses_served)


if __name__ == "__main__":
    directions = sys.stdin.readline().strip()
    h = Houses()
    h.run(directions)
    print(f"Houses served: {len(h.houses_served)}")
