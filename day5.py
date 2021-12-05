import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day5list.txt", "r")
lineCoordinates = []
maxX = 0
maxY = 0
for row in f:
    row = row.replace('\n', '')
    row = row.replace(' -> ', ',')
    row = row.split(',')
    row = list(map(int, row))
    if maxY < row[1]:
        maxY = row[1]
    if maxY < row[3]:
        maxY = row[3]
    if maxX < row[0]:
        maxX = row[0]
    if maxX < row[2]:
        maxX = row[2]
    lineCoordinates.append(row)
# part 1
dangerMap = {}
for y in range(maxY+1):
    dangerMap[y] = {}
    for x in range(maxX+1):
        dangerMap[y][x] = 0
for line in lineCoordinates:
    x1 = line[0]
    x2 = line[2]
    y1 = line[1]
    y2 = line[3]
    if x1 == x2:
        if y1 > y2:
            length = y1 - y2
            for i in range(length+1):
                dangerMap[y2+i][x1]+=1
        if y2 > y1:
            length = y2 - y1
            for i in range(length+1):
                dangerMap[y1+i][x1]+=1
    if y1 == y2:
        if x1 > x2:
            length = x1 - x2
            for i in range(length+1):
                dangerMap[y1][x2+i]+=1
        if x2 > x1:
            length = x2 - x1
            for i in range(length+1):
                dangerMap[y1][x1+i]+=1
countCross = 0
for row in range(len(dangerMap)):
    for col in range(len(dangerMap[row])):
        if dangerMap[row][col] > 1:
            countCross+=1
print("The answer is: ", countCross)


# part 2
for line in lineCoordinates:
    x1 = line[0]
    x2 = line[2]
    y1 = line[1]
    y2 = line[3]
    if x1 != x2 and y1 != y2:
        if x1<x2 and y1 < y2:
            length = x2 - x1
            for i in range(length + 1):
                dangerMap[y1+i][x1 + i] += 1
        if x1<x2 and y1 > y2:
            length = x2 - x1
            for i in range(length + 1):
                dangerMap[y1 - i][x1 + i] += 1
        if x1>x2 and y1 < y2:
            length = x1 - x2
            for i in range(length + 1):
                dangerMap[y1 + i][x1 - i] += 1
        if x1>x2 and y1 > y2:
            length = x1 - x2
            for i in range(length + 1):
                dangerMap[y1 - i][x1 - i] += 1

countCross = 0
for row in range(len(dangerMap)):
    for col in range(len(dangerMap[row])):
        if dangerMap[row][col] > 1:
            countCross+=1
print("The answer for part2 is: ", countCross)
f.close()
end = current_milli_time()
print(str(end - start) + "ms")
f.close()
