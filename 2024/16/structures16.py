from collections import namedtuple, defaultdict

Point = namedtuple("Point", "u v", defaults=[0, 0])
Point.__add__ = lambda self, o: Point(self.u + o.u, self.v + o.v)
Point.__sub__ = lambda self, o: Point(self.u - o.u, self.v - o.v)


headings = [Point( 1,  0), Point( 0, -1), Point(-1,  0), Point( 0,  1)]
headingsymbols = '>^<v'
axes = 'xyxy'

class Move:
    def __init__(self, p, h):
        self.p = p
        self.h = h

    def leads_to(self, p):
        v = p - self.p
        if v.u and v.v:  # diagonal
            return False

        off = headings[self.h]
        return v.u*off.u > 0 or v.v*off.v > 0

    def __repr__(self):
        return f"{self.p}{headingsymbols[self.h]}"

    def __str__(self):
        return repr(self)


class Link:
    def __init__(self, fro, to):
        self.fro = fro
        self.to = to
        v = to.p - fro.p
        steps = abs(v.u + v.v)
        turns = to.h != fro.h
        self.score = steps + 1000 * turns

    def __repr__(self):
        return f"({self.fro}->{self.to}@{self.score})"

    def __str__(self):
        return repr(self)


class Candidate:
    def __init__(self, link):
        self.links = list()
        self.score = 0
        self.add_link(link)

    def add_link(self, link):
        self.links.append(link)
        self.score += link.score

    def __repr__(self):
        return f"({self.links[0].fro} -> {self.links[-1].to} @{self.score})"

    def __str__(self):
        return repr(self)


import unittest

class TestMove(unittest.TestCase):
    def test_leads_to_simple(self):
        a = Point(1, 1)
        b = Point(3, 1)
        h = 0
        ma = Move(a, h)
        self.assertTrue(ma.leads_to(b))


class TestLink(unittest.TestCase):
    def test_score_one(self):
        link = Link(Move(Point(1, 1), 0), Move(Point(2, 1), 0))
        self.assertEqual(link.score, 1)

    def test_score_two(self):
        link = Link(Move(Point(1, 1), 3), Move(Point(1, 3), 3))
        self.assertEqual(link.score, 2)

    def test_score_one_thousand_five(self):
        link = Link(Move(Point(1, 1), 0), Move(Point(6, 1), 1))
        self.assertEqual(link.score, 1005)

    def test_score_one_thousand_six(self):
        link = Link(Move(Point(1, 7), 1), Move(Point(1, 1), 2))
        self.assertEqual(link.score, 1006)

    def test_score_one_thousand_seven(self):
        link = Link(Move(Point(1, 8), 2), Move(Point(1, 1), 1))
        self.assertEqual(link.score, 1007)

    def test_score_one_thousand_eight(self):
        link = Link(Move(Point(1, 9), 3), Move(Point(1, 1), 0))
        self.assertEqual(link.score, 1008)


class TestCandidate(unittest.TestCase):
    def test_single(self):
        link = Link(Move(Point(1, 9), 3), Move(Point(1, 1), 0))
        candidate = Candidate(link)
        self.assertEqual(candidate.score, 1008)

    def test_double(self):
        link1 = Link(Move(Point(1, 9), 3), Move(Point(1, 1), 0))
        link2 = Link(Move(Point(1, 1), 0), Move(Point(6, 1), 1))

        candidate = Candidate(link1)
        candidate.add_link(link2)

        self.assertEqual(candidate.score, 2013)



if __name__ == "__main__":
    unittest.main()
