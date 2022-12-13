#!/bin/python3

import fileinput


cycle = 0
x = 1
totalstrength = 0

def checkstrength(addpadding=False):
    global totalstrength
    strength = -1
    if not ((cycle + 20) % 40):
        strength = cycle * x
        totalstrength += strength

    if addpadding:
        print(" "*10, end='')
    print(f"{cycle=:3} {x=:4} {strength=:4}")

for line in fileinput.input():
    print(f"{line.strip():10}", end='')
    if line.startswith('noop'):
        cycle += 1
        checkstrength()
    elif line.startswith('addx'):
        cycle += 1
        checkstrength()
        cycle += 1
        checkstrength(True)
        x += int(line.strip().split()[1])

print(f"{totalstrength=}")
