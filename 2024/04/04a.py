from fileinput import input
from collections import namedtuple

word = "XMAS"
locations = dict((char, list()) for char in word)
Point = namedtuple("Point", ["u", "v"])

for v, line in enumerate(input()):
    line = line.strip()
    for u, char in enumerate(line):
        locations[char].append(Point(u, v))

print(locations)
