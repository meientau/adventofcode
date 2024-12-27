import fileinput
import itertools

keys = set()
locks = set()
current = 0
this_is = None
for line in fileinput.input():
    line = line.strip()
    if not line:
        if current:
            this_is.add(current)
        current = 0
        this_is = None
        continue

    if this_is is None:
        if line == '#####':
            this_is = locks
        else:
            this_is = keys
        continue

    for c in line:
        bit = int(c=='#')
        current = (current << 1) + bit

if len(keys) < 10:
    print()
    print("keys:")
    for c in keys:
        print(f"{c:09d}")


    print()
    print("locks:")
    for c in locks:
        print(f"{c:09d}")

    print()

def to_pins(v):
    pins = f"{v:030b}".replace('0', '.').replace('1', '#')
    return [''.join(s) for s in itertools.batched(pins, 5)]

def show_schematic(key, lock):
    print("  key   lock  k&l")
    print(f"  ..... ##### .....   {'' if (key&lock) else 'OK!'}")
    for a, b, c in zip(to_pins(key), to_pins(lock), to_pins(key&lock)):
        print(f"  {a} {b} {c}")
    print()


total = 0
for lock in locks:
    for key in keys:
        if len(keys) < 10:
            show_schematic(key, lock)
        total += int(not(key&lock))

print(f"{total=}")

# total=3063 0.015s wrong too low: forgot to add extra newline to end of input
# total=3065 0.017s