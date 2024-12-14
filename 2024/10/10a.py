import fileinput
from collections import namedtuple, defaultdict
from pprint import pprint

Point = namedtuple("Point", ["u", "v"])

neighbours = {Point( 0,  1), Point( 1,  0), Point( 0, -1), Point(-1,  0),}

def plus(point, direction):
    return Point(point.u + direction.u, point.v + direction.v)

locations = defaultdict(set)
for v, line in enumerate(fileinput.input()):
    line = line.strip()
    for u, char in enumerate(line):
        locations[int(char)].add(Point(u, v))

debug = len(locations[0]) < 10
if debug: pprint(locations)

scores = dict((p, {p}) for p in locations[9])
if debug: pprint(scores)
for height in range(8, -1, -1):
    new_scores = defaultdict(set)
    for p, reachable in scores.items():
        for d in neighbours:
            np = plus(p, d)
            if np in locations[height]:
                new_scores[np] |= scores[p]
    scores = new_scores

if debug: pprint(scores)

print(sum(len(v) for v in scores.values()))
# 798  0.087s
