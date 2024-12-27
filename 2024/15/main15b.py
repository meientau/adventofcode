import fileinput
from collections import namedtuple

Point = namedtuple("Point", ["u", "v"])
directions = {
    '^': Point(0, -1),
    'v': Point(0,  1),
    '>': Point( 1, 0),
    '<': Point(-1, 0),
}
things = dict()
classes = dict()


class Thing:
    def __init__(self, p, twin=None):
        things[p] = self
        self.position = p
        if twin:
            self.twin = True
            self.other = twin
        else:
            self.twin = False
            self.other = self.__class__(Point(p.u+1, p.v), twin=self)

    def getshowlabel(self):
        return self.__class__.label

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.label}-{self.position}"


class Space:
    label = '.'

    def __init__(self, p):
        return


class Wall(Thing):
    label = '#'

    def move_please(self, *_):
        return False

    def gps_coordinates(self):
        return 0


class Crate(Thing):
    label = 'O'
    showlabel = '[]'

    def move_please(self, direction, movers=None):
        if movers is None:
            movers = set()

        if self in movers:
            return movers

        movers.add(self)

        new_position = Point(self.position.u + direction.u,
                             self.position.v + direction.v)

        to_check = set()
        if new_position in things:
            to_check.add(things[new_position])

        if self.other:
            to_check.add(self.other)

        for other in to_check:
            ok = other.move_please(direction, movers)
            if ok is False: return False
            movers |= ok

        return movers
    
    # If I moved each thing one-by-one on the map, I would need to be careful
    # about order I move them so they don't erase each other.
    # It's easier to first collect all things that move, then remove them from the map,
    # then put them back on at the new position
    def jump(self):
        del things[self.position]

    def land(self, direction):
        new_position = Point(self.position.u + direction.u,
                             self.position.v + direction.v)
        things[new_position] = self
        self.position = new_position

    def gps_coordinates(self):
        if self.twin: # each box counts only once
            return 0

        return self.position.u + 100 * self.position.v

    def getshowlabel(self):
        return self.__class__.showlabel[self.twin]


robot = None
class Robot(Crate):
    label = '@'
    showlabel = label

    def __init__(self, p, *_):
        things[p] = self
        self.position = p
        self.twin = False
        self.other = None
        global robot
        robot = self

    def gps_coordinates(self):
        return 0

    def move_a_lot(self, line):
        for char in line:
            dir = directions[char]
            movers = self.move_please(dir)

            if not movers: continue

            for m in movers:
                m.jump()

            for m in movers:
                m.land(dir)



classes[Space.label] = Space
classes[Wall .label] = Wall
classes[Crate.label] = Crate
classes[Robot.label] = Robot


def read_line_into_field(v, line):
    for u, char in enumerate(line):
        p = Point(2*u, v)
        classes[char](p)

    global bottom_right
    bottom_right = Point(2*u+1, v)


def show_field():
    if len(things) < 200:
        for v in range(bottom_right.v+1):
            for u in range(bottom_right.u+1):
                p = Point(u, v)
                if p in things:
                    print(things[p].getshowlabel(), end='')
                else:
                    print(Space.label, end='')

            print()


robot_position = None
still_defining_field = True
for v, line in enumerate(fileinput.input()):
    line = line.strip()

    if not line and still_defining_field:
        still_defining_field = False
        show_field()
        continue

    if still_defining_field:
        read_line_into_field(v, line)
    else:
        robot.move_a_lot(line)

print()
show_field()
total = sum(thing.gps_coordinates() for thing in things.values())
print(f"{total=}")
# total=1386070   0.032s
