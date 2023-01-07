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


class Field:
    def __init__(self, lines=None):
        self.sensors = dict()
        self.beacons = set()
        self.covered = set()
        self.tl = None
        self.br = None

        if lines:
            self.fill(lines)

    def isBig(self):
        return distance(self.tl, self.br) < 10

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
                return True

        return False

    def countRow(self, y):
        return sum(self.inrange(Point(x, y)) for x in range(self.tl.x, self.br.x+1)
                   if Point(x, y) not in self.beacons)


if __name__ == "__main__":
    field = Field(sys.stdin.readlines())

    if not field.isBig():
        print(field.paint())

    if len(sys.argv) == 2:
        row = int(sys.argv[1])
        print(f"{field.countRow(row)=}")
