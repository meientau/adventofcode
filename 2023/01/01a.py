import fileinput
import re

numbers_re = re.compile("|".join([str(i) for i in range(1, 10)]))

sum = 0
for line in fileinput.input():
    matches = numbers_re.findall(line)
    a, b = matches[0], matches[-1]
    if fileinput.lineno() < 10:
        print(f"{a=} {b=} {line=}")
    sum += int(a + b)

print(f"{sum=}")
