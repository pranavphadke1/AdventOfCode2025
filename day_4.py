day = 4

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()

# Part 1
max_i = len(lines) - 1
total = 0
for y in range(max_i + 1):
    for x in range(max_i + 1):

        center = lines[y][x]
        if center == ".":
            continue

        c = 0

        y_a, y_b, x_l, x_r = None, None, None, None
        if y > 0:
            y_a = y - 1
        if y < max_i:
            y_b = y + 1
        if x > 0:
            x_l = x - 1
        if x < max_i:
            x_r = x + 1

        if y_a is not None:
            elem = lines[y_a][x]
            if elem == "@":
                c += 1
            if x_l is not None:
                elem = lines[y_a][x_l]
                if elem == "@":
                    c += 1
            if x_r is not None:
                elem = lines[y_a][x_r]
                if elem == "@":
                    c += 1
        if x_l is not None:
            elem = lines[y][x_l]
            if elem == "@":
                c += 1
        if x_r is not None:
            elem = lines[y][x_r]
            if elem == "@":
                c += 1

        if y_b is not None:
            elem = lines[y_b][x]
            if elem == "@":
                c += 1
            if x_l is not None:
                elem = lines[y_b][x_l]
                if elem == "@":
                    c += 1
            if x_r is not None:
                elem = lines[y_b][x_r]
                if elem == "@":
                    c += 1

        if c < 4:

            total += 1

print("Part 1: ", total)

# Part 2


cur_total = 0
last_total = -1

while last_total != cur_total:
    total = 0

    for y in range(max_i + 1):
        for x in range(max_i + 1):

            center = lines[y][x]

            if center == ".":
                continue

            c = 0

            y_a, y_b, x_l, x_r = None, None, None, None

            if y > 0:
                y_a = y - 1
            if y < max_i:
                y_b = y + 1
            if x > 0:
                x_l = x - 1
            if x < max_i:
                x_r = x + 1

            if y_a is not None:
                elem = lines[y_a][x]
                if elem == "@":
                    c += 1
                if x_l is not None:
                    elem = lines[y_a][x_l]
                    if elem == "@":
                        c += 1
                if x_r is not None:
                    elem = lines[y_a][x_r]
                    if elem == "@":
                        c += 1

            if x_l is not None:
                elem = lines[y][x_l]
                if elem == "@":
                    c += 1
            if x_r is not None:
                elem = lines[y][x_r]
                if elem == "@":
                    c += 1

            if y_b is not None:
                elem = lines[y_b][x]
                if elem == "@":
                    c += 1
                if x_l is not None:
                    elem = lines[y_b][x_l]
                    if elem == "@":
                        c += 1
                if x_r is not None:
                    elem = lines[y_b][x_r]
                    if elem == "@":
                        c += 1

            if c < 4:
                total += 1
                lines[y] = lines[y][:x] + "." + lines[y][x + 1 :]

    last_total = cur_total
    cur_total += total


print("Part 2: ", cur_total)
