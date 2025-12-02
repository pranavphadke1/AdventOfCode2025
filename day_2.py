day = 2

with open(f"Inputs/day{day}.txt") as f:
    lines = f.read().splitlines()

ranges = "".join(lines).split(",")

# Part 1
c = 0
for r in ranges:
    start, stop = map(int, r.split("-"))
    for i in range(start, stop + 1):
        i_str = str(i)
        # Odd length numbers are valid
        length = len(i_str)
        if length % 2 == 1:
            continue
        middle = int(length / 2)
        x, y = i_str[:middle], i_str[middle:]
        if x == y:
            c += i

print("Part 1: ", c)


# Part 2
c = 0
for r in ranges:
    start, stop = map(int, r.split("-"))
    for i in range(start, stop + 1):
        i_str = str(i)
        length = len(i_str)

        # find all divisors of the length of the string. These divisors are the possible substring lengths
        divisors = []
        for div in range(1, length):
            if length % div == 0:
                divisors.append(div)

        for div in divisors:
            # find all substrings at `div` intervals
            substrings = {i_str[sub : sub + div] for sub in range(0, length, div)}
            # if there is only one substring in the set, this divisor interval has found an invalid id
            if len(substrings) == 1:
                c += i
                break

print("Part 2: ", c)
