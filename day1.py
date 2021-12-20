import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day1list.txt", "r")
measurements = []
for row in f:
    row = row.replace('\n', '')
    measurements.append(int(row))

# PART 1
lastdepth = measurements[0]
counter = 0
for depth in measurements:
    if lastdepth < depth:
        counter += 1
    lastdepth = depth
print("Part 2: " + str(counter))

# PART 2
counter = 0
lastWindow = measurements[0] + measurements[1] + measurements[2]
for x in range(len(measurements) - 2):
    currentWindow = measurements[x] + measurements[x + 1] + measurements[x + 2]
    if lastWindow < currentWindow:
        counter += 1
    lastWindow = currentWindow
print("Part 2: " + str(counter))
end = current_milli_time()
print(str(end - start) + "ms")
f.close()
