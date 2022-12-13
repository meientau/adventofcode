#!/bin/python3

import sys

i = sys.stdin.read()

for p in range(14, len(i)):
    chunk = i[p-14:p]
    print((chunk, set(chunk), len(set(chunk))))
    if len(set(chunk)) == 14:
        print(p)
        break
