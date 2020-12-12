input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

with open('input.txt') as f:
    input = f.read()

lines = input.splitlines()
pairs = [x.split(')') for x in lines]
for p in pairs:
    p.reverse()

graph = dict(pairs)

def orbit_path(obj):
    global graph
    if obj == 'COM':
        return []
    assert obj in graph, obj
    origin = graph[obj]
    return [obj] + orbit_path(origin)

counts = map(len, map(orbit_path, graph.keys()))

print(sum(counts))

# Find the path to COM from the object you orbit, and the one Santa orbits.
# Includes You and Santa and the object you orbit, so remove 3.
# -3
com_to_you = orbit_path('YOU')
com_to_san = orbit_path('SAN')

# Remove all parts of the path to COM which is common (pus 2 extra).
# +2
while com_to_you.pop() == com_to_san.pop():
    pass

# Result: the length of the 2 remaining paths
# plus 1 (for the last closest common orbit object.)
# +1

# All in all, the off by X errors cancel.
print(len(com_to_you) + len(com_to_san))
