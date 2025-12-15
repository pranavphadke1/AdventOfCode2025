day = 6

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()

# Part 1
import math

parsed_lines = []
for line in lines:
    parsed_lines.append(line.split())

zipped = list(zip(*parsed_lines))

c = 0
for line in zipped:
    arith = line[-1]
    nums = list(map(int, line[:-1]))
    if arith == "+":
        c += sum(nums)
    else:
        c += math.prod(nums)

print("Part1 : ", c)


# Part 2

# Find the breaking points using index before arithmetic
arith = lines[-1]
indexes = set()
for i in range(1, len(arith)):
    if arith[i] != " ":
        indexes.add(i - 1)

new_lines = []
for line in lines[:-1]:
    new_line = ""
    for i in range(len(line)):
        if i in indexes:
            new_line += "-"
        else:
            new_line += line[i]
    new_lines.append(new_line)


lines = new_lines


parsed_lines = []
for line in lines:
    parsed_lines.append(line.split("-"))

zipped = list(zip(*parsed_lines))
reparsed = []

for x in zipped:
    y = list(map(list, list(x)))
    z = ["".join(col) for col in zip(*y)]
    j = [int(i.strip()) for i in z]
    reparsed.append(j)

arith = list(arith.split())
rezipped = list(zip(reparsed, arith))


c = 0
for group in rezipped:
    nums, operation = group[0], group[1]
    if operation == "+":
        c += sum(nums)
    else:
        c += math.prod(nums)

print("Part2 : ", c)
