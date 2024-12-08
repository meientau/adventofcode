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
        bottom_right = Point(max(bottom_right.u, u), max(bottom_right.v, v))
        if char != '.':
            locations[char].append(Point(u, v))

if len(locations) < 5:
    pprint(locations)

antinodes = set()
for frequency, antennas in locations.items():
    for a, b in permutations(antennas, 2):
        x = Point(2*b.u - a.u, 2*b.v - a.v)

        if len(locations) < 5:
            print(f"{frequency=} {a=} {b=} {x=}")

        if still_inside(x):
            antinodes.add(x)

if len(locations) < 5:
    pprint(antinodes)
print(len(antinodes))

# 364 0.080s
