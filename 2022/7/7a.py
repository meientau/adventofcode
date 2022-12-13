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

print(len(sizes))
print(len(dirs))
print('/qmfvph/ttltfz/ttltfz/hzqlb/jshj/hzqlb/zhq' in dirs)
print('\n'.join([p for p in dirs if 'zhq' in p]))

print()
sumsmall = 0
with open('alltotals.txt', 'w') as out:
    for d in sorted(dirs):
        totalsize = sum(s for f, s in sizes.items() if f.startswith(d) and f[len(d)] == '/')
        marker = ' '
        if totalsize <= 100000:
            sumsmall += totalsize
            marker = '%'
        print(f"{marker}  {totalsize:15} {d}", file=out)
        for f, s in sizes.items():
            if f.startswith(d):
                print(f"{marker}- {s:15}  {f}", file=out)


print()

print(sumsmall)


# too low:   1451199
#            2311417
# too high: 48381165
# google:    1989474


# - number of files in input equals number of files here
#
# - do the seen sizes match? yes
#
#     grep -o '^[0-9]\+' input |sort -n > allsizes-input.txt
#     diff allsizes*
#
# - number of directories in input is smaller than seen here, that
#   seems to be because directory names are repeated in different
#   places. Anyway: it's bigger here.
#
# - path following and resolving matches my understanding.
