#!/bin/python3

import re
import sys
import math


alldata = sys.stdin.read()


class Monkey:
    DEF = re.compile(r'Monkey\s+(?P<id>[0-9]):\n'
                     r'\s*Starting items: (?P<items>[0-9, ]+)\n'
                     r'\s*Operation: new = (?P<operation>[-old+*/0-9 ]+)\n'
                     r'\s*Test: divisible by (?P<test>[0-9]+)\n'
                     r'\s*If true: throw to monkey (?P<true_next>[0-9]+)\n'
                     r'\s*If false: throw to monkey (?P<false_next>[0-9]+)', re.S)

    monkeys = None

    def __init__(self, rows):
        match = Monkey.DEF.match(rows)
        if not match:
            print(repr(rows))
            raise

        self.__dict__.update(match.groupdict())
        self.items = list(map(int, self.items.strip().split(', ')))
        self.test = int(self.test)
        self.items_seen = 0

    @staticmethod
    def reset_all():
        Monkey.monkeys = [Monkey(rows) for rows in alldata.split('\n\n')]
        Monkey.globalmod = int(math.prod(m.test for m in Monkey.monkeys))
        Monkey.globalmaxitem = 0

    @staticmethod
    def inspect_all_monkeys():
        for monkey in Monkey.monkeys:
            monkey.inspect_all_items()

    @staticmethod
    def get_monkey_business():
        activity = sorted([m.items_seen for m in Monkey.monkeys], reverse=True)
        print(activity)
        return activity[0] * activity[1]


    def inspect_all_items(self):
        for item in list(self.items):
            self.inspect_one(item)

    def inspect_one(self, item):
        self.items_seen += 1
        new_item = eval(self.operation.replace('old', str(item))) % Monkey.globalmod
        Monkey.globalmaxitem = max(Monkey.globalmaxitem, new_item)
        self.items.remove(item)
        next_monkey = None
        if not new_item % self.test:
            next_monkey = self.true_next
        else:
            next_monkey = self.false_next

        Monkey.monkeys[int(next_monkey)].items.append(new_item)


Monkey.reset_all()
for i in range(1, 10001):
    Monkey.inspect_all_monkeys()
    if i == 1 or i == 20 or not i % 1000:
        print()
        print(f"business {Monkey.get_monkey_business()}, {Monkey.globalmaxitem=}")

print(Monkey.get_monkey_business())
