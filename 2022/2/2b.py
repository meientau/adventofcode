#!/bin/python3

import fileinput

winloose = {
    'A X': 3,
    'B X': 1,
    'C X': 2,
    'A Y': 4,
    'B Y': 5,
    'C Y': 6,
    'A Z': 8,
    'B Z': 9,
    'C Z': 7,
}

total = 0
for line in fileinput.input():
    line = line.strip()
    print(winloose[line])
    total += winloose[line]

print(total)
