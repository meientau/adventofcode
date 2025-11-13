from hashlib import md5
import unittest


def mine_coin(seed, nzeros=5):
    for answer in range(10_000_000):
        coin = md5(f"{seed}{answer}".encode()).hexdigest()
        if coin.startswith("0" * nzeros):
            return answer


class AdventCoinTest(unittest.TestCase):
    def test_md5(self):
        self.assertEqual("000001dbbfa3a5c83a2d506429c7b00e", md5("abcdef609043".encode()).hexdigest())

    def test_a(self):
        self.assertEqual(609043, mine_coin("abcdef"))

    def test_b(self):
        self.assertEqual(1048970, mine_coin("pqrstuv"))

    def test_mine(self):
        self.assertEqual(346386, mine_coin("iwrupvqb"))


if __name__ == "__main__":
    unittest.main()