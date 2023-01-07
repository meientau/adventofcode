#!/bin/python3

import sys
import unittest

from collections import namedtuple
import re


Point = namedtuple('Point', ['x', 'y'])


def distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


class Sensor:
    RE = re.compile(r"Sensor at x=(?P<x>-?\d+), y=(?P<y>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)")

    def __init__(self, description):
        m = Sensor.RE.match(description)
        if not m:
            raise ValueError(f"invalid {description=}")

        self.p = Point(int(m.group('x')), int(m.group('y')))
        self.b = Point(int(m.group('bx')), int(m.group('by')))
        self.d = abs(self.b.x - self.p.x) + abs(self.b.y - self.p.y)


    def __str__(self):
        return f"S({self.p.x},{self.p.y} [{self.d}])"

    def __repr__(self):
        return self.__str__()


class Field:
    def __init__(self, lines=None):
        self.sensors = dict()
        self.beacons = set()
        self.covered = set()
        self.tl = None
        self.br = None
        self.fullRow = set()

        if lines:
            self.fill(lines)

        print(f"{distance(self.tl, self.br)=}")

    def isBig(self):
        return distance(self.tl, self.br) > 50

    def fill(self, lines):
        for line in lines:
            self.add(Sensor(line))

    def extend(self, p):
        if self.tl is None:
            self.tl = p
            self.br = p
            return

        self.tl = Point(min(self.tl.x, p.x), min(self.tl.y, p.y))
        self.br = Point(max(self.br.x, p.x), max(self.br.y, p.y))

    def add(self, sensor):
        self.sensors[sensor.p] = sensor
        self.beacons.add(sensor.b)
        self.extend(sensor.p)
        self.extend(sensor.b)

    def paint(self):
        result = ""

        for y in range(self.tl.y-5, self.br.y+1+5):
            for x in range(self.tl.x-5, self.br.x+1+5):
                where = Point(x, y)
                if where in self.sensors:
                    result += "S"
                elif where in self.fullRow:
                    result += "o"
                elif where in self.beacons:
                    result += "B"
                elif self.inrange(where):
                    result += "#"
                else:
                    result += "."

            result += "\n"

        return result

    def inrange(self, p):
        for s in self.sensors.values():
            if distance(s.p, p) <= s.d:
                return s

        return None

    def countRow(self, y):
        fullRow = set()

        for s in self.sensors.values():
            p = Point(s.p.x, y)
            rd = s.d - distance(s.p, p)
            a = s.p.x - rd
            b = s.p.x + rd
            print(f"{s=}: {a}...{b} ({(a + b)//2})")
            for x in range(a, b + 1):
                fullRow.add(Point(x, y))

        self.fullRow = fullRow - self.beacons
        count = len(self.fullRow)
        return count

if __name__ == "__main__":
    field = Field(sys.stdin.readlines())

    if len(sys.argv) == 2:
        row = int(sys.argv[1])
        print(f"{field.countRow(row)=}")

    if not field.isBig():
        print(field.paint())

# 6697770 too big

# ..####B######################..

# ..#########################.......
# ..ooooBoooooooooooooooooooooo......
# .###S#############.###########.....
