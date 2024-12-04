from fileinput import input
from collections import namedtuple
from pprint import pprint

Point = namedtuple("Point", ["u", "v"])

crossing = "A"
goodneighbours = {"MMSS", "MSSM", "SSMM", "SMMS"}
directions = [
    Point( 1,  1),
    Point(-1,  1),
    Point(-1, -1),
    Point( 1, -1),
]
def plus(point, direction):
    return Point(point.u + direction.u, point.v + direction.v)

mslocations = dict()
alocations = set()

minmax = (5, 5, 5, 5)

for v, line in enumerate(input()):
    line = line.strip()
    for u, char in enumerate(line):
        minmax = (min(u, minmax[0]), min(v, minmax[1]), max(u, minmax[2]), max(v, minmax[3]))
        p = Point(u,v)
        mslocations[p] = char
        if char == crossing:
            alocations.add(p)
        if char in goodneighbours:
            mslocations[p] = char

if len(alocations) < 100:
    pprint(alocations)
    pprint(mslocations)

found = set()
other = set()
for point in alocations:
    neighbourlocations = [plus(point, direction) for direction in directions]
    neighbours = ''.join(mslocations[p] for p in neighbourlocations if p in mslocations)
    if neighbours in goodneighbours:
        found.add(point)
        other |= set(neighbourlocations)


print(len(found))
if len(found) < 100:
    pprint(found)

    for v in range(minmax[0], minmax[2]+1):
        for u in range(minmax[1], minmax[3]+1):
            p = Point(u, v)
            if p in found:
                if p in alocations:
                    print('*', end='')
                else:
                    print('-', end='')

            elif p in other:
                print(mslocations[p], end='')
            else:
                print('.', end='')
        print()


# small n=9 t=0.02s
# full  n=1916 t=0.036s