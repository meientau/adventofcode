#!/bin/python

import sys
from pprint import pprint


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True

        if a > b:
            return False

        return None

    if isinstance(a, int):
        a = [a]
        return compare(a, b)

    if isinstance(b, int):
        b = [b]
        return compare(a, b)

    for a1, b1 in zip(a, b):
        result = compare(a1, b1)
        if result is not None:
            return result

    if len(a) < len(b):
        return True

    if len(a) > len(b):
        return False

    return None



class Item:
    def __init__(self, data):
        self.data = eval(data)
        self.r = data

    def __str__(self):
        return self.r

    def __repr__(self):
        return self.r

    def __lt__(self, other):
        return compare(self.data, other.data)



items = [Item(line.strip()) for line in sys.stdin.readlines() if line.strip()]
x, y = Item("[[2]]"), Item("[[6]]")
items += [x, y]

items = sorted(items)
if len(items) < 20:
    for item in items:
        pprint(item)

i = items.index(x) + 1
j = items.index(y) + 1
print(f"{i} * {j} = {i*j}")
