import fileinput
from collections import namedtuple, defaultdict, OrderedDict
from pprint import pprint

P = namedtuple("P", "u v", defaults=[0, 0])
P.__add__ = lambda self, o: P(self.u + o.u, self.v + o.v)

S = namedtuple("S", "p head score prev")
S.__repr__ = lambda self: f"({self.p} {self.head} {self.score} {self.prev.p})"
S.__str__ = S.__repr__

headings = [P( 1,  0), P( 0, -1), P(-1,  0), P( 0,  1)]
headingsymbols = '>^<v'

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

    spaces.add(start)
    spaces.add(end)


def all_field():
    for v in range(pmax.v+1):
        for u in range(pmax.u+1):
            yield P(u, v)


seen = defaultdict(set)
def print_field():
    for p in all_field():
        if not p.u:
            print()

        if p in seen:
            shortest = min(seen[p])
            c = headingsymbols[shortest.head]
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


def find_paths():
    global crash, crash2
    interesting = {end, P(13, 13)}

    todo = {S(p=start+headings[2], head=0, score=0, prev=None)}
    accu = set()
    while todo:
        for s in todo:
            for h, offset in enumerate(headings):
                next_p = s.p + offset
                if next_p in spaces:
                    headingscore = 1000*abs(s.head - h)
                    score = s.score + 1 + headingscore
                    step = S(next_p, h, score, s)
                    if next_p in interesting: pprint(step)
                    if seen[next_p]:
                        if next_p in interesting: print(f"{seen[next_p]=}")
                        minscore = min(s.score for s in seen[next_p])
                        if next_p in interesting: print(f"{score=} {minscore=}")
                        if score > minscore:
                            if next_p in interesting: print("skipping")
                            continue

                    if next_p in interesting: print("adding")
                    seen[next_p].add(step)
                    if len(accu) > 20: return
                    accu.add(step)

        print(f"{len(todo)=} {len(accu)=}")

        todo = accu
        accu = set()


read_all()
print_field()
find_paths()
print_field()
pprint(seen[end])
print(f"{start=} {end=}")
