import fileinput
from collections import defaultdict
from pprint import pprint

class Game:
    next_game = 1
    games = dict()
    def __init__(self, line):
        self.id = Game.next_game
        Game.games[self.id] = self
        Game.next_game += 1
        head, rest = line.split(':')
        win, have = rest.split('|')
        self.win = separate(win)
        self.have = separate(have)
        self.score = len(self.win & self.have)

    def __str__(self):
        return f"Game {self.id}: {self.win=} {self.have=} {self.score=}"

    def __repr__(self):
        return str(self)

def separate(data):
    return set(int(v) for v in data.split())

cards = defaultdict(lambda: 1)

for line in fileinput.input():
    g = Game(line)
    cards[g.id]
    for win in range(g.id + 1, g.id + g.score + 1):
        cards[win] += cards[g.id]


if len(Game.games) < 10:
    pprint(Game.games)
    pprint(cards)

score = sum(cards.values())
print(f"{score=}")

# 11787590 0.081s
