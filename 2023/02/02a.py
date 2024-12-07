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

    def possible(self):
        for draw in self.draws:
            for color, count in max_cubes.items():
                if draw[color] > count:
                    return False

        return True


sum = 0
for line in fileinput.input():
    g = Game(line)
    if g.possible():
        sum += g.id

print(f"{sum=}")
# sum=2545 0.052s
