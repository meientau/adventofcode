from fileinput import input

safes = [{-1, -2, -3}, {1, 2, 3}]

count = 0
for line in input():
    line = [int(v) for v in line.split()]
    found = { b-a for a, b in zip(line, line[1:]) }
    safesteps = [found-safe for safe in safes]
    print(f"{found=} {safesteps=}")
    if not safesteps[0] or not safesteps[1]:
        count += 1

print(count)
if count in {2, 660}:
    print("OK")
