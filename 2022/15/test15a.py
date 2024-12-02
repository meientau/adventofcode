#!/bin/python3

import unittest

import main15a

class SensorTest(unittest.TestCase):
    def testImport(self):
        s = main15a.Sensor("Sensor at x=2, y=18: closest beacon is at x=-2, y=15")

        self.assertEqual(2, s.p.x)
        self.assertEqual(18, s.p.y)
        self.assertEqual(-2, s.b.x)
        self.assertEqual(15, s.b.y)
        self.assertEqual(7, s.d)

    def testPaint(self):
        field = main15a.Field()
        field.add(main15a.Sensor("Sensor at x=3, y=3: closest beacon is at x=-1, y=1"))

        self.assertEqual(
"""
...............
.........#.....
........###....
.......#####...
......#######..
.....B########.
....###########
...######S#####
....###########
.....#########.
......#######..
.......#####...
........###....
""".strip(), field.paint().strip())

    def testCountRow(self):
        with open("input_small") as rows:
            field = main15a.Field(rows.readlines())
            self.assertEqual(26, field.countRow(10))


unittest.main()
