from fileinput import input
from pprint import pprint
from collections import defaultdict
from itertools import chain

rules = defaultdict(list)
editions = list()
for line in input():
    if '|' in line:
        first, then = [int(p) for p in line.split('|')]
        rules[first].append(then)
    if ',' in line:
        editions.append([int(p) for p in line.split(',')])

if len(rules) < 100:
    pprint(rules)
    pprint(editions)

sum = 0
for update in editions:
    todo = dict([(f, [v for v in t if v in update]) for f, t in rules.items() if f in update])
    bad = list(chain(todo.values()))
    ok = True
    for page in update:
        if page in todo:
            del todo[page]
            bad = set(chain(*todo.values()))
            

        if page in bad:
            ok = False
            break

    element_to_use = len(update) // 2
    number = update[element_to_use]
    if len(rules) < 100:
        print(f"{ok=} {element_to_use=} {number=} {update=}")
    if ok:
        sum += number

print(sum)