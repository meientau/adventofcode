#!/bin/python3

import fileinput

cycle = 0
x = 1
rows = list()
row = ''

def checksignal(addpadding=False):
    global row, rows
    pix = '.'
    if abs(x - ((cycle-1) % 40)) < 2:
        pix = '#'

    row += pix

    if not (cycle % 40):
        print(row)
        rows.append(row)
        row = ''

    if addpadding:
        print(" "*10, end='')
    print(f"{cycle=:3} {x=:4}")

for line in fileinput.input():
    print(f"{line.strip():10}", end='')
    if line.startswith('noop'):
        cycle += 1
        checksignal()
    elif line.startswith('addx'):
        cycle += 1
        checksignal()
        cycle += 1
        checksignal(True)
        x += int(line.strip().split()[1])

print()
print('\n'.join(rows))
