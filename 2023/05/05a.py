import fileinput
from pprint import pprint

def separate(data):
    return list(map(int, data.split()))

def map_values(last, current, rules):
    dest, src, length = rules
    result = list()
    for value, default in zip(last, current):
        if value >= src and value < src+length:
            result.append(dest + value - src)
        else:
            result.append(default)

    return result

current = None
traces = list()
for line in fileinput.input():
    line = line.strip()
    if not line:
        continue

    if not current:
        current = separate(line.split(':')[1])
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
# 331445006 0.097s
