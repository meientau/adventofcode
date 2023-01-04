#!/bin/python

import sys
from pprint import pprint


def compare(a, b, i=""):
    print(f"{i}- Compare {str(a).replace(' ','')} vs {str(b).replace(' ','')}")

    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            print(f"{i}  - Right side is smaller, so inputs are not in the right order")
            return False

        if a < b:
            print(f"{i}  - Left side is smaller, so inputs are in the right order")
            return True

        return None

    if isinstance(a, int):
        a = [a]
        print(f"{i}  - Mixed types; convert left to {a} and retry comparison")
        return compare(a, b, i+"  ")

    if isinstance(b, int):
        b = [b]
        print(f"{i}  - Mixed types; convert right to {b} and retry comparison")
        return compare(a, b, i+"  ")

    for a1, b1 in zip(a, b):
        result = compare(a1, b1, i+"  ")
        if result is not None:
            return result

    if len(a) < len(b):
        print(f"{i}  - Left side ran out of items, so inputs are in the right order")
        return True

    if len(a) > len(b):
        print(f"{i}  - Right side ran out of items, so inputs are not in the right order")
        return False


    return None



pairs = [list(eval(item) for item in pair.split('\n') if item) for pair in sys.stdin.read().split('\n\n') if pair]

if len(pairs) < 20:
    pprint(pairs)

total = 0
for i, pair in enumerate(pairs, 1):
    a, b = pair
    print()
    print(f"== Pair {i} ==")
    if compare(a, b) is True:
        total += i

print(total)
