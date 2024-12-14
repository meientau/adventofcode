"""
Now that I know what the tree looks like I have another idea.
What if we look at a histogram of only the robots on specific x places?

+-----------+
|.....x.....|
|...xxxxx...|
|....xxx....|
|..xxxxxxx..|
|xxxxxxxxxxx|
|....xxx....|
+-----------+

_...xXXXx..._
0112356532110

So tha max of 6 is much larger than the rest.
To get this number, we only need to calculate one coordinate, and we don't
need to paint it, just count occurrences in the buckets.
"""

import fileinput
import re
from collections import namedtuple, Counter

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
pmid = P(pmax.u // 2, pmax.v // 2)

def clamp(v, m):
    return v % m

after = list()
secs = 10000 # Will we find the tree before the historian pees himself?
snapshot = 0
safeties = list()
min_safety = len(robots) // 30
for sec in range(secs):
    buckets = Counter(clamp(r.p.u + sec * r.v.u, pmax.u) for r in robots)
    safety = max(buckets.values())

    if safety > min_safety: # Arbitrary filter
        safeties.append((safety, sec))

    # progress indicator:
    if not sec % 1000:
        print('.', end='', flush=True)

print()
print(safeties)

# Look at the best guesses first:
safeties = sorted(safeties, key=lambda t: t[0], reverse=True)
print(safeties)

for safety, sec in safeties:
    # Clean slate to paint in
    pic = [[' ' for v in range(pmax.v)] for u in range(pmax.u)]
    for r in robots:
        p = P(clamp(r.p.u + sec * r.v.u, pmax.u),
              clamp(r.p.v + sec * r.v.v, pmax.v))
        pic[p.u][p.v] = 'X'

    print()
    print()
    for v in range(pmax.v):
        for u in range(pmax.u):
            print(pic[u][v], end='')
        print()

    print()
    # Would be nice to be able to scroll back here?
    input(f"{safety=}  {sec=} {snapshot=} ")
    snapshot += 1

"""Spoiler: this still doesn't work well. It works well to point out
the gost images (example below), but there are over 50 frames that
have the same bucket-based safety factor.

                 XX X    X
                   X      X X          X    X        X        X                            X
                         X X                   X
           X     X                   X                                       X
  X              X         X   X          X      X  X
                              X   XX
  X           X         XX  X    X
  X                           X X              X         X                X
                               XX
                 X X       X     X  X          X                       X
                            X                  X           X
        X           X      X   X                                                        X
                                   XX
                 X          X  X   X       X
                          X         X                                        X
                           X    XXX            X                                X
                                 X X X        X
                        X       X  X     X                                   X
                          X    X    X             X
    X                                   X                               X                    X
                 X   X           X
                 X      X X  X X    X          X
          X                      X    X                                             X              X
                 X         X  XX              X                          X  X
                      X       XX  X                            X
       X             X          X    X                             X
                                 X           X                 X       X
                              X   X                                                 X
                                  X
                                    XX X                         X
               X           X X             X
                             X X  XX
                                    X X
                        XX           X  X                                    X                X
                 X          X   X     X        X       X
                       X            X  X                           X
                                 X   X X       X
                               X   X                                    X
                            X  X               X
                 X      X       X   X
                                    XX        XX
    X                   X X
       X                   X    XX
                 X           X X X           X X                       X               X      X  X
                              X  X X              X          X                            X
     X           X                       X     X

   X             X              X X   X        X
                 X          X       X                                     X
                                 X
     X           X                                                        X               X      X
                            X                                                               XX
                          X  X     X  X
                              X X                                                X
                 X                X   X
                 X         X    X              X
                                  X   X    X
                         X    X   X     X             X
            X                  XX    X
                 X         X           X          X
                 X   X  X                      X
                   X         X X      X  X  X                              X
                             XX   X
                 X           X  X XX
"""
