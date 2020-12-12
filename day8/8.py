with open('input.txt') as f:
    input = f.read()
    # Remove last newline.
    input = input[:-1]
ints = list(map(int, input))

width = 25
height = 6

group_size = width * height

layers = []

while len(ints) > 0:
    layer = []
    for i in range(group_size):
        layer.append(ints[0])
        ints = ints[1:]
    layers.append(layer)


def occurs(layer, num):
    return len([i for i in layer if i == num])


counts = [(occurs(l, 0), l) for l in layers]
counts.sort()

(_, least_zeros) = counts[0]
ones = occurs(least_zeros, 1)
twos = occurs(least_zeros, 2)

print(ones*twos)

final_layer = [2] * group_size

for l in layers:
    for i in range(group_size):
        if final_layer[i] == 2:
            final_layer[i] = l[i]

# Display.
result = ''.join(map(lambda x: '\u25a0' if x == 1 else ' ', final_layer))
for y in range(height):
    print(' '.join(result[0:width]))
    result = result[width:]
