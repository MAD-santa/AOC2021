import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day8list.txt", "r")
signalPatternList = []
for row in f:
    row = row.replace('\n', '')
    row = row.split(' | ')
    signalPattern = row[0].split(' ')
    outputValue = row[1].split(' ')
    listentry = signalPattern+outputValue
    signalPatternList += [listentry]
f.close()



# PART 1
counter = 0
for signal in signalPatternList:
    for x in range(4):
        unique = 0
        digitLength = len(signal[x+10])
        for i in range(10):
            if len(signal[i]) == digitLength:
                unique+=1
        if unique == 1:
            counter+=1
print("Part one: ", counter)


# PART 2
summa = 0
for row in signalPatternList:
    for i in range(10):
        pattern = row[i]
        match len(pattern):
            case 2:
                one = set(pattern)
            case 3:
                seven = set(pattern)
            case 4:
                four = set(pattern)
            case 7:
                eight = set(pattern)
    for i in range(10):
        pattern = row[i]
        match len(pattern):
            case 6:
                match len(set(pattern)-one):
                    case 5:
                        six = set(pattern)
                    case 4:
                        match len(set(pattern) - four):
                            case 2:
                                nine = set(pattern)
                            case 3:
                                zero = set(pattern)
            case 5:
                match len(set(pattern) - one):
                    case 3:
                        three = set(pattern)
                    case 4:
                        match len(set(pattern) - four):
                            case 2:
                                five = set(pattern)
                            case 3:
                                two = set(pattern)
    output = ''
    for i in range(4):
        pattern = row[i+10]
        if set(pattern) == zero:
            output+='0'
        if set(pattern) == one:
            output+='1'
        if set(pattern) == two:
            output+='2'
        if set(pattern) == three:
            output+='3'
        if set(pattern) == four:
            output+='4'
        if set(pattern) == five:
            output+='5'
        if set(pattern) == six:
            output+='6'
        if set(pattern) == seven:
            output+='7'
        if set(pattern) == eight:
            output+='8'
        if set(pattern) == nine:
            output+='9'
    summa+=int(output)
print("Part 2 answer is: ", summa)


end = current_milli_time()
print(str(end - start) + "ms")
