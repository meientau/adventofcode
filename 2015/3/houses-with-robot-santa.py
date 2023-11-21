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

    served = set()

    def __init__(self):
        self.here = Point(0,0)

    def move(self, direction):
        Houses.served.add(self.here)
        self.here += Houses.directions[direction]
        Houses.served.add(self.here)

    def run(self, directions):
        for d in directions:
            self.move(d)

    def how_many_houses(self):
        return len(Houses.served)


if __name__ == "__main__":
    directions = sys.stdin.readline().strip()
    santa = Houses()
    robot_santa = Houses()
    print(f"input is:   {directions[:10]}")
    print(f"santa sees: {directions[:10][::2]}")
    print(f"robot sees: {directions[:10][1::2]}")
    santa.run(directions[::2])
    robot_santa.run(directions[1::2])
    print(f"Houses served: {santa.how_many_houses()}")
