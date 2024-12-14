# Guess one: The tree fills the playfield and looks like a solid rectangle
# resting on one side, which fills the width of the playfield, and its
# tip touching the middle of the top of the playfield.

# +-----------+
# |.....x.....|
# |....xxx....|
# |...xxxxx...|
# |..xxxxxxx..|
# |.xxxxxxxxx.|
# |xxxxxxxxxxx|
# +-----------+

# Soooo ... How about rewriting the safety function to describe this?
# See `is_safe(p)` below.

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
pmid = P(pmax.u // 2, pmax.v // 2)

def is_safe(p):
    return abs(p.u - pmid.u) * 2 * pmax.v / pmax.u < p.v


def clamp(v, m):
    return v % m

after = list()
secs = 10000 # Will we find the tree before the historian pees himself?
max_safety = 0
snapshot = 0
for sec in range(secs):
    # Clean slate to paint in
    pic = [[' ' for v in range(pmax.v)] for u in range(pmax.u)]
    safety_sum = 0
    for r in robots:
        p = P(clamp(r.p.u + sec * r.v.u, pmax.u),
              clamp(r.p.v + sec * r.v.v, pmax.v))

        if is_safe(p):
            safety_sum += 1
            pic[p.u][p.v] = 'X'
        else:
            pic[p.u][p.v] = '.'

    max_safety = max(max_safety, safety_sum)

    # progress indicator:
    if not sec % 100:
        print(f"{max_safety}", end=' ', flush=True)

    # Print only somewhat-safe arrangements:
    if safety_sum * 20 / 19 > max_safety:
        print()
        print()
        for v in range(pmax.v):
            for u in range(pmax.u):
                print(pic[u][v], end='')
            print()

        print()
        # Would be nice to be able to scroll back here?
        input(f"{max_safety=}  {safety_sum=}  {sec=} {snapshot=} ")
        snapshot += 1

"""
7492 found on snapshot 27.

See how the easter egg *incidentally* falls mostly into my safety function ...



       .            .                                                                .
                                                                 X
                                        X                  X
                                      X                                   .         .         .  .

                        .         X
  .                                                        X
                 .............XXXXXXXXXXXXXXXXXX                            .
               . .                             X                                  .
                 .                             X                                          .
                 .                             X                            .
                 .                             X
                 .              X              X
                 .             XXX             X                        X  .
                 .            XXXXX            X
                 .           XXXXXXX           X
                 .          XXXXXXXXX          X              XX                    .
                 .            XXXXX            X                                   .
                 .           XXXXXXX           X                     X
                 .          XXXXXXXXX          X
                 .         XXXXXXXXXXX         X                    X               .
                 .        XXXXXXXXXXXXX        X                              .
                 .          XXXXXXXXX          X
     .           .         XXXXXXXXXXX         X                             X
                 .        XXXXXXXXXXXXX        X
                 .       XXXXXXXXXXXXXXX       X
          .      .      XXXXXXXXXXXXXXXXX      X                                    .
                 .        XXXXXXXXXXXXX        X
       .         .       XXXXXXXXXXXXXXX       X             X           X
                 .      XXXXXXXXXXXXXXXXX      X          X
                 .     XXXXXXXXXXXXXXXXXXX     X
                 .    XXXXXXXXXXXXXXXXXXXXX    X
                 .             XXX             X                                X    .
  .         .    .             XXX             X         X             X
                 X             XXX             X                        X                      .
                 X                             X                                      .
                 X                             X  X X                        X     X
                 X                             X                                                 . .
                 X                             X
                 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                                                                            X
                                                                                              .
               X                                                                  X
                                                                       X
  .                                X   X                                   X     X
 .              X X                  X


                                   X    X         X                                        .

.    .                  X
          X    X                X                    X

                     X

                                                                                       X

                                                              X

                                                    X          X
                       X                                                     X


                                                                                          X
                                       X

       X
                                                                                        X
                                        X                                 X                X

max_safety=380  safety_sum=380  sec=7492 snapshot=27
"""
