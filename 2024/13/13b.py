import fileinput
from collections import namedtuple
import re
from pprint import pprint
from sympy import Symbol
from sympy.solvers import solve

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
# Note: add empty line to end of input

re_num = re.compile(r"\d+")
Point = namedtuple("Point", ["x", "y"])
Machine = namedtuple("Machine", ["a", "b", "prize"])

def play(m):
    a, b = [Symbol(v, integer=True) for v in ['a', 'b']]
    presses = solve([a * m.a.x + b * m.b.x - m.prize.x,
                     a * m.a.y + b * m.b.y - m.prize.y],
                    [a, b])
    if not presses:
        return False

    return 3 * presses[a] + 1 * presses[b]

info = list()
machines = list()
tokens = 0
unfair_part_two_penalty = 10000000000000
for line in fileinput.input():
    line = line.strip()

    if not line:
        m = Machine(info[0], info[1],
                    Point(unfair_part_two_penalty+info[2].x,
                          unfair_part_two_penalty+info[2].y))
        machines.append(m)
        info.clear()

        cost = play(m)
        if cost:
            print(f"{m} wins for {cost} tokens")
            tokens += cost
        else:
            print(f"{m} cannot win")
        continue

    numbers = (int(n) for n in re_num.findall(line))
    info.append(Point(*numbers))

print(tokens)
# 79352015273424  3.878s
