import fileinput
import re
import string
from collections import defaultdict

lines = [line.strip() for line in fileinput.input()]
width = len(lines[0]) + 1
buffer_line = '.' * width
text = buffer_line + '.'.join(lines) + buffer_line

if width < 20:
    print(text)

numbers_re = re.compile(r'\d+')

candidates = defaultdict(list)
gear = '*'
for match in numbers_re.finditer(text):
    start, end = match.span(0)
    start, end = start-1, end+1
    value = int(match.group(0))
    for base, chunk in enumerate([ text[start-width:end-width],
                                   text[start:end],
                                   text[start+width:end+width] ]):
        if gear in chunk:
            gear_pos = (base-1)*width + start + chunk.index(gear)
            candidates[gear_pos].append(int(match.group(0)))


if width < 20:
    print(candidates)

gears = [t for t in candidates.values() if len(t) == 2]
sum = sum(a*b for a, b in gears)
print(f"{sum=}")

# 467835 0.055s
# 75805607 0.051s
