import unittest

def is_nice_1(message):
    if any(pair in message for  pair in ["ab", "cd", "pq", "xy"]):
        return False
    
    if sum(1 for a in message if a in "aeiou") < 3:
        return False
    
    if not any(a == b for a, b in zip(message[:-1], message[1:])):
        return False

    return True


def is_nice_2(message):
    if not any(message.count(a+b) > 1 for a, b in zip(message[:-1], message[1:])):
        return False
    
    if not any(a == b for a, b in zip(message[:-2], message[2:])):
        return False

    return True


class NiceTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_nice_1("ugknbfddgicrmopn"))

    def test_2(self):
        self.assertTrue(is_nice_1("aaa"))

    def test_3(self):
        self.assertFalse(is_nice_1("jchzalrnumimnmhp"))

    def test_4(self):
        self.assertFalse(is_nice_1("haegwjzuvuyypxyu"))

    def test_5(self):
        self.assertFalse(is_nice_1("dvszwmarrgswjxmb"))

    def test_6(self):
        self.assertTrue(is_nice_2("qjhvhtzxzqqjkmpb"))

    def test_7(self):
        self.assertTrue(is_nice_2("xxyxx"))

    def test_8(self):
        self.assertFalse(is_nice_2("uurcxstgmygtbstg"))

    def test_9(self):
        self.assertFalse(is_nice_2("ieodomkazucvgmuy"))

    def test_10(self):
        message = "ieodomkazucvgmuy"
        self.assertEqual([], list((a+b) for a, b in zip(message[:-1], message[1:]) if message.count(a+b) >1))

        
if __name__ == "__main__":
    unittest.main()