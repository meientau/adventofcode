import unittest
import re

numbers = {
    '1': 1, 'one': 1,
    '2': 2, 'two': 2,
    '3': 3, 'three': 3,
    '4': 4, 'four': 4,
    '5': 5, 'five': 5,
    '6': 6, 'six': 6,
    '7': 7, 'seven': 7,
    '8': 8, 'eight': 8,
    '9': 9, 'nine': 9,
}

numbers_re = re.compile("|".join(numbers))

def calc_line(line):
    matches = [m.group(0) for m in [numbers_re.match(line[i:])
                                    for i in range(len(line)-1)]
               if m]
    a, b = matches[0], matches[-1]
    a, b = numbers[a], numbers[b]

    return 10*a + b

class RulesTest(unittest.TestCase):
    def test_(self):
        self.assertEqual(29, calc_line("two1nine"))

    def test_eightwothree(self):
        self.assertEqual(83, calc_line("eightwothree     "))

    def test_abcone2threexyz(self):
        self.assertEqual(13, calc_line("abcone2threexyz  "))

    def test_xtwone3four(self):
        self.assertEqual(24, calc_line("xtwone3four      "))

    def test_4nineeightseven2(self):
        self.assertEqual(42, calc_line("4nineeightseven2 "))

    def test_zoneight234(self):
        self.assertEqual(14, calc_line("zoneight234      "))

    def test_7pqrstsixteen(self):
        self.assertEqual(76, calc_line("7pqrstsixteen    "))

    def test_vpjthc6(self):
        self.assertEqual(66, calc_line("vpjthc6          "))

    def test_sevenine(self):
        self.assertEqual(79, calc_line("sevenine         "))

    def test_eighthree(self):
        self.assertEqual(83, calc_line("eighthree"))



# What I missed, rsp. thought I missed:
# - overlapping matches count. re.findall() doesn't work.
# - if there is only one number, it is the first *and* last number.
# After nothing worked, I first came across the second problem and made
# a wrong change. On reddit I found the first tip.   Then it still failed,
# and it took me some time to figure out the second rule.

if __name__ == "__main__":
    unittest.main()
