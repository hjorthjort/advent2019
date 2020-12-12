with open('input.txt', 'r') as f:
    wires = f.readlines()

# w1

grid = {(0, 0): [True, True]}
current = [0, 0]
total_steps = 0
step_counts = [{(0, 0): 0}, {(0, 0): 0}]

def move_x(idx, steps):
    move(0, idx, steps)

def move_y(idx, steps):
    move(1, idx, steps)

def move(axis, idx, steps):
    global current
    global grid
    global total_steps
    inc = -1 if steps < 0 else 1
    steps = abs(steps)
    step_count = step_counts[idx]
    for i in range(steps):
        total_steps += 1
        current[axis] = current[axis] + inc
        key = tuple(current)
        if key not in grid:
            grid[key] = [False, False]
        if key not in step_count:
            step_count[key] = total_steps
        status = grid[key]
        status[idx] = True
        grid[key] = status

for wire in range(len(wires)):
    current = [0, 0]
    total_steps = 0
    for step in wires[wire].split(','):
        d = step[0]
        i = int(step[1:])
        if d == 'R':
            move_x(wire, i)
        if d == 'L':
            move_x(wire, -i)
        if d == 'U':
            move_y(wire, i)
        if d == 'D':
            move_y(wire, -i)

crossings = list(filter(lambda key_val: all(key_val[1]), grid.items()))
dists = list(map(lambda item: abs(item[0][0]) + abs(item[0][1]), crossings))

tots = []
for c in crossings:
    a = step_counts[0][c[0]]
    b = step_counts[1][c[0]]
    tots.append(a + b)

dists.sort()
tots.sort()

print(dists[1])
print(tots[1])
