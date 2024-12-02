from fileinput import input

count = 0
for line in input():
    line = [int(v) for v in line.split()]
    steps = { b-a for a, b in zip(line, line[1:]) }
    print(steps)
    if min(steps) >= -3 and max(steps) <= -1 or min(steps) >= 1 and max(steps) <= 3: 
        count += 1
        
print(count)
