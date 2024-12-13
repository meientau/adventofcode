import main12a
import unittest
# This is the first day where I found I need a real unit test to get it right.

class Main12a_Test(unittest.TestCase):
    def test_single_field_exists(self):
        fields = main12a.find_all_fields(["a\n"])
        self.assertEqual(1, len(fields))

    def test_single_field_has_an_area(self):
        fields = main12a.find_all_fields(["a\n"])
        self.assertEqual(1, fields[0].area())

    