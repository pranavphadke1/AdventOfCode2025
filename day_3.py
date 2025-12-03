day = 3

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()

# Part 1
c = 0
num_batteries = len(lines[0])
for line in lines:
    left = 0
    left_i = 0

    for i in range(num_batteries - 1):
        cur_left = int(line[i])
        if cur_left > left:
            left = cur_left
            left_i = i + 1
    right = 0
    for battery in line[left_i:]:
        cur_right = int(battery)
        if cur_right > right:
            right = cur_right

    joltage = int(f"{left}{right}")
    c += joltage

print("Part1: ", c)

# Part 2
c = 0
num_batteries = len(lines[0])
for line in lines:
    cur_index = 0
    left_sliding_index = (
        0  # Tracks how many indexes we've moved relative to `cur_index`
    )
    joltage = ""
    # `x` represents how many batteries have already been select.
    for x in range(12):
        # The possible batteries for each sliding window changes in respect to
        # the total number of batteries in a bank and the number of batteries
        # that have already been selected.
        possible_batteries = line[left_sliding_index : num_batteries - 12 + x + 1]
        left = 0
        for i in range(len(possible_batteries)):
            left_sliding_index += 1
            cur_left = int(possible_batteries[i])
            if cur_left > left:
                left = cur_left
                # Set the next 'current' index
                cur_index = left_sliding_index
        # Reset sliding index to index of highest voltage battery during this
        # window. This allows batteries we didn't pick in this window
        # to be included in the next window.
        left_sliding_index = cur_index
        joltage += str(left)

    c += int(joltage)

print("Part2: ", c)
