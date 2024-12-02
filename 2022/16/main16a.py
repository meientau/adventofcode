#!/bin/python3

import sys
import re
from collections import defaultdict


valves = dict()


def showstate(time, openvalves, mv, op):
    print(f"== Minute {time} ==")
    if not openvalves:
        print("No valves are open.")
    elif len(openvalves) == 1:
        print(f"Valve {openvalves[0].id} is open, releasing {openvalves[0].flowrate} pressure.")
    else:
        print("Valves " + (", ".join([v.id for v in openvalves[:-1]]) + " and " + openvalves[-1].id)
              + f" are open, releasing {sum(v.flowrate for v in openvalves)} pressure.")

    if mv:
        print(f"You move to valve {mv.id}.")
    elif op:
        print(f"You open valve {op.id}.")

    print()


maxvisit = 2
maxrelease = 0
class Valve:
    RE_DESCRIPTION = re.compile(r"Valve (?P<id>[A-Z]{2}) has flow rate=(?P<flowrate>\d+); tunnels? leads? to valves? (?P<paths>[A-Z, ]+)")

    def __init__(self, description):
        match = Valve.RE_DESCRIPTION.match(description)
        if not match:
            raise ValueError(f"Cannot parse {description=}")

        self.id = match.group('id')
        self.flowrate = int(match.group('flowrate'))
        self.paths = match.group('paths').split(', ')

    def __str__(self):
        return f"Valve {self.id} has flow rate={self.flowrate}; tunnels lead to valves {', '.join(self.paths)}"

    def __repr__(self):
        return self.__str__()

    def walk(self, openvalves=None, time=0, currentflow=0, totalrelease=0, seen=None):
        openvalves = openvalves or list()
        seen = seen or defaultdict(int)

        if len(openvalves) == len(valves):
            totalrelease += currentflow * (30-time)
            time = 30

        if time == 30:
            print(f"{totalrelease=}")
            global maxrelease
            maxrelease = max(maxrelease, totalrelease)
            return

        newtime = time
        for thisopened in range((self not in openvalves and self.flowrate > 0) + 1):
            newopenvalves = list(openvalves)
            if thisopened:
                newopenvalves.append(self)
                newtime += 1
                showstate(newtime, openvalves, None, self)

            newtime += 1
            newseen = seen.copy()
            newseen[self] += 1

            for path in self.paths:
                v = valves[path]
                if seen[v] < maxvisit:
                    showstate(newtime, newopenvalves, v, None)
                    v.walk(newopenvalves,
                           newtime,
                           currentflow + self.flowrate*thisopened,
                           totalrelease + currentflow*2 + self.flowrate*thisopened,
                           newseen)


firstvalve = None
for d in sys.stdin.readlines():
    v = Valve(d)
    valves[v.id] = v
    firstvalve = firstvalve or v

firstvalve.walk()
print(f"{maxrelease=}")
