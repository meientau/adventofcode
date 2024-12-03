import re
import fileinput

re_muls = re.compile(r"(?P<on>do\(\))|(?P<off>don't\(\))|mul\((?P<a>[0-9]+),(?P<b>[0-9]+)\)")

sum = 0
on = True
for line in fileinput.input():
    for match in re_muls.finditer(line):
        print(match.groups())
        if match.group('on'):
            on = True
        elif match.group('off'):
            on = False
        elif on:
            sum += int(match.group('a')) * int(match.group('b'))

print(sum)