#!/bin/python3

incr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def do_everything():
    d = 0
    x = 0
    y = 0
    seen = set()
    for i in input().strip().split(', '):
        print(i)
        turn = i[0]
        steps = int(i[1:])
        if turn == 'R':
            d += 1
        else:
            d -= 1

        d %= 4
        for _ in range(steps):
            x += incr[d][0]
            y += incr[d][1]
            if (x, y) in seen:
                return x, y

            seen.add((x, y))

    return x, y

x, y = do_everything()
print(abs(x) + abs(y))
