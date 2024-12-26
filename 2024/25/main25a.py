import fileinput

keys = list()
locks = list()
current = 0
this_is = None
for line in fileinput.input():
    line = line.strip()
    if not line:
        if current:
            this_is.append(current)
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


total = 0
for key in keys:
    for lock in locks:
        if len(keys) < 10:
            print(f"key:     {key:030b}")
            print(f"lock:    {lock:030b}")
            print(f"overlap: {lock&key:030b}")
        total += int(not(key&lock))

print(f"{total=}")

# total=3063 0.015s wrong
