import time
import math


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day15list.txt", "r")
riskMap = {}
y=0
for row in f:
    row = row.replace('\n', '')
    x=0
    for col in row:
        riskMap[y,x] = int(col)
        x+=1
    y+=1
removeList = []
lowestsofar = 0
# PART 1
def findRouteRisk():
    global lowestRisk
    global lowestsofar
    riskUpdates = {}
    for row in lowestRisk:
        if not lowestRisk[row] < lowestsofar:
            for i in range(4):
                match i:
                    case 0:
                        y = row[0]+1
                        x = row[1]
                    case 1:
                        y = row[0]
                        x = row[1]+1
                    case 2:
                        y = row[0]-1
                        x = row[1]
                    case 3:
                        y = row[0]
                        x = row[1]-1

                if (y, x) in riskMap:
                    if (y, x) in lowestRisk:
                        if lowestRisk[y, x] > lowestRisk[row]+riskMap[y, x]:
                            if (y, x) in riskUpdates:
                                if riskUpdates[y, x] > lowestRisk[row] + riskMap[y, x]:
                                    riskUpdates[y, x] = lowestRisk[row] + riskMap[y, x]
                            else:
                                riskUpdates[y,x] = lowestRisk[row] + riskMap[y, x]
                    else:
                        if (y, x) in riskUpdates:
                            if riskUpdates[y, x] > lowestRisk[row] + riskMap[y, x]:
                                riskUpdates[y, x] = lowestRisk[row] + riskMap[y, x]
                        else:
                            riskUpdates[y, x] = lowestRisk[row] + riskMap[y, x]
    if len(riskUpdates) == 0:
        return False
    lowestsofar = riskUpdates[min(riskUpdates.keys(), key=(lambda k: riskUpdates[k]))]
    lowestRisk.update(riskUpdates)

lowestRisk = {}
lowestRisk[0,0] = 0
while True:
    if findRouteRisk() == False:
        break


corner = int(math.sqrt(len(lowestRisk))-1)

print("The answer for part 1 is:", lowestRisk[corner,corner])
end1 = current_milli_time()
print(str(end1 - start) + "ms")

# PART 2
corner = int(math.sqrt(len(riskMap)))

newrisk = riskMap.copy()
for risk in riskMap:
    if  riskMap[risk] == 9:
        newvalue = 1
    else:
        newvalue = riskMap[risk]+1
    for i in range(4):
        multiplier = i+1
        newrisk[risk[0], risk[1]+corner*multiplier] = int(newvalue)
        if newvalue == 9:
            newvalue = 1
        else:
            newvalue+=1
riskMap = newrisk.copy()
for risk in riskMap:
    if  riskMap[risk] == 9:
        newvalue = 1
    else:
        newvalue = riskMap[risk]+1
    for i in range(4):
        multiplier = i+1
        newrisk[risk[0]+corner*multiplier, risk[1]] = newvalue
        if newvalue == 9:
            newvalue = 1
        else:
            newvalue+=1


riskMap = {}
riskMap = newrisk.copy()
lowestRisk = {}
lowestRisk[0,0] = 0
lowestsofar = 0
while True:
    if findRouteRisk() == False:
        break
corner = int(math.sqrt(len(lowestRisk))-1)
print("The answer for part 2 is:", lowestRisk[corner,corner])
end = current_milli_time()
print(str(end - start) + "ms")
f.close()
