import fileinput
from collections import namedtuple

P = namedtuple("P", "u v", defaults=[0, 0])
directions = {P(-1, 0), P(1, 0), P(0, -1), P(0, 1)}
P.__add__ = lambda self, o: P(self.u + o.u, self.v + o.v)

start = None
end = None
spaces = set()
pmin = P()
pmax = P()

def read_all():
    global pmax, start, end
    for v, line in enumerate(fileinput.input()):
        for u, char in enumerate(line.strip()):
            p = P(u, v)
            pmax = P(max(pmax.u, p.u), max(pmax.v, p.v))
            if char == 'S':
                start = p
            elif char == 'E':
                end = p
            elif char == '.':
                spaces.add(p)

def all_field():
    for v in range(pmax.v+1):
        for u in range(pmax.u+1):
            yield P(u, v)


distances = dict()
def print_field():
    for p in all_field():
        if not p.u:
            print()

        if p in distances:
            c = '-'
        elif p in spaces:
            c = '.'
        elif p == start:
            c = 'S'
        elif p == end:
            c = 'E'
        else:
            c = '#'

        print(c, end='')
    print()

def find_path():
    todo = {start}
    accu = set()
    for dist in range(pmax.u*pmax.v):
        for p in todo:
            for d in directions:
                next_p = p + d
                if next_p in spaces and next_p not in distances:
                    accu.add(next_p)
                    distances[next_p] = dist

        if end in distances:
            return

        print(f"{dist=} {accu=}")
        todo = accu
        accu = set()


read_all()
print_field()
find_path()
print_field()
