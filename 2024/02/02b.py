from fileinput import input
from itertools import pairwise

safes = [{-1, -2, -3}, {1, 2, 3}]

def is_safe(numbers):
    found = { b-a for a, b in pairwise(numbers) }
    safesteps = [found-safe for safe in safes]
    print(f"{numbers=} {found=} {safesteps=}")
    return not safesteps[0] or not safesteps[1]

def is_safe_enough(numbers):
    print(f"{numbers=}")
    if is_safe(numbers):
        return True

    for i in range(len(numbers)):
        clone = list(numbers)
        del clone[i]
        if is_safe(clone):
            return True

    return False

count = 0
for line in input():
    count += is_safe_enough([int(v) for v in line.split()])

print(count)
