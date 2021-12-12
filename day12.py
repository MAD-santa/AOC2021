import time
def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day12list.txt", "r")
pathConnections = {}
for row in f:
    row = row.replace('\n', '')
    row = row.split('-')
    if row[0] in pathConnections.keys():
        pathConnections[row[0]] += [row[1]]
    else:
        pathConnections[row[0]] = [row[1]]
    if row[1] in pathConnections.keys():
        pathConnections[row[1]] += [row[0]]
    else:
        pathConnections[row[1]] = [row[0]]
# PART 1
pathList = []
def findWay(cave, visited):
    if cave in pathConnections.keys():
        newvisit = [*visited]
        newvisit+=[cave]
        for nextCave in pathConnections[cave]:
            if nextCave != "start" and nextCave != "end":
                if nextCave.islower():
                    if nextCave not in newvisit:
                        findWay(nextCave,newvisit)
                if nextCave.isupper():
                    findWay(nextCave, newvisit)
            if nextCave == "end":
                newvisit += ["end"]
                pathList.append(newvisit)
findWay("start",[])
print("Answer for part one is: ", len(pathList))


# PART 2
pathList = []
def findWay(cave, visited,smallcave):
    if cave in pathConnections.keys():
        newvisit = [*visited]
        newvisit+=[cave]
        for nextCave in pathConnections[cave]:
            if nextCave != "start" and nextCave != "end":
                if nextCave.islower():
                    if nextCave not in newvisit:
                        findWay(nextCave,newvisit,smallcave)
                    if nextCave in newvisit:
                        if newvisit.count(nextCave) < 2 and smallcave == 0:
                            findWay(nextCave, newvisit, 1)
                if nextCave.isupper():
                    findWay(nextCave, newvisit,smallcave)
            if nextCave == "end":
                newvisit += ["end"]
                pathList.append(newvisit)
findWay("start",[],0)

print("Answer for part two is: ", len(pathList))
f.close()
end = current_milli_time()
print(str(end - start) + "ms")
f.close()
