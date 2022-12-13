#!/bin/python

import fileinput

sumcal=0
maxcal=0
for line in fileinput.input():
    line = line.strip()
    if not line:
        maxcal = max(sumcal, maxcal)
        sumcal = 0
        continue

    sumcal += int(line)
    continue

print(maxcal)
