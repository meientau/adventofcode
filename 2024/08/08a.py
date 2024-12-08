from fileinput import input
from collections import namedtuple, defaultdict
from itertools import permutations
from pprint import pprint

Point = namedtuple("Point", ["u", "v"])
bottom_right = Point(0, 0)
def still_inside(p):
    return p.u >= 0 and p.v >= 0 and p.u <= bottom_right.u and p.v <= bottom_right.v

locations = defaultdict(list)

for v, line in enumerate(input()):
    line = line.strip()
    for u, char in enumerate(line):
        if char != '.':
            locations[char].append(Point(u, v))

if len(locations) < 5:
    pprint(locations)

antinodes = set()
for frequency, antennas in locations.items():
    for a, b in permutations(antennas, 2):
        if len(locations) < 5:
            print(f"{frequency=} {a=} {b=}")
