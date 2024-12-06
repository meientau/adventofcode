import fileinput
from collections import namedtuple

Point = namedtuple("Point", ["u", "v"])
directions = [
    Point( 0, -1),
    Point( 1,  0),
    Point( 0,  1),
    Point(-1,  0),
]

def plus(p, o):
    return Point(p.u + o.u, p.v + o.v)

def still_inside(p):
    return p.u >= 0 and p.v >= 0 and p.u <= bottom_right.u and p.v <= bottom_right.v

obstacles = set()
starting_point = None
bottom_right = Point(0, 0)
for v, line in enumerate(fileinput.input()):
    for u, char in enumerate(line):
        bottom_right = Point(max(bottom_right.u, u), max(bottom_right.v, v))
        if char == '#':
            obstacles.add(Point(u, v))
        elif char == '^':
            starting_point = Point(u, v)

if len(obstacles) < 100:
    print(obstacles)
    print(f"{starting_point=}")

seen = set()
here = starting_point
heading = 0
while still_inside(here):
    seen.add(here) # remember that we've been here
    next_stop = plus(here, directions[heading])
    hit = next_stop in obstacles
    if hit:
        heading = (heading + 1) % 4
        next_stop = plus(here, directions[heading])
        hit = next_stop in obstacles
        if hit:
            heading = (heading + 1) % 4
            next_stop = plus(here, directions[heading])
    # after 2x hit we are going back where we came from, so that must be free.
    here = next_stop

if len(obstacles) < 100:
    for v in range(bottom_right.v+1):
        for u in range(bottom_right.u+1):
            here = Point(u, v)
            if here in obstacles:
                print("#", end="")
            elif here == starting_point:
                print("X", end="")
            elif here in seen:
                print("x", end="")
            else:
                print(".", end="")
        print()

print(f"{len(seen)=}")

# len(seen)=41   0.015s
# len(seen)=5531 0.034s
