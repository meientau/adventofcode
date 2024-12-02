import fileinput
from collections import Counter

all = [ line.split() for line in fileinput.input() ]
a = [ int(column) for column, _ in all ]
b = Counter([ int(column) for _, column in all ])

sum = 0
for value in a:
    score = value * b[value]
    if len(all) < 30:
        print(f"{a=} {b=} {score=} {sum=}")
    sum += score

print(sum)
