from PIL import Image, ImageDraw, ImageChops
from pprint import pprint
import fileinput
import re

mode = "L"
re_instruction = re.compile(r"(?P<op>turn on|turn off|toggle) ((?P<x0>\d+),(?P<y0>\d+)) through ((?P<x1>\d+),(?P<y1>\d+))(?: (?P<sum>\d+))?")

size = None
accu = None
draw = None

def read_instructions():
    global size, accu, draw
    for instruction in fileinput.input():
        if not size:
            size = tuple(map(int, instruction.split()))
            accu = Image.new(mode, size)
            draw = ImageDraw.Draw(accu)
            print(f"{size=}")
            continue

        m = re_instruction.match(instruction)
        if not m:
            print(f"Error in: {instruction=}")
            continue

        i = m.groupdict()
        x0, y0, x1, y1 = int(i['x0']), int(i['y0']), int(i['x1']), int(i['y1'])
        x0, x1 = min(x0, x1), max(x0, x1)
        y0, y1 = min(y0, y1), max(y0, y1)
        yield i['op'], (x0, y0, x1, y1), i['sum'] and int(i['sum'])

ops = {
    "turn on": 1,
    "turn off": -1,
    "toggle": 2,
}


if __name__ == "__main__":
    for op, area, expected in read_instructions():
        value = ops[op]
        mask = Image.new(mode, size)
        draw = ImageDraw.Draw(mask)
        draw.rectangle(area, fill=abs(value))
        if value > 0:
            accu = ImageChops.add(accu, mask)
        else:
            accu = ImageChops.subtract(accu, mask)

        if expected is not None:
            print(f"{expected} =? {sum(accu.getdata())} : {expected == sum(accu.getdata())}")

accu.save("part1.png")
totalsize = size[0] * size[1]
totalbrightness = 0
for y in range(size[1]):
    for x in range(size[0]):
        totalbrightness += accu.getpixel((x, y))

        if totalsize < 1000:
            print(f"{accu.getpixel((x, y)):3}", end="")

    if totalsize < 1000:
        print()

print(f"{totalsize=}")
print(f"{totalbrightness=}")

# 145349745
# real    0m0.118s


# size=(1000, 1000)
# totalsize=1000000
# totalpixels=569076 - too low
# real    0m0.487s
# Problem: getdata seems somehow compressed or whatever - after visiting each pixel individually, I got the correct data.

# correct:
# totalpixels=569999
# real    0m0.497s