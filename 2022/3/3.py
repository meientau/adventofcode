#!/bin/python3

import fileinput


def calculateItemPriority(item):
    p = ord(item) - ord('a') + 1
    if p < 0:
        p += 32 + 26

    return p

total = 0
for rucksack in fileinput.input():
    rucksack = rucksack.strip()
    half = int(len(rucksack) / 2)
    compartmentLeft, compartmentRight = rucksack[:half], rucksack[half:]
    commonItem = sorted(set(compartmentLeft) & set(compartmentRight))[0]
    print(commonItem)
    itemPriority = calculateItemPriority(commonItem)
    total += itemPriority
    print(itemPriority)

print(total)
