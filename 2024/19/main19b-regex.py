import fileinput
import re
import functools

@functools.cache
def count_matches(line):
    if not line:
        return 1

    total = 0
    for prefix in available:
        if line.startswith(prefix):
            if len(available) < 20:
                print(f"line '{line}' starts with '{prefix}'")
            total += count_matches(line[len(prefix):])

    return total

available = None
possible = 0
for line in fileinput.input():
    line = line.strip()

    if not line:
        continue

    if not available:
        available = [t.strip(', ') for t in line.split()]
        available_re = re.compile('^('
                                  + '|'.join(available)
                                  + ')+$')
        continue

    if available_re.match(line):
        n = count_matches(line)
        if len(available) < 20:
            print(f"{n=} {line}")
        possible += n

print(possible)
# 752461716635602  0.814s
