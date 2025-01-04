import fileinput
import re


available = None
possible = 0
for line in fileinput.input():
    line = line.strip()

    if not line:
        continue

    if not available:
        available = re.compile('^('
                               + '|'.join([t.strip(', ') for t in line.split()])
                               + ')+$')
        continue

    n = int(bool(available.match(line)))
    print(f"{n=} {line}")
    possible += n

print(possible)
# 265 0.096s
