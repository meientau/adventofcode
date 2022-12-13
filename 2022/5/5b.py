#!/bin/python3

import sys

inp = sys.stdin.readlines()
crack = inp.index("\n")

print(len(inp))
print(crack)

stacks = inp[:crack-1]
stacklegend = inp[crack-1]
stacks.reverse()
moves = inp[crack+1:]

print(stacks[0])
print(stacks[-1])
print(moves[0])
print(moves[-1])
print()

stackpos = dict(((pos, istack) for pos, istack in zip(range(len(stacklegend)), stacklegend) if istack.strip()))
print(stackpos)

# fill stacks initially
stack = dict(((i, list()) for i in stackpos.values()))
for line in stacks:
    for pos, istack in stackpos.items():
        if pos >= len(line):
            continue

        crate = line[pos].strip()
        if crate:
            stack[istack].append(crate)

print(stack)

for line in moves:
    _, ncrates, _, ifrom, _, ito = line.split()
    print((ncrates, ifrom, ito))
    ncrates = int(ncrates)
    crates = stack[ifrom][-ncrates:]
    del stack[ifrom][-ncrates:]
    stack[ito] += crates

    print(stack)

toprow = [(s.pop() if s else ' ') for s in stack.values()]
print(''.join(toprow))
