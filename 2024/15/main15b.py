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
            self.other = self.__class__(Point(p.u+1, p.v), twin=True)

    def getshowlabel(self):
        return self.__class__.label


class Space:
    label = '.'

    def __init__(self, p):
        return


class Wall(Thing):
    label = '#'

    def move_please(self, direction):
        return False

    def gps_coordinates(self):
        return 0


class Crate(Thing):
    label = 'O'
    showlabel = '[]'

    def move_please(self, direction):
        new_position = Point(self.position.u + direction.u,
                             self.position.v + direction.v,)

        if new_position in things:
            neighbour = things[new_position]
            ok = neighbour.move_please(direction)
        else:
            ok = True

        if ok:
            del things[self.position]
            things[new_position] = self
            self.position = new_position
            return True

        return False

    def gps_coordinates(self):
        return self.position.u + 100 * self.position.v

    def getshowlabel(self):
        return self.__class__.showlabel[self.twin]


robot = None
class Robot(Crate):
    label = '@'

    def __init__(self, p, twin=False):
        Crate.__init__(self, p, twin=True)
        global robot
        robot = self

    def gps_coordinates(self):
        return 0


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


def move_robot(line):
    for char in line:
        robot.move_please(directions[char])


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
        move_robot(line)

print()
show_field()
total = sum(thing.gps_coordinates() for thing in things.values())
print(f"{total=}")
# total=1414416  0.082s
