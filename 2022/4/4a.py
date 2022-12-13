#!/bin/python3

import sys
import re

containingPairs = 0
for line in sys.stdin.readlines():
    a1, a2, b1, b2 = [int(x) for x in re.split('[-,]', line.strip())]
    overlap = a1 <= b1 and a2 >= b2 or a1 >= b1 and a2 <= b2
    # print((a1, a2, b1, b2, overlap))
    if overlap: containingPairs += 1


print(containingPairs)
