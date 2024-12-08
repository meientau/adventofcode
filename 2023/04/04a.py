import fileinput
from collections import namedtuple
from pprint import pprint

class Game:
    next_game = 1
    def __init__(self, line):
        self.id = Game.next_game
        Game.next_game += 1
        head, rest = line.split(':')
        win, have = rest.split('|')
        self.win = separate(win)
        self.have = separate(have)

    def score(self):
        winning_numbers = len(self.win & self.have)
        if winning_numbers:
            return 2 ** (winning_numbers - 1)
        return 0

    def __str__(self):
        return f"Game {self.id}: {self.win=} {self.have=}"

    def __repr__(self):
        return str(self)

def separate(data):
    return set(int(v) for v in data.split())

games = list()
for line in fileinput.input():
    games.append(Game(line))

if len(games) < 10:
    pprint(games)

score = sum(g.score() for g in games)
print(f"{score=}")

# 18519 0.098s
