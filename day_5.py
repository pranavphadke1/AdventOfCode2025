day = 5

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()

split = lines.index("")
ranges = lines[:split]
indexes = lines[split + 1 :]

# Part 1

fresh_ids = {}

for r in ranges:
    new_lower, new_upper = map(int, r.split("-"))
    for cur_low, cur_up in list(fresh_ids.items()):
        # no overlap
        if new_lower > cur_up or new_upper < cur_low:
            continue

        # There is overlap
        new_lower = min(new_lower, cur_low)
        new_upper = max(new_upper, cur_up)

        # remove old
        del fresh_ids[cur_low]

    fresh_ids[new_lower] = new_upper

c = 0
for i in indexes:
    for low, up in list(fresh_ids.items()):
        if low <= int(i) <= up:
            c += 1

print("Part 1", c)


total = 0
# Part 2:
for low, up in list(fresh_ids.items()):
    total += up - low + 1

print("Part 2", total)
