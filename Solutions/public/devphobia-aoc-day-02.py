aim, depth, horizontal = 0, 0, 0

for info in open("input.txt").readlines():
    if info.split()[0] == "up": aim -= int(info.split()[1])
    elif info.split()[0] == "down": aim += int(info.split()[1])
    else:
        depth += aim*int(info.split()[1])
        horizontal += int(info.split()[1])

print(horizontal*aim, depth*horizontal)
