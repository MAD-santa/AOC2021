import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day2list.txt", "r")
instructions = []
for row in f:
    row = row.replace('\n', '')
    row = row.split(' ')
    instructions.append(row)

# PART 1
horizontal = 0
depth = 0
for instruction in instructions:
    match instruction[0]:
        case "forward":
            horizontal+=int(instruction[1])
        case "down":
            depth+=int(instruction[1])
        case "up":
             depth-=int(instruction[1])
print(horizontal*depth)

# PART 1
horizontal = 0
depth = 0
aim = 0
for instruction in instructions:
    match instruction[0]:
        case "forward":
            horizontal+=int(instruction[1])
            depth+=aim*int(instruction[1])
        case "down":
            aim+=int(instruction[1])
        case "up":
             aim-=int(instruction[1])
print(horizontal*depth)


f.close()
end = current_milli_time()
print(str(end - start) + "ms")
f.close()
