from collections import namedtuple

Point = namedtuple("Point", ["u", "v"])

class Field:
    def __init__(self, u, v, crop):
        self.entry = Point(u, v)
        self.acres = set()
        self.acres.add(self.entry)
        self.crop = crop
        
    def area(self):
        return len(self.acres)
    
    def perimeter(self):
        return 4
    
    def similar_to(self, o):
        return self != o and self.crop == o.crop
    
    def merge(self, o):
        self.acres |= o.acres

def find_all_fields(lines):
    all_fields = list()
    for v, line in enumerate(lines):
        last_field = None
        
        for u, crop in enumerate(line.strip()):
            this_field = Field(u, v, crop)
            
            if last_field and last_field.similar_to(this_field):
                last_field.merge(this_field)
                this_field = last_field
            else:
                all_fields.append(this_field)
                
            last_field = this_field
            
    return all_fields
