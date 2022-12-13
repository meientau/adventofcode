#!/bin/python3

import sys
from collections import defaultdict
import copy
import math


class Move:
    STEPS = {
        'U': (0,1),
        'R': (1,0),
        'D': (0,-1),
        'L': (-1,0)
    }
    def __init__(self, direction, steps):
        self.direction = direction
        self.steps = int(steps)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.direction}->{self.steps}"


class Position:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"({self.u:3},{self.v:3})"

    def __eq__(self, other):
        return self.u == other.u and self.v == other.v

    def __lt__(self, other):
        return self.u < other.u or self.v < other.v

    def __hash__(self):
        return self.u + 31 * self.v

    def __add__(self, move):
        return Position(self.u + Move.STEPS[move.direction][0],
                        self.v + Move.STEPS[move.direction][1])


class Marks:
    START = 's'
    HEAD = 'H'
    TAIL = 'T'
    SEEN = '#'
    EMPTY = '.'

    def __init__(self):
        self.marks = set()

    def __add__(self, mark):
        self.marks.add(mark)
        return self

    def __sub__(self, mark):
        self.marks.remove(mark)

    def __contains__(self, mark):
        return mark in self.marks

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        for i in [Marks.HEAD, Marks.TAIL, Marks.START, Marks.SEEN]:
            if i in self.marks:
                return i

        return Marks.EMPTY


class Field:
    def __init__(self):
        self.l = 0
        self.r = 6
        self.t = 5
        self.b = 0
        self.marks = defaultdict(Marks)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '\n'.join([''.join([str(self.marks[Position(u, v)])
                                   for u in self.rowrange()])
                          for v in self.colrange()])

    def rowrange(self):
        return range(self.l, self.r+1)

    def colrange(self):
        return range(self.t, self.b-1, -1)

    def __getitem__(self, position):
        self.extend(position)
        return self.marks[position]

    def __setitem__(self, position, item):
        self.extend(position)
        self.marks[position] += item

    def count(self, mark):
        return sum([mark in self.marks[Position(u, v)] for u in self.rowrange() for v in self.colrange()])

    def extend(self, position):
        self.l = min(self.l, position.u)
        self.r = max(self.r, position.u)
        self.t = max(self.t, position.v)
        self.b = min(self.b, position.v)


field = Field()
start = Position(0,0)
field[start] = Marks.START

class Mob:
    def __init__(self, mark):
        self.mark = mark
        self.position = None
        self.move(start)

    def move(self, newposition):
        if self.position:
            field[self.position] -= self.mark
        self.lastposition = self.position
        self.position = newposition
        if self.position:
            field[self.position] += self.mark

    def follow(self, other):
        field[self.position] += Marks.SEEN
        d = math.sqrt((self.position.u - other.position.u)**2 + (self.position.v - other.position.v)**2)
        if d >= 2:
            self.move(other.lastposition)

        field[self.position] += Marks.SEEN


moves = [Move(*line.split()) for line in sys.stdin.readlines()]

head = Mob(Marks.HEAD)
tail = Mob(Marks.TAIL)
seen = set()

print(moves)
# print(field)
# head.move(Position(1,0))
# tail.follow(head)
# print(field)
# head.move(Position(2,0))
# tail.follow(head)
# print(field)
# head.move(Position(2,1))
# tail.follow(head)
# print(field)
# head.move(Position(2,2))
# tail.follow(head)
# print(field)

#moves = moves[:99]
for move in moves:
    print(move)
    for i in range(move.steps):
        head.move(head.position + move)
        tail.follow(head)
    if len(moves) < 100:
        print(field)

print(field.count(Marks.SEEN))
