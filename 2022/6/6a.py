#!/bin/python3

import sys

i = sys.stdin.read()

for p in range(4, len(i)):
    chunk = i[p-4:p]
    print((chunk, set(chunk), len(set(chunk))))
    if len(set(chunk)) == 4:
        print(p)
        break
