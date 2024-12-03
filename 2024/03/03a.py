import re
import fileinput

re_muls = re.compile(r"mul\(([0-9]+),([0-9]+)\)")

sum = 0
for line in fileinput.input():
    for match in re_muls.finditer(line):
        sum += int(match.group(1)) * int(match.group(2))

# 173785482
print(sum)