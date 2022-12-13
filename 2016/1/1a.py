#!/bin/python3

incr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
x = 0
y = 0
for i in input().strip().split(', '):
    print(i)
    turn = i[0]
    steps = int(i[1:])
    if turn == 'R':
        d += 1
    else:
        d -= 1

    d %= 4
    x += steps * incr[d][0]
    y += steps * incr[d][1]

print(abs(x) + abs(y))
