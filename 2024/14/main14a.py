import fileinput
import re
from collections import namedtuple
from pprint import pprint

# p=0,4 v=3,-3
# - each robot has to x/y pairs:
# - position
# - velocity
# Let's just look for four numbers (sign optional) and
# assign the first two as x/y for the position,
# the last two as the velocity.

# Find groups of digits, optionally lead by a minus sign:
re_num = re.compile(r'-?\d+')

# Give names to x/y pairs and robots:
# I like using u/v instead of x/y for integer coordinates.
P = namedtuple("P", ["u", "v"])
R = namedtuple("R", ["p", "v"])


robots = list()
for line in fileinput.input():
    # find four numbers
    num = [int(n) for n in re_num.findall(line)]
    # drop the first two into the point that becomes the position,
    # the rest into the point that becomes the velocity.
    robots.append(R(P(*num[:2]), P(*num[2:])))

# When looking at the small sample, show our work:
debug = len(robots) < 20

# For display, define the size of the area where the robots live:
pmin = P(0, 0)
pmax = P(101, 103)
if debug: pmax = P(11, 7)
pmid = P(pmax.u//2, pmax.v//2)

# If debugging, show what we read
if debug: pprint(robots)
print(f"{pmin=} {pmid=} {pmax=}")

# Limit a coordinate to the playfield, rolling around the edges:
def clamp(v, m):
    return (v + m) % m

# Count robots in quadrants.
def safety(robots):
    safety = (
        sum(1 for r in robots if r.p.u < pmid.u and r.p.v < pmid.v),
        sum(1 for r in robots if r.p.u > pmid.u and r.p.v < pmid.v),
        sum(1 for r in robots if r.p.u < pmid.u and r.p.v > pmid.v),
        sum(1 for r in robots if r.p.u > pmid.u and r.p.v > pmid.v)
    )
    if debug: print(safety)
    return safety


# Fast-forward to second 100:
sec = 100
after = list()
for r in robots:
    after.append(R(P(clamp(r.p.u + 100 * r.v.u, pmax.u),
                     clamp(r.p.v + 100 * r.v.v, pmax.v)),
                   r.v))

robots = after

# Print all the new detail:
if debug: pprint(robots)

# Calculate the safety factor:
safety = safety(robots)
print(safety[0]*safety[1]*safety[2]*safety[3])

# 208437768  0.082s
