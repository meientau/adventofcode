#!/bin/python3

import re
import sys
import unittest


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
        print(self.__dict__)
        self.items_seen = 0

    @staticmethod
    def reset_all():
        Monkey.monkeys = [Monkey(rows) for rows in alldata.split('\n\n')]

    @staticmethod
    def inspect_all_monkeys():
        for monkey in Monkey.monkeys:
            monkey.inspect_all_items()

    @staticmethod
    def get_monkey_business():
        activity = sorted([m.items_seen for m in Monkey.monkeys], reverse=True)
        return activity[0] * activity[1]


    def inspect_all_items(self):
        for item in list(self.items):
            self.inspect_one(item)

    def inspect_one(self, item):
        self.items_seen += 1
        new_item = eval(self.operation.replace('old', str(item)))
        new_item //= 3
        print(f"before {self.id=:2} {self.items=}")
        self.items.remove(item)
        next_monkey = None
        if not new_item % self.test:
            next_monkey = self.true_next
        else:
            next_monkey = self.false_next

        Monkey.monkeys[int(next_monkey)].items.append(new_item)
        print(f"after  {self.id=:2}{self.items=}")
        print(f"       {next_monkey=:2} {new_item}")

class MonkeyTest(unittest.TestCase):
    def setUp(self):
        Monkey.reset_all()

    def test_inspect_one_zero(self):
        m0 = Monkey.monkeys[0]
        m3 = Monkey.monkeys[3]
        self.assertEquals(m0.id, '0')
        self.assertEquals(m3.id, '3')
        m0.inspect_one(79)
        self.assertEquals([98], m0.items)
        self.assertEquals([74, 500], m3.items)

    def test_inspect_round_one(self):
        Monkey.inspect_all_monkeys()
        self.assertEquals([20, 23, 27, 26], Monkey.monkeys[0].items)
        self.assertEquals([2080, 25, 167, 207, 401, 1046], Monkey.monkeys[1].items)
        self.assertEquals([], Monkey.monkeys[2].items)
        self.assertEquals([], Monkey.monkeys[3].items)

    def test_inspect_twenty_rounds(self):
        for i in range(20):
            Monkey.inspect_all_monkeys()
        self.assertEquals([10, 12, 14, 26, 34], Monkey.monkeys[0].items)
        self.assertEquals([245, 93, 53, 199, 115], Monkey.monkeys[1].items)
        self.assertEquals([], Monkey.monkeys[2].items)
        self.assertEquals([], Monkey.monkeys[3].items)

        self.assertEquals(101, Monkey.monkeys[0].items_seen)
        self.assertEquals(95, Monkey.monkeys[1].items_seen)
        self.assertEquals(7, Monkey.monkeys[2].items_seen)
        self.assertEquals(105, Monkey.monkeys[3].items_seen)

        self.assertEquals(10605, Monkey.get_monkey_business())



#unittest.main()

Monkey.reset_all()
for i in range(20):
    Monkey.inspect_all_monkeys()
print(Monkey.get_monkey_business())
