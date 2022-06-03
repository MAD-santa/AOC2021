import time


def current_milli_time():
    return round(time.time() * 1000)
start = current_milli_time()


f = open("day18list.txt", "r")
inputData = []
for row in f:
    row = row.replace('\n', '')
    inputData.append(row)
one = []
first = "global one; one = "+inputData[0]
exec(first)
two = []
second = "global two; two = "+inputData[1]
exec(second)
afterAdd = []
afterAdd = [one]+[two]




deepest = []
maxdepth = 0
bef = 0
aftFound = 0
def digDeeper(nest,lvl,id):
    global afterAdd
    global deepest
    global maxdepth
    idlocal1 = id.copy()
    idlocal0 = id.copy()
    if isinstance(nest[0], list):
        idlocal0.append(0)
        if lvl > maxdepth:
            maxdepth = lvl
            deepest = []
            deepest = idlocal0.copy()
        digDeeper(nest[0],lvl+1,idlocal0)
    if isinstance(nest[1], list):
        idlocal1.append(1)
        if lvl > maxdepth:
            maxdepth = lvl
            deepest = idlocal1.copy()
        digDeeper(nest[1],lvl+1,idlocal1)
    return maxdepth,deepest

def findExplotion(nest):
    global id
    global deepest
    global maxdepth
    id = []
    deepest = []
    maxdepth = 0
    return digDeeper(nest, 0, id)
def findBefInt(nest,lvl,id,compare):
    global intBef
    global intAft
    global aftFound
    localcompare0 = compare.copy()
    localcompare1 = compare.copy()
    localcompare1.append(1)
    localcompare0.append(0)
    idlocal1 = id.copy()
    idlocal0 = id.copy()
    if isinstance(nest[0], int):

        idlocal0.append(0)

        if idlocal0 < compare:
            intBef = [nest[0], idlocal0]

        if idlocal0 > localcompare0:
            if aftFound == 0:
                intAft = [nest[0], idlocal0]
                aftFound = 1
            if aftFound == 1:
                if idlocal0 < intAft[1]:
                    intAft = [nest[0], idlocal0]

    if isinstance(nest[1], int):

        idlocal1.append(1)

        if idlocal1 < compare:

            intBef = [nest[1], idlocal1]
        if idlocal1 > localcompare1:
            if aftFound == 0:
                intAft = [nest[1], idlocal1]
                aftFound = 1
            if aftFound == 1:
                if idlocal1 < intAft[1]:
                    intAft = [nest[1], idlocal1]
    if isinstance(nest[0], list):
        idlocal0.append(0)
        findBefInt(nest[0], lvl + 1, idlocal0,compare)
    if isinstance(nest[1], list):
        idlocal1.append(1)
        findBefInt(nest[1], lvl + 1, idlocal1,compare)

def findFirstInt(nest,lvl,id):
    global intfound
    global firstInt
    idlocal1 = id.copy()
    idlocal0 = id.copy()
    if isinstance(nest[0], int) and nest[0] > 9:
        idlocal0.append(0)
        intfound.append([nest[0],idlocal0])
        firstInt = [nest[0],idlocal0]
    if isinstance(nest[1], int)and nest[1] > 9:

        idlocal1.append(1)
        intfound.append([nest[1],idlocal1])
        firstInt = [nest[1],idlocal1]
    if isinstance(nest[0], list):
        idlocal0.append(0)
        findFirstInt(nest[0], lvl + 1, idlocal0)
    if isinstance(nest[1], list):
        idlocal1.append(1)
        findFirstInt(nest[1], lvl + 1, idlocal1)

test = ""
def findInt(nest,exploded):
    global test
    global intBef
    global intAft
    global aftFound
    aftFound = 0
    intBef = []
    intAft = []
    id = []
    indexExpl = ""
    expl = exploded.copy()
    if expl[len(expl)-1] == 0:
        expl[len(expl) - 1] = 1
        for x in expl:
            indexExpl = indexExpl + '[' + str(x) + ']'
        run = "global test; test = afterAdd"+indexExpl
        exec(run)
        if isinstance(test,int):
            intAft = [test, expl]
            aftFound = 1
    findBefInt(nest, 0, id, exploded)
    return [intBef,exploded,intAft]
firstInt = []
intfound = []


def takeSecond(elem):
    return elem[1]
def split(nest):
    id = []
    global firstInt
    global intfound
    global afterAdd
    global splitint
    firstInt = []
    intfound = []
    findFirstInt(nest, 0, id)

    intfound.sort(key=takeSecond)
    if len(intfound) > 1:
        firstInt = intfound[0]
    if len(firstInt) > 1:
        intIndex = ""
        try:
            for i in firstInt[1]:
                intIndex = intIndex + '[' + str(i) + ']'

        except:
            pass
        specialAdd = afterAdd.copy()
        intIndex = "specialAdd" + intIndex
        test2 = "global splitint; splitint=["+intIndex+"// 2,-(-"+intIndex+" // 2)]"
        exec(test2)
        splitint = "= "+str(splitint)
        test3 = str(intIndex+splitint)
        exec(test3)
        afterAdd=specialAdd.copy()
        return True
    else:
        return False
splitint = ""
def explotion(array):
    global afterAdd
    iB = array[0]
    expl = array[1]
    iA = array[2]
    indexIb = ""
    try:
        for i in iB[1]:
            indexIb = indexIb+'['+str(i)+']'
    except:
        pass
    indexExpl = ""
    for x in expl:
        indexExpl = indexExpl + '[' + str(x) + ']'
    indexAft = ""
    try:
        for z in iA[1]:
            indexAft = indexAft + '[' + str(z) + ']'
    except:
        pass
    if len(indexIb) > 0:
        addbef = "afterAdd"+indexIb+"+=afterAdd"+indexExpl+"[0]"
        exec(addbef)
    if len(indexAft) > 0:
        addaft = "afterAdd"+indexAft+"+=afterAdd"+indexExpl+"[1]"
        exec(addaft)
    removeexpl = "afterAdd"+indexExpl+"=0"
    exec(removeexpl)


for i in range(len(inputData)-1):
    while True:
        changes = 0
        while findExplotion(afterAdd)[0] > 2:
            explotion(findInt(afterAdd,findExplotion(afterAdd)[1]))
            changes+=1
        if split(afterAdd):
            changes+=1
        if changes == 0:
            break
    if i+2 < len(inputData):
        two = []
        nextrow = "global two; two = "+inputData[i+2]
        exec(nextrow)
        one = afterAdd.copy()
        afterAdd = []
        afterAdd = [one]+[two]

finalsum = afterAdd.copy()


def magcalc(nest):
    if isinstance(nest[0],list):
        nest[0] = magcalc(nest[0])

    if isinstance(nest[1],list):
        nest[1] = magcalc(nest[1])

    if isinstance(nest[0],int) and isinstance(nest[1],int):
        left = nest[0]*3
        right = nest[1]*2
        return left+right


magnitude = magcalc(finalsum)

print(f"The answer for part 1 is {magnitude}")

end = current_milli_time()
print(str(end - start) + "ms")
f.close()