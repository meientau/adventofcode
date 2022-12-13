#!/bin/python3

import fileinput

winloose = {
    'A X': 3,
    'B X': 0,
    'C X': 6,
    'A Y': 6,
    'B Y': 3,
    'C Y': 0,
    'A Z': 0,
    'B Z': 6,
    'C Z': 3,
}

total = 0
for line in fileinput.input():
    line = line.strip()
    op, me = line.split()
    op = ord(op) - ord('@')
    me = ord(me) - ord('W')

    score = me + winloose[line]
    print(score)
    total += score

print(total)
