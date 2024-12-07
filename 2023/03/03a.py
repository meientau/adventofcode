import fileinput

lines = [line.strip() for line in fileinput.input()]
width = len(lines[0]) + 1
buffer_line = '.' * width
text = buffer_line + '.'.join(lines) + buffer_line

if width < 20:
    print(text)
