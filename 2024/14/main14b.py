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

debug = len(robots) < 20
pmin = P(0, 0)
pmax = P(101, 103)
if debug: pmax = P(11, 7)
if debug: pprint(robots)
pmid = P(pmax.u//2, pmax.v//2)
print(f"{pmid=}")

def clamp(v, m):
    return (v + m) % m

def in_tree(p):
    return p.v > 2*pmax.v*abs(p.u - pmid.u)/pmax.u

def safety_check(robots):
    return sum(1 for r in robots if in_tree(r.p))

def safety_recheck(a, b):
    if in_tree(a) and not in_tree(b):
        return -1
    if not in_tree(a) and in_tree(b):
        return 1
    return 0

safety = safety_check(robots)
after = list()
secs = 7492
pic = [['.' for v in range(pmax.v)] for u in range(pmax.u)]
after = list()
for r in robots:
    p = P(clamp(r.p.u + secs * r.v.u, pmax.u),
          clamp(r.p.v + secs * r.v.v, pmax.v))
    after.append(R(p, r.v))
    pic[p.u][p.v] = 'X'

safe = safety_check(after)
if safe > 300:
    print(f"{secs=} {safe=}")

print()
for v in range(pmax.v):
    for u in range(pmax.u):
        print(pic[u][v], end='')
    print()
# 7492
