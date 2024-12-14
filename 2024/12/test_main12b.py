import main12b
import unittest
# This is the first day where I found I need a real unit test to get it right.

class Main12b_Test(unittest.TestCase):
    def test_two_fields_do_not_merge(self):
        fields = main12b.find_all_fields(["aabbb\n"])
        self.assertEqual(2, len(fields))
        self.assertEqual(2, fields[0].area())
        self.assertEqual(4, fields[0].perimeter())
        self.assertEqual(3, fields[1].area())
        self.assertEqual(4, fields[1].perimeter())

    def test_hole_in_a_field(self):
        fields = main12b.find_all_fields(["aaa\n", "aba\n", "aaa\n"])
        self.assertEqual(2, len(fields))
        self.assertEqual(8, fields[0].area())
        self.assertEqual(8, fields[0].perimeter())
        self.assertEqual(1, fields[1].area())
        self.assertEqual(4, fields[1].perimeter())

    def test_all_four_corners(self):
        fields = main12b.find_all_fields(["aabb\n", "axxb\n", "cxxd\n", "ccdd\n"])
        self.assertEqual(5, len(fields))
        self.assertEqual(3, fields[0].area())
        self.assertEqual(6, fields[0].perimeter())
        self.assertEqual(3, fields[1].area())
        self.assertEqual(6, fields[1].perimeter())
        self.assertEqual(4, fields[2].area())
        self.assertEqual(4, fields[2].perimeter())
        self.assertEqual(3, fields[3].area())
        self.assertEqual(6, fields[3].perimeter())
        self.assertEqual(3, fields[4].area())
        self.assertEqual(6, fields[4].perimeter())

    def test_all_horseshoe(self):
        fields = main12b.find_all_fields(["aaa\n", "abb\n", "aaa\n"])
        self.assertEqual(2, len(fields))
        self.assertEqual(7, fields[0].area())
        self.assertEqual(8, fields[0].perimeter())
        self.assertEqual(2, fields[1].area())
        self.assertEqual(4, fields[1].perimeter())

    def test_sample_input(self):
        land = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
        fields = main12b.find_all_fields(land.split())
        self.assertEqual(11, len(fields))
        self.assertEqual(12, fields[0].area())
        self.assertEqual(10, fields[0].perimeter())
        self.assertEqual(4, fields[1].area())
        self.assertEqual(4, fields[1].perimeter())
        self.assertEqual(14, fields[2].area())
        self.assertEqual(22, fields[2].perimeter())
        self.assertEqual(10, fields[3].area())
        self.assertEqual(12, fields[3].perimeter())
        self.assertEqual(13, fields[4].area())
        self.assertEqual(10, fields[4].perimeter())
        self.assertEqual(11, fields[5].area())
        self.assertEqual(12, fields[5].perimeter())
        self.assertEqual(1, fields[6].area())
        self.assertEqual(4, fields[6].perimeter())
        self.assertEqual(13, fields[7].area())
        self.assertEqual(8, fields[7].perimeter())
        self.assertEqual(14, fields[8].area())
        self.assertEqual(16, fields[8].perimeter())
        self.assertEqual(5, fields[9].area())
        self.assertEqual(6, fields[9].perimeter())
        self.assertEqual(3, fields[10].area())
        self.assertEqual(6, fields[10].perimeter())
        self.assertEqual(1206, main12b.total_value(fields))
