#!/bin/python3

import fileinput


def calculateItemPriority(item):
    p = ord(item) - ord('a') + 1
    if p < 0:
        p += 32 + 26

    return p

total = 0
rucksacks = [r.strip() for r in open("input").readlines()]

groups = int(len(rucksacks) / 3)

for group in range(groups):
    group_rucksacks = rucksacks[group*3:(group+1)*3]
    commonItems = set(group_rucksacks[0])
    for other_rucksack in group_rucksacks[1:]:
        commonItems &= set(other_rucksack)

    print(commonItems)
    commonItem = list(commonItems)[0]
    priority = calculateItemPriority(commonItem)
    print(priority)
    total += priority

print(total)
