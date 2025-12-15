day = 7

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()

# Part 1

start_x = lines[0].find("S")
start_y = 0
height = len(lines)
width = len(lines[0])

carrot_positions = set()
visited = set()


def find_carrots(x, y):
    if (x, y) in visited:
        return
    visited.add((x, y))
    while True:
        if y == height:
            break

        elem = lines[y][x]
        if elem == "^":
            carrot_positions.add((x, y))
            find_carrots(x - 1, y + 1)
            find_carrots(x + 1, y + 1)
            break
        else:
            y += 1


find_carrots(start_x, start_y)

print("Part1: ", len(carrot_positions))

# Part 2

height = len(lines)
start_x = lines[0].find("S")


def find_timelines(x, y):
    while True:
        if y == height:
            return 1
        elif f"{x},{y}" in memo:
            return memo[f"{x},{y}"]
        else:
            return find_timelines(x, y + 1)


memo = {}
for y in range(height - 1, -1, -1):
    line = lines[y]
    for x in range(len(line)):
        elem = line[x]
        if elem in ["^", "S"]:
            memo[f"{x},{y}"] = find_timelines(x - 1, y + 1) + find_timelines(
                x + 1, y + 1
            )

print("Part2: ", memo[f"{start_x},0"])
