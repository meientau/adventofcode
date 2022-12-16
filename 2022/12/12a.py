#!/bin/python3

import fileinput
from copy import copy
import os


class Point:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __repr__(self):
        return f"({self.u: 5}, {self.v: 5})"

    def __str__(self):
        return self.__repr__()

    def __copy(self):
        return Point(self.u, self.v)

    def __eq__(self, other):
        return self.u == other.u and self.v == other.v

    def __hash__(self):
        return self.u*31 + self.v

    def __add__(self, m):
        return Point(self.u + m.increment.u, self.v + m.increment.v)

    def __sub__(self, m):
        return Point(self.u - m.increment.u, self.v - m.increment.v)


class World:
    def __init__(self):
        self.data = [line for line in [rawline.strip() for rawline in fileinput.input()] if line.strip()]
        self.height = len(self.data)
        self.width = len(self.data[0])
        self.overlay = [list([None] * self.width) for row in range(self.height)]

    def elevation(self, p):
        c = self.data[p.v][p.u]
        if c.islower():
            return ord(c)

        if c == 'S':
            return ord('a')

        if c == 'E':
            return ord('z')

    def can_go(self, here, there):
        return (0 <= there.u < self.width and 0 <= there.v < self.height
                and not self.overlay[there.v][there.u]
                and self.elevation(there) <= self.elevation(here) + 1)

    def is_target(self, p):
        return self.data[p.v][p.u] == 'E'

    def __repr__(self):
        return '\n'.join([''.join([f"\033[7m{o}\033[0m" if o else w for w, o in zip(*row)]) for row in zip(self.data, self.overlay)])

    def __str__(self):
        return self.__repr__()

    def put(self, p, s):
        self.overlay[p.v][p.u] = s

    def remove(self, p):
        self.overlay[p.v][p.u] = None



class State:
    def __init__(self):
        self.find_start_and_target()

    def find_start_and_target(self):
        for v, row in enumerate(world.data):
            for u, c in enumerate(row):
                if c == 'S':
                    self.start = Point(u, v)
                if c == 'E':
                    self.target = Point(u, v)

    def __repr__(self):
        return f"State({self.start=}->{self.target=})"


class Movement:
    def __init__(self, increment, symbol):
        self.increment = increment
        self.symbol = symbol


class Walker:
    ds = [
        Movement(Point(1, 0), '>'),
        Movement(Point(0, -1), '^'),
        Movement(Point(-1, 0), '<'),
        Movement(Point(0, 1), 'v'),
    ]

    def __init__(self, state, world):
        self.path = set()
        self.state = state
        self.world = world
        self.here = copy(state.start)

        self.shortest = None

        self.bored = 0

    def walk(self, movement):
        there = self.here + movement
        if not self.world.can_go(self.here, there):
            return False

        self.world.put(self.here, movement.symbol)
        self.path.add(self.here)
        self.here = there
        return True

    def unwalk(self, movement):
        self.here -= movement
        self.world.remove(self.here)
        self.path.remove(self.here)

    def record_path(self):
        if not self.shortest or len(self.shortest) > len(self.path):
            self.shortest = set(self.path)
            print()
            print(len(self.shortest))
            if world.width + world.height < 20:
                print(str(world))

    def walk_all(self):
        for m in Walker.ds:
            self.bored += 1
            if not self.bored % 1000000:
                print("\033[H\033[J", end="")
                print(str(world))

            if self.walk(m):

                if world.is_target(self.here):
                    self.record_path()
                else:
                    self.walk_all()

                self.unwalk(m)



world = World()
state = State()

if world.width + world.height < 20:
    print(str(world))

walker = Walker(state, world)
walker.walk_all()
