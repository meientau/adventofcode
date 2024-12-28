from collections import namedtuple, defaultdict
from pprint import pprint

Point = namedtuple("Point", "u v", defaults=[0, 0])
Point.__add__ = lambda self, o: Point(self.u + o.u, self.v + o.v)
Point.__sub__ = lambda self, o: Point(self.u - o.u, self.v - o.v)

Heading = namedtuple("Heading", "off sym axis")
headings = [
    Heading(Point( 1,  0), '>', 'x'),
    Heading(Point( 0,  1), 'v', 'y'),
    Heading(Point(-1,  0), '<', 'x'),
    Heading(Point( 0, -1), '^', 'y'),
]

class Hook:
    def __init__(self, p: Point, h: Heading):
        self.p = p
        self.h = h

    def __repr__(self):
        return f"{self.p}{self.h.sym}"

    def __str__(self):
        return repr(self)

    all = defaultdict(set)

    @classmethod
    def find_all(cls, spaces):
        for p in spaces:
            away = [heading for heading in headings
                    if p + heading.off in spaces]
            if len(away) > 2:
                for h in away:
                    cls.all[p].add(Hook(p, h))

    def __eq__(self, other):
        return self.p == other.p and self.h == other.h

    def __hash__(self):
        return 31*hash(self.p) + hash(self.h)


def show_path(path):
    points = dict((h.p, h) for h in path)
    for v in range(min(h.p.v for h in path), max(h.p.v for h in path)+1):
        for u in range(min(h.p.u for h in path), max(h.p.u for h in path)+1):
            p = Point(u,v)
            if p in points:
                print(points[p].h.sym, end='')
            else:
                print(' ', end='')
        print()


class Link:
    def __init__(self, fro: Hook, to: Hook, score: int):
        self.fro = fro
        self.to = to
        self.score = score

    def __repr__(self):
        return f"({self.fro} -> {self.to}@{self.score})"

    def __str__(self):
        return repr(self)

    all = set()

    @classmethod
    def find_all(cls, spaces):
        if cls.all:
            return

        Hook.find_all(spaces)

        collected = defaultdict(set)
        for hooks in Hook.all.values():
            for hook in hooks:
                collected[hook] = cls.follow_hook(hook)

        cls.all = dict(collected.items())

    @classmethod
    def follow_hook(cls, fro: Hook):
        score = 1
        here = Hook(fro.p + fro.h.off, fro.h)
        seen = {fro, here}
        while True:
            for heading in headings:
                p = here.p + heading.off
                if p in spaces and (heading == here.h or heading.axis != here.h.axis):
                    new_hook = Hook(p, heading)
                    break

            if new_hook.p in Hook.all:
                links = set()
                for to in Hook.all[new_hook.p]:
                    if to.h == here.h or to.h.axis != here.h.axis:
                        print(f"    adding {fro} --> {to}, last looked at {here}")
                        show_path(seen)
                        links.add(Link(fro, to, score + 1 + 1000 * int(here.h.axis != to.h.axis)))
                return links

            score += 1 + 1000 * int(here.h.axis != new_hook.h.axis)
            here = new_hook
            seen.add(here)

import unittest

spaces = {
    Point(1, 1),
    Point(2, 1),
    Point(3, 1),
    Point(4, 1),
    Point(5, 1),
    Point(1, 2),
    Point(3, 2),
    Point(5, 2),
    Point(1, 3),
    Point(2, 3),
    Point(3, 3),
    Point(4, 3),
    Point(5, 3),
}


class TestHook(unittest.TestCase):
    def test_find_hooks(self):
        Hook.find_all(spaces)
        self.assertEqual(2, len(Hook.all))
        for hooks in Hook.all.values():
            self.assertEqual(3, len(hooks))
        self.assertEqual(set('<^>'), set(hook.h.sym for hook in Hook.all[Point(3,3)]))


class TestLink(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        Link.find_all(spaces)

        print()
        print("after init:")
        pprint(Link.all)

    def test_find_links(self):
        Link.find_all(spaces)
        self.assertEqual(6, len(Link.all))

    def test_find_in_place_links(self):
        for links in Link.all.values():
            self.assertEqual(2, len(links))
        self.assertEqual({2006, 3006}, set(link.score for link in Link.all[Hook(Point(3,3), headings[0])]))
        self.assertNotIn(Hook(Point(3,3), headings[1]), Link.all)
        self.assertEqual({2006, 3006}, set(link.score for link in Link.all[Hook(Point(3,3), headings[2])]))
        self.assertEqual([1002, 1002], [link.score for link in Link.all[Hook(Point(3,3), headings[3])]])


if __name__ == "__main__":
    unittest.main()
