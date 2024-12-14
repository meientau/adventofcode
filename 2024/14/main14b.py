# Now I know where the tree is, I can show it.
# See main14b-guess-one.py for how I got here, and it was not a straight path.

import fileinput
import re
from collections import namedtuple
from pprint import pprint

# p=0,4 v=3,-3
re_num = re.compile(r'-?\d+')
P = namedtuple("P", ["u", "v"])
R = namedtuple("R", ["p", "v"])

robots = list()
for line in fileinput.input():
    num = [int(n) for n in re_num.findall(line)]
    robots.append(R(P(*num[:2]), P(*num[2:])))

pmin = P(0, 0)
pmax = P(101, 103)

def clamp(v, m):
    return v % m

after = list()
secs = 7492
pic = [['.' for v in range(pmax.v)] for u in range(pmax.u)]
for r in robots:
    p = P(clamp(r.p.u + secs * r.v.u, pmax.u),
          clamp(r.p.v + secs * r.v.v, pmax.v))
    after.append(R(p, r.v))
    pic[p.u][p.v] = 'X'

print()
for v in range(pmax.v):
    for u in range(pmax.u):
        print(pic[u][v], end='')
    print()

# 7492
