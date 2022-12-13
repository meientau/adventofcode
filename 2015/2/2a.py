#!/bin/python3

import fileinput

totalarea = 0
totalribbon = 0
for line in fileinput.input():
    a, b, c = sorted(map(int, line.strip().split('x')))
    area = 2*a*b + 2*b*c + 2*c*a + a*b
    ribbon = 2*(a+b) + a*b*c
    totalarea += area
    totalribbon += ribbon
    print(f"{area=} {totalarea=} {totalribbon=}")
