import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day4list.txt", "r")
bingonumbers = [67,31,58,8,79,18,19,45,38,13,40,62,85,10,21,96,56,55,4,36,76,42,32,34,39,89,6,12,24,57,93,47,41,52,83,61,5,37,28,15,86,23,69,92,70,27,25,53,44,80,65,22,99,43,66,26,11,72,2,98,14,82,87,20,73,46,35,7,1,84,95,74,81,63,78,94,16,60,29,97,91,30,17,54,68,90,71,88,77,9,64,50,0,49,48,75,3,59,51,33]
bingoboard = []
tempboard = []
for row in f:
    row = row.strip()
    row = row.replace('  ', ' ')
    if row == '':
        bingoboard.append(tempboard)
        tempboard = []
        continue
    row = row.split(' ')
    tempboard.append(row)
bingoboard.append(tempboard)

# PART 1
def whenWillItWin(board):
    lowesthighkey = 10000000
    unmarkedSum = 0
    for row in bingoboard[board]:
        highestkey = 0
        matches = 0
        for number in row:
            if int(number) in bingonumbers:
                matches += 1
                if highestkey < bingonumbers.index(int(number)):
                    highestkey = bingonumbers.index(int(number))
            if matches == 5:
                if lowesthighkey > highestkey:
                    lowesthighkey = highestkey
    for col in zip(*reversed(bingoboard[board])):
        highestkey = 0
        matches = 0
        for number in col:
            if int(number) in bingonumbers:
                matches += 1
                if highestkey < bingonumbers.index(int(number)):
                    highestkey = bingonumbers.index(int(number))
            if matches == 5:
                if lowesthighkey > highestkey:
                    lowesthighkey = highestkey
    return lowesthighkey
lowestWin=[]
for i in range(len(bingoboard)):
    lowestWin.append(whenWillItWin(i))

unmarkedSum = 0
for row in bingoboard[lowestWin.index(min(lowestWin))]:
    for number in row:
        if int(number) not in bingonumbers[:lowestWin[lowestWin.index(min(lowestWin))]+1]:
            unmarkedSum+=int(number)
print("The answer is:", unmarkedSum*bingonumbers[lowestWin[lowestWin.index(min(lowestWin))]])

#part 2
unmarkedSum = 0
for row in bingoboard[lowestWin.index(max(lowestWin))]:
    for number in row:
        if int(number) not in bingonumbers[:lowestWin[lowestWin.index(max(lowestWin))]+1]:
            unmarkedSum+=int(number)
print("The answer is:", unmarkedSum*bingonumbers[lowestWin[lowestWin.index(max(lowestWin))]])
f.close()
end = current_milli_time()
print(str(end - start) + "ms")
f.close()

