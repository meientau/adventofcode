import fileinput
from collections import namedtuple
from pprint import pprint

Game = namedtuple("Game", ["win", "have"])

def separate(data):
    return [int(v) for v in data.split()]

games = list()
for line in fileinput.input():
    head, rest = line.split(':')
    win, have = rest.split('|')
    win = separate(win)
    have = separate(have)
    games.append(Game(win, have))


if len(games) < 10:
    pprint(games)
