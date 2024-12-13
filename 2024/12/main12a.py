from collections import namedtuple

class Point:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __add__(self, o):
        return Point(self.u + o.u, self.v + o.v)

    def __eq__(self, o):
        return self.u == o.u and self.v == o.v

    def __hash__(self):
        return 31 * self.u + self.v

directions = {Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)}

class Field:
    def __init__(self, u, v, crop):
        self.entry = Point(u, v)
        self.acres = set()
        self.acres.add(self.entry)
        self.crop = crop

    def area(self):
        return len(self.acres)

    def perimeter(self):
        return sum(1 for a in self.acres
                   for d in directions
                   if a+d not in self.acres)

    def similar_to(self, o):
        return self != o and self.crop == o.crop

    def merge(self, o):
        self.acres |= o.acres

def find_all_fields(lines):
    all_fields = list()

    above = list()
    for v, line in enumerate(lines):
        here = list()
        for u, crop in enumerate(line.strip()):
            if crop == ' ': continue

            this_field = Field(u, v, crop)

            if here and here[-1].similar_to(this_field):
                here[-1].merge(this_field)
                this_field = here[-1]
            elif above and above[u].similar_to(this_field):
                above[u].merge(this_field)
                this_field = above[u]
            else:
                all_fields.append(this_field)
                
            here.append(this_field)
            
        above = here

    return all_fields
