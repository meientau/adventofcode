#!/bin/python3

import fileinput
import re
from collections import defaultdict
from pathlib import Path

root = Path('/')
cwd = Path('/')
sizes = dict()
dirs = set(['/'])
vi = open('visited.log', 'w')
for line in fileinput.input():
    if line.startswith('$ ls'):
        continue

    if line.startswith('$ cd'):
        arg = line.split()[2].strip()
        newcwdu = cwd / arg
        newcwd = newcwdu.resolve()

        print(f"u {newcwdu}", file=vi)
        print(f"r {newcwd}", file=vi)
        if str(newcwd) not in dirs:
            print(f"ouch 2: '{line.strip()}' - {newcwd} doesn't exist")
        cwd = newcwd
        #print(f"# {cwd}")
        continue

    if line.startswith('dir '):
        arg = line.split()[1].strip()
        dirs.add(str((cwd / arg).resolve()))
        continue

    if not re.match(r'^[0-9]+ \S+$', line):
        print(f"ouch 1: '{line}'")

    size, name = line.split()
    size = int(size)

    f = str(cwd / name)
    #sizes.append((f, size))
    sizes[f] = size
    #print(f"# {size:15} {f}")
    for d in dirs:
        if d == '/': continue
        if f.startswith(d) and f[len(d)] != '/':
            print(f"ouch 3: '{f}' is not uniq prefix with '{d}'")

sumsmall = 0
alltotals = defaultdict(list)
with open('alltotals.txt', 'w') as out:
    for d in sorted(dirs):
        totalsize = sum(s for f, s in sizes.items() if f.startswith(d) and (d=='/' or f[len(d)] == '/'))
        print(f"{totalsize:15} {d}", file=out)
        alltotals[totalsize].append(d)

totalused = sum((s for f, s in sizes.items()))
print(max(alltotals.keys()))
print(alltotals)
print(totalused)

totalspace = 70000000
freespace = totalspace - totalused
print(freespace)
needspace = 30000000
needtofree = needspace - freespace
bestmatch = min((s for s, dirs in alltotals.items() if s > needtofree))

print(list(s for s, dirs in alltotals.items() if s > needtofree))

print(bestmatch)

print()
