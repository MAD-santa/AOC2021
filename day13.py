import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day13list.txt", "r")
inputData = []
dots = []
foldInstructions = []
bp = 0
for row in f:
    row = row.replace('\n', '')
    inputData.append(row)
dots = [*inputData[:inputData.index("")]]
foldInstructions = [*inputData[inputData.index("")+1:]]
dots = list(map(lambda x: x.split(','), dots))
dots = list(map(lambda x: [int(x[0]),int(x[1])], dots))
maxX = 0
maxY = 0
for row in dots:
    if row[0] > maxX:
        maxX = row[0]
    if row[1] > maxY:
        maxY = row[1]
# PART 1

dotMap = {}
for y in range(maxY+1):
    dotMap[y] = []
    for x in range(maxX+1):
        dotMap[y] += '.'
for row in dots:
    dotMap[row[1]][row[0]] = "#"

def foldX(foldline):
    global dotMap
    tempMap = {}
    for i in range(len(dotMap)):
        tempMap[i] = dotMap[i][:foldline-(len(dotMap[i])-1-foldline)]
        for x in range(len(dotMap[i])-1-foldline):
            if dotMap[i][len(dotMap[i]) - 1 -x] == "#" or dotMap[i][foldline-(len(dotMap[i])-1-foldline)+x] == "#":
                tempMap[i] += "#"
            else:
                tempMap[i] += "."
    dotMap = tempMap
def foldY(foldline):
    global dotMap
    tempMap = {}
    for i in range(foldline - (len(dotMap) - foldline - 1)):
        tempMap[i] = dotMap[i]
    for i in range(len(dotMap) - foldline - 1):
        tempMap[foldline - (len(dotMap) - foldline)+1+i] = []
        for x in range(len(dotMap[i])):
            if dotMap[foldline - (len(dotMap) - foldline - 1) + i][x] == "#" or dotMap[len(dotMap)-i-1][x] == "#":
                tempMap[foldline - (len(dotMap) - foldline)+1+i] += "#"
            else:
                tempMap[foldline - (len(dotMap) - foldline) + 1 + i] += "."
    dotMap = tempMap
counter=0
for fold in foldInstructions:
    fold = fold.split('=')
    if fold[0] == "fold along x":
        foldX(int(fold[1]))
    if fold[0] == "fold along y":
        foldY(int(fold[1]))
    if counter == 0:
        for y in range(len(dotMap)):
            for x in range(len(dotMap[y])):
                if dotMap[y][x] == "#":
                    counter+=1
print("The answer for part 1 is:", counter)
print("The answer for part 2 is:")
for i in range(len(dotMap)):
    print(' '.join(dotMap[i]))
f.close()

end = current_milli_time()
print(str(end - start) + "ms")
f.close()
