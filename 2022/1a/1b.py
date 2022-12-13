#!/bin/python

import fileinput

sumcal=0
maxcal=list()
for line in fileinput.input():
    line = line.strip()
    if not line:
        maxcal = sorted(maxcal+[sumcal])
        if len(maxcal) > 3:
            maxcal = maxcal[-3:]
        sumcal = 0
        continue

    sumcal += int(line)
    continue

print(sum(maxcal))
