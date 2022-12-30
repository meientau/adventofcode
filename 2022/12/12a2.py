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


class Movement:
    def __init__(self, increment, symbol):
        self.increment = increment
        self.symbol = symbol


ds = [
    Movement(Point(1, 0), '>'),
    Movement(Point(0, -1), '^'),
    Movement(Point(-1, 0), '<'),
    Movement(Point(0, 1), 'v'),
]


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
                and (self.elevation(there) <= self.elevation(here) + 1))

                # and (self.elevation(there) == self.elevation(here) or self.elevation(there) == self.elevation(here) + 1))

    def is_target(self, p):
        return self.data[p.v][p.u] == 'E'

    def __repr__(self):
        return '\n'.join([''.join([self.encode(w, o) for w, o in zip(*row)]) for row in zip(self.data, self.overlay)])

    def encode(self, w, o):
        if isinstance(o, int):
            o = o % 10

        if o is None:
            o = " "

        if o == '@':
            return  f"\033[7m\033[32m{w}\033[33m{o}\033[0m "

        return f"\033[32m{w}\033[33m{o}\033[0m "

    def __str__(self):
        return self.__repr__()

    def put(self, p, s):
        self.overlay[p.v][p.u] = s

    def put_min(self, here, there):
        if not self.can_go(here, there):
            return False

        self.overlay[there.v][there.u] = self.overlay[here.v][here.u] + 1
        return True

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


class Filler:
    def __init__(self, state, world):
        self.path = set()
        self.state = state
        self.world = world

    def fill_all(self):
        self.looking_at = set([self.state.start])
        self.world.put(self.state.start, 1)

        for distance in range(1, self.world.height * self.world.width):
            visited = set()
            for here in self.looking_at:
                for move in ds:
                    there = here + move
                    if self.world.put_min(here, there):
                        visited.add(there)

            if self.state.target in visited:
                print(f"{distance=}")
                break

            if not visited:
                for here in self.looking_at:
                    self.world.put(here, '@')
                    break

            self.looking_at = visited



world = World()
state = State()

filler = Filler(state, world)
filler.fill_all()

print(str(world))
