import main12a
import unittest
# This is the first day where I found I need a real unit test to get it right.

class Main12a_Test(unittest.TestCase):
    def test_single_field_exists(self):
        fields = main12a.find_all_fields(["a\n"])
        self.assertEqual(1, len(fields))

    def test_no_crop_no_field(self):
        fields = main12a.find_all_fields([" \n"])
        self.assertEqual(0, len(fields))

    def test_single_field_has_an_area(self):
        fields = main12a.find_all_fields(["a\n"])
        self.assertEqual(1, fields[0].area())

    def test_double_field_has_an_area(self):
        fields = main12a.find_all_fields(["aa\n"])
        self.assertEqual(1, len(fields))
        self.assertEqual(2, fields[0].area())

    def test_two_fields_do_not_merge(self):
        fields = main12a.find_all_fields(["aabbb\n"])
        self.assertEqual(2, len(fields))
        self.assertEqual(2, fields[0].area())
        self.assertEqual(3, fields[1].area())

    def test_single_field_has_a_perimeter(self):
        fields = main12a.find_all_fields(["a\n"])
        self.assertEqual(4, fields[0].perimeter())

    def test_double_field_has_a_perimeter(self):
        fields = main12a.find_all_fields(["aa\n"])
        self.assertEqual(6, fields[0].perimeter())

    def test_two_fields_do_not_merge(self):
        fields = main12a.find_all_fields(["aacaaa\n"])
        self.assertEqual(3, len(fields))
        self.assertEqual(2, fields[0].area())
        self.assertEqual(6, fields[0].perimeter())
        self.assertEqual(1, fields[1].area())
        self.assertEqual(4, fields[1].perimeter())
        self.assertEqual(3, fields[2].area())
        self.assertEqual(8, fields[2].perimeter())

    def test_fields_merge_vertically(self):
        fields = main12a.find_all_fields(["a\n", "a\n"])
        self.assertEqual(1, len(fields))
        self.assertEqual(2, fields[0].area())
        self.assertEqual(6, fields[0].perimeter())

    def test_fields_merge_vertically_and_horizontally(self):
        fields = main12a.find_all_fields(["aa\n", "aa\n"])
        self.assertEqual(1, len(fields))
        self.assertEqual(4, fields[0].area())
        self.assertEqual(8, fields[0].perimeter())

    def test_fields_merge_with_corners(self):
        fields = main12a.find_all_fields(["bba\n", "baa\n"])
        self.assertEqual(2, len(fields))
        self.assertEqual(3, fields[0].area())
        self.assertEqual(8, fields[0].perimeter())
        self.assertEqual(3, fields[1].area())
        self.assertEqual(8, fields[1].perimeter())

    def test_fields_merge_with_enclaves(self):
        fields = main12a.find_all_fields(["aaa\n", "aba\n", "aaa\n"])
        self.assertEqual(2, len(fields))
        self.assertEqual(8, fields[0].area())
        self.assertEqual(16, fields[0].perimeter())
        self.assertEqual(1, fields[1].area())

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
        fields = main12a.find_all_fields(land.split())
        self.assertEqual(11, len(fields))
        self.assertEqual(12, fields[0].area())
        self.assertEqual(18, fields[0].perimeter())
        self.assertEqual(4, fields[1].area())
        self.assertEqual(8, fields[1].perimeter())
        self.assertEqual(14, fields[2].area())
        self.assertEqual(28, fields[2].perimeter())
        self.assertEqual(10, fields[3].area())
        self.assertEqual(18, fields[3].perimeter())
        self.assertEqual(13, fields[4].area())
        self.assertEqual(20, fields[4].perimeter())
        self.assertEqual(11, fields[5].area())
        self.assertEqual(20, fields[5].perimeter())
        self.assertEqual(1, fields[6].area())
        self.assertEqual(4, fields[6].perimeter())
        self.assertEqual(13, fields[7].area())
        self.assertEqual(18, fields[7].perimeter())
        self.assertEqual(14, fields[8].area())
        self.assertEqual(22, fields[8].perimeter())
        self.assertEqual(5, fields[9].area())
        self.assertEqual(12, fields[9].perimeter())
        self.assertEqual(3, fields[10].area())
        self.assertEqual(8, fields[10].perimeter())
        self.assertEqual(1930, main12a.total_value(fields))
