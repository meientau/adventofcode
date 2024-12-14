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

def clamp(v, m):
    return (v + m) % m

def safety(robots):
    safety = (
        sum(1 for r in robots if r.p.u < pmid.u and r.p.v < pmid.v),
        sum(1 for r in robots if r.p.u > pmid.u and r.p.v < pmid.v),
        sum(1 for r in robots if r.p.u < pmid.u and r.p.v > pmid.v),
        sum(1 for r in robots if r.p.u > pmid.u and r.p.v > pmid.v)
    )
    if debug: print(safety)
    return safety


sec = 100
after = list()
for r in robots:
    after.append(R(P(clamp(r.p.u + 100 * r.v.u, pmax.u),
                     clamp(r.p.v + 100 * r.v.v, pmax.v)),
                   r.v))

robots = after


if debug: pprint(robots)
safety = safety(robots)
print(safety[0]*safety[1]*safety[2]*safety[3])
# 208437768  0.082s
