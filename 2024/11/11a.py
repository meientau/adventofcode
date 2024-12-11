import fileinput

todo = [int(v) for v in next(fileinput.input()).split()]
debug = len(todo) < 10
if debug: print(todo)

def evolve(pebble):
    if pebble == 0:
        return [1]
    
    pebble_inscription = str(pebble)
    n_digits = len(pebble_inscription)
    if not n_digits % 2:
        cut = n_digits // 2
        return [int(pebble_inscription[:cut]),
                int(pebble_inscription[cut:])]
    
    return [pebble * 2024]

for i in range(25):
    next_todo = list()
    for pebble in todo:
        next_todo += evolve(pebble)
    todo = next_todo
        
if debug: print(todo)
print(f"{len(todo)=}")
# 216042 0.263s for 25 cycles
