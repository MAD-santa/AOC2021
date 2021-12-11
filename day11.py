import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day11list.txt", "r")
octopusGrid = []
for row in f:
    row = row.replace('\n', '')
    row = list(map(lambda x: int(x), row))
    octopusGrid.append(row)
octopusGrid2 = [*octopusGrid]
# PART 1
flashlist = []
flashed = []
flashcounter = 0


def plusOne(ogl):
    for x in range(len(ogl)):
        ogl[x] = list(map(lambda y: y + 1, ogl[x]))
    return ogl


def checkFlash(ogl):
    global flashcounter
    for y in range(len(ogl)):
        for x in range(len(ogl[y])):
            if ogl[y][x] >= 10 and flashed.count([y, x]) == 0:
                flashlist.append([y, x])
                flashcounter += 1


def flash(flashthis):
    y = flashthis[0]
    x = flashthis[1]
    if y > 0:
        octopusGrid[y - 1][x] += 1
    if y < len(octopusGrid) - 1:
        octopusGrid[y + 1][x] += 1
    if x > 0:
        octopusGrid[y][x - 1] += 1
    if x < len(octopusGrid[y]) - 1:
        octopusGrid[y][x + 1] += 1
    if y > 0 and x > 0:
        octopusGrid[y - 1][x - 1] += 1
    if y > 0 and x < len(octopusGrid[y]) - 1:
        octopusGrid[y - 1][x + 1] += 1
    if x < len(octopusGrid[y]) - 1 and y < len(octopusGrid) - 1:
        octopusGrid[y + 1][x + 1] += 1
    if x > 0 and y < len(octopusGrid) - 1:
        octopusGrid[y + 1][x - 1] += 1


def flashedToZero(flashedlist):
    octopusGrid[flashedlist[0]][flashedlist[1]] = 0


# part 1
allflash = 0
for step in range(100):
    plusOne(octopusGrid)
    while True:
        checkFlash(octopusGrid)
        list(map(flash, flashlist))
        flashed = flashed + [*flashlist]
        if len(flashlist) == 0:
            break
        flashlist = []
    list(map(flashedToZero, flashed))
    flashed = []
print("The answer for part 1 is:", flashcounter)

# part 2
octopusGrid = [*octopusGrid2]
allflash = 0
step = 1
while allflash == 0:
    plusOne(octopusGrid)
    while True:
        checkFlash(octopusGrid)
        list(map(flash, flashlist))
        flashed = flashed + [*flashlist]
        if len(flashed) == 100:
            allflash = step
        if len(flashlist) == 0:
            break
        flashlist = []
    list(map(flashedToZero, flashed))
    flashed = []
    step += 1
print("The answer for part 2 is: ", allflash)
f.close()

end = current_milli_time()
print(str(end - start) + "ms")
f.close()
