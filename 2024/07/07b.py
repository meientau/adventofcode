import fileinput

def mul(a, b): return a*b
def add(a, b): return a+b
def con(a, b): return int(f"{a}{b}")
operations = [mul, add, con]

def fill(result, rest, partial=0):
    if not rest:
        good = result == partial
        if good and fileinput.lineno() < 10:
            print(result)
        return good

    return any(fill(result, rest[1:], op(partial, rest[0])) for op in operations)

sum = 0
for line in fileinput.input():
    result, rest = line.strip().split(": ")
    result = int(result)
    operands = [int(n) for n in rest.split()]

    if fill(result, operands[1:], operands[0]):
        sum += result

print(sum)
# 169122112716571 11.542s
