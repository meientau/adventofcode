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


def fix(update):
    todo = dict([(f, [v for v in t if v in update]) for f, t in rules.items() if f in update])
    while True:
        ok = True
        for first_n, thens in todo.items():
            for then_n in thens:
                fi = update.index(first_n)
                ti = update.index(then_n)
                if fi < ti:
                    continue

                ok = False
                update.remove(first_n)
                update.insert(ti, first_n)

        if ok:
            break

oksum = 0
fixedsum = 0
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

    if not ok:
        fix(update)

    element_to_use = len(update) // 2
    number = update[element_to_use]

    if ok:
        oksum += number
    else:
        fixedsum += number

    if len(rules) < 100:
        print(f"{ok=} {element_to_use=} {number=} {update=}")



print(f"{oksum=} {fixedsum=}")

# oksum=4689 fixedsum=6336
# real    0m0.045s