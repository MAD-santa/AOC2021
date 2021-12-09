import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day9list.txt", "r")
heightMap = []
for row in f:
    row = row.replace('\n', '')
    heightMap.append(row)
lowPoints = []
# PART 1
riskLevel = 0
for y in range(len(heightMap)):
    for x in range(len(heightMap[y])):
        counter = 0
        if y-1 >= 0:
            if heightMap[y-1][x] > heightMap[y][x]:
                counter+=1
        else:
            counter+=1
        if y+1 < len(heightMap):
            if heightMap[y+1][x] > heightMap[y][x]:
                counter+=1
        else:
            counter+=1
        if x-1 >= 0:
            if heightMap[y][x-1] > heightMap[y][x]:
                counter+=1
        else:
            counter+=1
        if x+1 < len(heightMap[y]):
            if heightMap[y][x+1] > heightMap[y][x]:
                counter+=1
        else:
            counter+=1
        if counter == 4:
            riskLevel+=int(heightMap[y][x])+1
            lowPoints.append([x,y])
print("Answer for part 1 is: ", riskLevel)


# Part 2
def searchBasin(x,y):
    counter=1
    if y - 1 >= 0:
        if int(heightMap[y - 1][x]) > int(heightMap[y][x]) and int(heightMap[y - 1][x]) != 9:
            if searched.count([x,y-1]) == 0:
                searched.append([x, y - 1])
                counter += searchBasin(x,y-1)
    if y + 1 < len(heightMap):
        if int(heightMap[y + 1][x]) > int(heightMap[y][x]) and int(heightMap[y + 1][x]) != 9:
            if searched.count([x,y+1]) == 0:
                searched.append([x, y + 1])
                counter += searchBasin(x,y+1)
    if x - 1 >= 0:
        if int(heightMap[y][x - 1]) > int(heightMap[y][x]) and int(heightMap[y][x - 1]) != 9:
            if searched.count([x-1,y]) == 0:
                searched.append([x-1, y])
                counter += searchBasin(x-1,y)
    if x + 1 < len(heightMap[y]):
        if int(heightMap[y][x + 1]) > int(heightMap[y][x]) and int(heightMap[y][x+1]) != 9:
            if searched.count([x+1,y]) == 0:
                searched.append([x+1, y])
                counter += searchBasin(x+1,y)
    return counter
basinList = []
for lowPoint in lowPoints:
    searched = []
    basinList.append(searchBasin(lowPoint[0],lowPoint[1]))
basinList.sort(reverse = True)
print("The answer for part 2 is: ", basinList[0]*basinList[1]*basinList[2])
f.close()
end = current_milli_time()
print(str(end - start) + "ms")
f.close()
