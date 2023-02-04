#!/bin/python3

import sys
import re
from collections import defaultdict
import itertools


valves = dict()
deadline = 30


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


class Valve:
    RE_DESCRIPTION = re.compile(r"Valve (?P<id>[A-Z]{2}) has flow rate=(?P<flowrate>\d+); tunnels? leads? to valves? (?P<paths>[A-Z, ]+)")

    def __init__(self, description):
        match = Valve.RE_DESCRIPTION.match(description)
        if not match:
            raise ValueError(f"Cannot parse {description=}")

        self.id = match.group('id')
        self.flowrate = int(match.group('flowrate'))
        self.paths = match.group('paths').split(', ')
        self.distances = dict((valve, 1) for valve in self.paths)
        self.distances[self.id] = 0

    @staticmethod
    def calc_distances():
        todo = set(valves)
        while todo:
            seen = set()
            for vid in todo:
                valve = valves[vid]
                if valve.update_distances():
                    seen |= set(valve.paths)

            todo = seen

    def update_distances(self):
        updated = False
        for neighbour in self.paths:
            for remote, distance in valves[neighbour].distances.items():
                if remote in self.distances:
                    continue

                self.distances[remote] = distance + 1
                updated = True

        return updated

    def show_distances(self, allids):
        return ' '.join(f"{self.distances[remote]:3}" for remote in allids)

    def __str__(self):
        return f"Valve {self.id} has flow rate={self.flowrate}; tunnels lead to valves {', '.join(self.paths)}"

    def __repr__(self):
        return self.__str__()

    def walk(self):
        useful_valves = list(v for v in valves.values() if v.flowrate > 0)
        for length in range(3, len(useful_valves) + 1):
            maxrelease = 0
            maxopen = 0
            maxroute = list()
            for route in itertools.permutations(useful_valves, length):
                total_open = 0
                all_open = []
                total_release = 0
                time = 0
                for last_valve, next_valve in zip([firstvalve] + list(route), route):
                    new_time = time + last_valve.distances[next_valve.id]
                    total_release += total_open * (min(deadline, new_time) - time)
                    time = new_time

                    if time > deadline:
                        break

                    # You open valve {next_valve.id}.
                    total_release += total_open
                    all_open.append(next_valve.id)
                    total_open += next_valve.flowrate
                    time += 1

                rest_time = max(0, deadline - time)
                total_release += total_open * rest_time

                #print(f" {total_release:3} {time:3} {'->'.join(all_open)}")

                if total_release > maxrelease:
                    maxrelease = total_release
                    maxopen = total_open
                    maxroute = route

            print(f"{length=} {maxrelease=} {maxopen=} route={'->'.join(v.id for v in maxroute)}")


firstvalve = None
for d in sys.stdin.readlines():
    v = Valve(d)
    valves[v.id] = v
    firstvalve = firstvalve or v


Valve.calc_distances()

if len(valves) < 30:
    allids = sorted(valves.keys())
    print("     " + '  '.join(allids))
    for v in valves.values():
        print(f"{v.id}: {v.show_distances(allids)}")
    print()

firstvalve.walk()
# small target: DD->BB->JJ->HH->EE->CC

# 2019 is too high
