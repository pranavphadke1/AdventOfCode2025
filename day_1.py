day = 1

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()


# Part 1
cur, count = 50, 0

for line in lines:
    direction, move = line[0], int(line[1:])
    if direction == "L":
        cur = (cur - move) % 100
    else:
        cur = (cur + move) % 100

    if cur == 0:
        count += 1

print("part 1", count)

# Part 2
cur, count = 50, 0

for line in lines:
    direction, move = line[0], int(line[1:])

    # Calc >100 rotation
    if move > 100:
        count += int(move / 100)
        move = move % 100

    if direction == "L":
        new_cur = cur - move
    else:
        new_cur = cur + move

    # increment count if current isn't at 0 and new current is either negative or greater than 100
    # (if current is at 0 we would be double counting )
    if cur != 0 and (new_cur <= 0 or new_cur >= 100):
        count += 1

    cur = new_cur % 100


print("part 2", count)
