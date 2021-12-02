aim, depth, horizontal = 0, 0, 0

for info in [info.split() for info in open("input.txt").readlines()]:
    if info[0] == "up": aim -= int(info[1])
    elif info[0] == "down": aim += int(info[1])
    else:
        depth += aim*int(info[1])
        horizontal += int(info[1])

print(horizontal*aim, depth*horizontal)
