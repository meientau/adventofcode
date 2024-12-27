import fileinput
from collections import defaultdict
from itertools import chain
from pprint import pprint

from structures16 import *

moves = defaultdict(set)            # all moves on a point
network = defaultdict(set)          # all links starting at a point

start = None
end = None
spaces = set()
pmin = Point()
pmax = Point()

def read_all():
    global pmax, start, end
    for v, line in enumerate(fileinput.input()):
        for u, char in enumerate(line.strip()):
            p = Point(u, v)
            pmax = Point(max(pmax.u, p.u), max(pmax.v, p.v))
            if char == 'S':
                start = p
            elif char == 'E':
                end = p
            elif char == '.':
                spaces.add(p)

    spaces.add(start)
    spaces.add(end)


debug = len(spaces) < 100


def all_field():
    for v in range(pmax.v+1):
        for u in range(pmax.u+1):
            yield Point(u, v)


def print_field():
    for p in all_field():
        if not p.u:
            print()

        if p in moves:
            c = str(len(moves[p]))
        elif p == start:
            c = 'S'
        elif p == end:
            c = 'E'
        elif p in spaces:
            c = '.'
        else:
            c = '#'

        print(c, end='')
    print()


def find_moves():
    for p in all_field():
        if p not in spaces: continue
        is_node = (p == start
                   or len(set(axis for axis, offset in zip(axes, headings)
                              if p+offset in spaces)) > 1)
        if is_node:
            for h, offset in enumerate(headings):
                if p + offset in spaces:
                    m = Move(p, h)
                    moves[p].add(m)


def find_links():
    max_distance = max(pmax.u, pmax.v)
    for m in chain.from_iterable(moves.values()):
        closest_node = set()
        closest_distance = max_distance
        for p, o in moves.items():
            if not m.leads_to(p): continue

            vector = p - m.p
            distance = abs(vector.u + vector.v)
            if not closest_node or closest_distance > distance:
                closest_node = o
                closest_distance = distance

        for target in closest_node:
            if abs(m.h - target.h) == 2: continue
            link = Link(m, target)
            network[m.p].add(link)


def walk_network():
    candidates = [Candidate(link) for link in network[start]]
    pprint(candidates)
    todo: do not link through walls


read_all()
if debug: print_field()
find_moves()
if debug: print_field()
pprint(moves[start])
pprint(moves[end])
find_links()
pprint(network)
walk_network()
if debug: print_field()
print(len(network))
