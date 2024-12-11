import fileinput
import re
import string

lines = [line.strip() for line in fileinput.input()]
width = len(lines[0]) + 1
buffer_line = '.' * width
text = buffer_line + '.'.join(lines) + buffer_line

if width < 20:
    print(text)

numbers_re = re.compile(r'\d+')

sum = 0
for match in numbers_re.finditer(text):
    start, end = match.span(0)
    start, end = start-1, end+1
    vicinity = (text[start-width:end-width] + '\n'
                + text[start:end] + '\n'
                + text[start+width:end+width] + '\n')

    if width < 20:
        print(vicinity)

    stripped = vicinity.strip(".\n" + string.digits)
    if stripped:
        if width < 20:
            print(f"{stripped=}")
        sum += int(match.group(0))
        if width < 20:
            print(vicinity)



print(f"{sum=}")
# 525911 0.043s
