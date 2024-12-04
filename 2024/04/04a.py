from fileinput import input
from collections import namedtuple
from pprint import pprint

Point = namedtuple("Point", ["u", "v"])

word = "XMAS"
directions = [
    Point( 1,  0),
    Point( 1,  1),
    Point( 0,  1),
    Point(-1,  1),
    Point(-1,  0),
    Point(-1, -1),
    Point( 0, -1),
    Point( 1, -1),
]
def plus(point, direction):
    return Point(point.u + direction.u, point.v + direction.v)

locations = dict((char, list()) for char in word)

for v, line in enumerate(input()):
    line = line.strip()
    for u, char in enumerate(line):
        locations[char].append(Point(u, v))

if len(locations['X']) < 100:
    pprint(locations)

todo = [ (p, d) for p in locations[word[0]] for d in directions ]
for char in word[1:]:
    nexttodo = list()
    for point, direction in todo:
        nextpoint = plus(point, direction)
        nexttodo += [(p, direction) for p in locations[char] if p == nextpoint]
    todo = nexttodo

print(len(todo))

# small n=18 t=0.02s
# full  n=2554 t=4s