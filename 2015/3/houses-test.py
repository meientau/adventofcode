import unittest

from houses import Houses

class HousesTest(unittest.TestCase):
    def test_one_step(self):
        '''> delivers presents to 2 houses: one at the starting location, and one to the east.'''
        h = Houses()
        h.run('>')
        self.assertEqual(2, h.how_many_houses())

    def test_square(self):
        '''^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.'''
        h = Houses()
        h.run('^>v<')
        self.assertEqual(4, h.how_many_houses())

    def test_flip_flop(self):
        '''^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.'''
        h = Houses()
        h.run('^v^v^v^v^v')
        self.assertEqual(2, h.how_many_houses())
