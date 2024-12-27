import fileinput
from itertools import batched # since python 3.12
from pprint import pprint

def separate(data):
    return list(map(int, data.split()))

def map_values(last, current, rules):
    result = list()
    for r in rules:
        for s in last:
            if r[0]

    return result

current = None
traces = list()
for line in fileinput.input():
    line = line.strip()
    if not line:
        continue

    if not current:
        ranges = separate(line.split(':')[1])
        current = list()
        for start, end in batched(ranges, 2):
            current += range(start, start + end)
        continue

    if ':' in line:
        traces.append(current)
        last = current
        continue

    rules = separate(line)
    current = map_values(last, current, rules)

traces.append(current)
if len(current) < 10:
    pprint(traces)
print(min(traces[-1]))
