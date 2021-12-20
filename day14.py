import time

def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day14list.txt", "r")
insertionRules = {}
insertionRules2 = []
for row in f:
    row = row.replace('\n', '')
    row = row.split(' -> ')
    insertionRules[row[0]] = row[1]
    insertionRules2.append(row)

# PART 1
polymerTemplate = "FSKBVOSKPCPPHVOPVFPC"
startstring = polymerTemplate
ptPairList = {}


for g in range(10):
    ptPairList = {}
    key = ''
    joined = ''
    newstring = ''
    for i in range(len(polymerTemplate)-1):
        key = ''.join([polymerTemplate[i], polymerTemplate[i + 1]])
        for insert in insertionRules2:
            if str(insert[0]) == key:
                newstring += polymerTemplate[i]+insert[1]
    newstring+=polymerTemplate[i + 1]
    polymerTemplate = newstring
newstring = polymerTemplate[:len(polymerTemplate)-1]

stringList = []
maxElement = 0
minElement = 99999999999999
for i in range(len(newstring)):
    if newstring.count(newstring[i]) > maxElement:
       maxElement = newstring.count(newstring[i])
    if newstring.count(newstring[i]) < minElement:
        minElement = newstring.count(newstring[i])

print("The answer for part 1 is: ", maxElement-minElement)
end = current_milli_time()
print(str(end - start) + "ms")

# PART 2

polymerTemplate = "FSKBVOSKPCPPHVOPVFPC"
pairCounter = {a: 0 for a in insertionRules.keys()}
for i in range(len(polymerTemplate)-1):
    pairCounter[polymerTemplate[i:i+2]]+=1

tempPairCounter = pairCounter.copy()

for _ in range(40):
    for pair in pairCounter:
        if pairCounter[pair] > 0:
            tempPairCounter[pair[0]+insertionRules[pair]]+=1*pairCounter[pair]
            tempPairCounter[insertionRules[pair]+pair[1]]+=1*pairCounter[pair]
            tempPairCounter[pair]-=1*pairCounter[pair]
    pairCounter=tempPairCounter.copy()


testcount = 0
counters = {}
for pair in pairCounter:
    if pairCounter[pair] > 0:
        testcount+=pairCounter[pair]
    if pair[0] in counters.keys():
        counters[pair[0]]+=pairCounter[pair]
    else:
        counters[pair[0]] = pairCounter[pair]
counters[polymerTemplate[len(polymerTemplate)-1]]+=1
maxElement = 0
minElement = 9999999999999
for letter in counters:
    if maxElement < counters[letter]:
        maxElement = counters[letter]
    if minElement > counters[letter]:
        minElement = counters[letter]

print("The answer for part 2 is:", maxElement-(minElement))

end2 = current_milli_time()
print(str(end2 - end) + "ms")
f.close()


