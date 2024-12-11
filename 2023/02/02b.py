import fileinput
from collections import defaultdict

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

class Game:
    def __init__(self, spec):
        game_spec, draws_spec = spec.split(":")
        self.id = int(game_spec.strip("Game :"))
        self.draws = list()
        for draw_spec in draws_spec.split(";"):
            self.add_draw(draw_spec)

    def add_draw(self, spec):
        draw = defaultdict(int)
        for sample in spec.split(','):
            count, color = sample.strip().split()
            draw[color] = int(count)

        self.draws.append(draw)

    def power(self):
        power = 1
        for pick_color in max_cubes:
            power *= max([draw[pick_color] for draw in self.draws])
        if self.id < 10:
            print(f"{self.id=} {power=}")
        return power


sum = 0
for line in fileinput.input():
    g = Game(line)
    sum += g.power()

print(f"{sum=}")
# sum=78111 0.052s
