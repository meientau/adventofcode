import fileinput
import sys

from structures16 import Point, headings, headingsymbols

sys.setrecursionlimit(10000)


start = None
end = None
spaces = set()
pmin = Point()
pmax = Point()
moves = dict()

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

    global debug
    debug = len(spaces) < 200
    print(f"{len(spaces)=}")

def all_field():
    for v in range(pmax.v+1):
        for u in range(pmax.u+1):
            yield Point(u, v)


def print_field():
    for p in all_field():
        if not p.u:
            print()

        if p in moves:
            c = moves[p]
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


def find_score(here, head):
    if here == end:
        if debug:
            print_field()
        else:
            print(len(moves))
        return 0

    score = sys.maxsize
    any_step_made = False
    for h, off in zip(headingsymbols, headings):
        newpos = here + off

        if newpos in spaces and newpos not in moves:
            any_step_made = True
            moves[here] = h
            add_score = 1 + 1000 * int(head != h)
            score = min(score, find_score(newpos, h) + add_score)
            del moves[here]

    return score

def start_find_score():
    return find_score(start, headingsymbols[0])


read_all()
if debug: print_field()
score = start_find_score()
if debug: print_field()
print(f"{score=}")

# 238836 too high
# score=228812  0.216s too high (using invalid caching)
