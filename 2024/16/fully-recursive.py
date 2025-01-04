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


best_score = sys.maxsize
def find_score(here, head, old_score):
    global best_score
    if old_score > best_score:
        return

    if here == end:
        if debug:
            print_field()
        else:
            print(old_score)

        best_score = min(old_score, best_score)
        return

    for h, off in zip(headingsymbols, headings):
        newpos = here + off

        if newpos in spaces and newpos not in moves:
            moves[here] = h
            add_score = 1 + 1000 * int(head != h)
            find_score(newpos, h, old_score+add_score)
            del moves[here]

    return

def start_find_score():
    return find_score(start, headingsymbols[0], 0)


read_all()
if debug: print_field()
start_find_score()
if debug: print_field()
print(f"{best_score=}")

# 238836 too high
# 228812 too high
