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
    
    def __str__(self):
        return f"({self.u},{self.v})"

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

    def __repr__(self): return str(self)
    
    def __str__(self):
        return f"Field({self.crop}@{self.entry} a={self.area()} p={self.perimeter()})"
    

def find_all_fields(lines):
    all_fields = list()

    above = list()
    for v, line in enumerate(lines):
        here = list()
        for u, crop in enumerate(line.strip()):
            if crop == ' ': continue

            this_field = Field(u, v, crop)

            merge_left = here and here[-1].similar_to(this_field)
            merge_up = above and above[u].similar_to(this_field)
            if merge_left and merge_up:
                above_field = above[u]
                left_field = here[-1]
                above_field.merge(this_field)
                this_field = above_field
                above_field.merge(left_field)
                here = [this_field if f == left_field else f
                        for f in here]
                if above_field != left_field:
                    all_fields.remove(left_field)
            elif merge_left:
                here[-1].merge(this_field)
                this_field = here[-1]
            elif merge_up:
                above[u].merge(this_field)
                this_field = above[u]
            else:
                all_fields.append(this_field)
                
            here.append(this_field)
            
        above = here

    return all_fields

def total_value(fields):
    total = 0
    for field in fields:
        total += field.area() * field.perimeter()
    return total

if __name__ == "__main__":
    import fileinput
    fields = find_all_fields(list(fileinput.input()))
    total = total_value(fields)
    print(f"{total=}")

# total=1359028 0.124s