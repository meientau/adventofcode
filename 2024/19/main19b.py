import fileinput


def is_possible(line):
    if not line:
        return True

    for prefix in available:
        if line.startswith(prefix):
            if len(available) < 20:
                print(f"line '{line}' starts with '{prefix}'")
            if is_possible(line[len(prefix):]):
                return True
    return False


available = None
possible = 0
for line in fileinput.input():
    line = line.strip()

    if not line:
        continue

    if not available:
        available = [t.strip(', ') for t in line.split()]
        continue

    possible += is_possible(line)

print(possible)
