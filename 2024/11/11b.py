import fileinput
import functools

@functools.cache # without caching, it's still way too slow
def evolve(pebble, depth):
    if depth < 1:
        return 1
    
    if pebble == 0:
        return evolve(1, depth-1)
    
    pebble_inscription = str(pebble)
    n_digits = len(pebble_inscription)
    if not n_digits % 2:
        cut = n_digits // 2
        return (evolve(int(pebble_inscription[:cut]), depth-1)
                + evolve(int(pebble_inscription[cut:]), depth-1))
    
    return evolve(pebble * 2024, depth-1)

pebbles = [int(v) for v in next(fileinput.input()).split()]

debug = len(pebbles) < 10
if debug: print(pebbles)


total = 0
for pebble in pebbles:
    result = evolve(pebble, depth=75)
    total += result
    print(f"{pebble=} {result=} {total=}")
        
print(f"{total=}")
# total=255758646442399 0.119s