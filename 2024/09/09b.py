import fileinput
from collections import namedtuple
from itertools import batched
from pprint import pprint

empty_id = '.'

class File:
    def __init__(self, id, size, start):
        self.id = id
        self.size = size
        self.start = start

    def value(self):
        if self.id == empty_id:
            return 0

        return sum(int(self.id) * b
                   for b in range(self.start, self.start + self.size))

    def __str__(self):
        return f"({self.id}: {self.start}+{self.size} {self.value()})"

    def __repr__(self): return str(self)


diskspec = [int(c) for c in next(fileinput.input()).strip()]
diskspec.append(0)

if len(diskspec) < 50:
    print(f"{diskspec=}")

files = list()
holes = list()
file_id = 0
head = 0
for file_chunk, empty_chunk in batched(diskspec, 2):
    f = File(str(file_id), file_chunk, head)
    head += file_chunk
    e = File(empty_id, empty_chunk, head)
    head += empty_chunk
    files.insert(0, f)
    holes.append(e)
    file_id += 1

if len(diskspec) < 50:
    pprint(files)
    pprint(holes)
    print()

def move(f, h):
    f.start = h.start
    h.start += f.size
    h.size -= f.size


for f in files:
    for h in holes:
        if h.start > f.start:
            break

        if h.size >= f.size:
            move(f, h)
            break



if len(diskspec) < 50:
    print("after defrag:")
    pprint(files)
    pprint(holes)
    print()

cksum = sum(f.value() for f in files)

print(f"{cksum=}")
# cksum=6620961903358 too high
# cksum=8515929533392  6.484s
# cksum=6360363199987  3.864s
