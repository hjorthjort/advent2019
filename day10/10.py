from math import gcd

with open('input.txt') as f:
    inp = f.read()

inp = inp.splitlines()

asts = set()

for y in range(len(inp)):
    for x in range(len(inp[y])):
        if inp[x][y] == '#':
            asts.add((x, y))

counts = []

for a in asts:
    s = asts.copy()
    s.remove(a)
    angles = set()
    n = 0
    (x, y) = a
    for (x_o, y_o) in s:
        x_d = x_o - x
        y_d = y_o - y
        d = gcd(x_d, y_d)
        x_d //= d
        y_d //= d
        angle = (x_d, y_d)
        if angle not in angles:
            n += 1
            angles.add(angle)
    counts.append(n)

print(max(counts))
