import fileinput


def is_possible(line):
    if not line:
        return 1

    total = 0
    for prefix in available:
        if line.startswith(prefix):
            if len(available) < 20:
                print(f"line '{line}' starts with '{prefix}'")
            total += is_possible(line[len(prefix):])

    return total


available = None
possible = 0
for line in fileinput.input():
    line = line.strip()

    if not line:
        continue

    if not available:
        available = [t.strip(', ') for t in line.split()]
        continue

    n = is_possible(line)
    print(f"{n=} {line}")
    possible += n

print(possible)
