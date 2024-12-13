from collections import namedtuple

Point = namedtuple("Point", ["u", "v"])

class Field:
    def __init__(self, u, v, crop):
        self.entry = Point(u, v)
        self.crop = crop
        
    def area(self):
        return 1

def find_all_fields(lines):
    all_fields = list()
    for v, line in enumerate(lines):
        for u, crop in enumerate(line.strip()):
            all_fields.append(Field(u, v, crop))
            
    return all_fields
