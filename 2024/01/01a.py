import fileinput

all = [ line.split() for line in fileinput.input() ]
a = sorted([ int(column) for column, _ in all ])
b = sorted([ int(column) for _, column in all ])

sum = 0
for a, b in zip(a, b):
    diff = abs(b - a)
    if len(all) < 30:
        print(f"{a=} {b=} {diff=} {sum=}")
    sum += diff

print(sum)
