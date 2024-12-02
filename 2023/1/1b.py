#!/bin/python3

import fileinput

#words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

sum=0
for line in fileinput.input():
    line = line.strip()
    try:
        digits = list()
        while line:
            try:
                i = int(line[0])
                digits.append(i)
                line = line[1:]
                continue
            except ValueError:
                pass
            
            for i, word in enumerate(words, 1):
                if line.startswith(word):
                    digits.append(i)
                    nextline = line[len(word):]
                    print(f"{line} - {word} -> {nextline}")
                    line = nextline
                    break


            line = line[1:]
    except KeyboardInterrupt:
        print(fileinput.lineno())

    if len(digits) == 1:
        digits += digits
    value = 10*digits[0] + digits[-1]
    print(value)
    sum += value

print(sum)

# 55186 too high
# 54971 too high