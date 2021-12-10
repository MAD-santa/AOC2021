import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day10list.txt", "r")
syntaxList = []
incompleteList = []
for row in f:
    row = row.replace('\n', '')
    syntaxList.append(row)

# PART 1
def checkCorrupt(x):
    brackets = 0  # []
    anglebrackets = 0  # <>
    parentheses = 0  # ()
    braces = 0 #{}
    startChar = str(row[x])
    for i in range(x):
        match str(row[x-1-i]):
            case "]":
                brackets += 1
            case ">":
                anglebrackets += 1
            case ")":
                parentheses += 1
            case "}":
                braces += 1
            case "[":
                if brackets == 0:
                    if startChar == "]":
                        return True
                    else:
                        return False
                else:
                    brackets -= 1
            case "<":
                if anglebrackets == 0:
                    if startChar == ">":
                        return True
                    else:
                        return False
                else:
                    anglebrackets -= 1
            case "(":
                if parentheses == 0:
                    if startChar == ")":
                        return True
                    else:
                        return False
                else:
                    parentheses -= 1
            case "{":
                if braces == 0:
                    if startChar == "}":
                        return True
                    else:
                        return False
                else:
                    braces -= 1
syntaxErrorScore = 0
for row in syntaxList:
    brackets = 0  # []
    anglebrackets = 0  # <>
    parentheses = 0  # ()
    braces = 0 #{}
    for x in range(len(row)):
        match str(row[x]):
            case "[":
                brackets+=1
            case "<":
                anglebrackets+=1
            case "(":
                parentheses+=1
            case "{":
                braces+=1
            case "]":
                if checkCorrupt(x) == False:
                    syntaxErrorScore+=57
                    break
                else:
                    brackets-=1
            case ">":
                if checkCorrupt(x) == False:
                    syntaxErrorScore+=25137
                    break
                else:
                    anglebrackets-=1
            case ")":
                if checkCorrupt(x) == False:
                    syntaxErrorScore+=3
                    break
                else:
                    parentheses-=1
            case "}":
                if checkCorrupt(x) == False:
                    syntaxErrorScore+=1197
                    break
                else:
                    braces-=1
        if x == len(row)-1:
            incompleteList.append(row)
print("Answer for part 1 is: ", syntaxErrorScore)

#Part 2
def autoComplete(line):
    completion = ''
    brackets = 0  # []
    anglebrackets = 0  # <>
    parentheses = 0  # ()
    braces = 0 #{}
    for i in range(len(line)):
        match str(line[len(line)-i-1]):
            case "]":
                brackets += 1
            case ">":
                anglebrackets += 1
            case ")":
                parentheses += 1
            case "}":
                braces += 1
            case "[":
                if brackets == 0:
                    completion+=']'
                else:
                    brackets -= 1
            case "<":
                if anglebrackets == 0:
                    completion+='>'
                else:
                    anglebrackets -= 1
            case "(":
                if parentheses == 0:
                    completion+=')'
                else:
                    parentheses -= 1
            case "{":
                if braces == 0:
                    completion+='}'
                else:
                    braces -= 1
    return completion
completionStrings = []
for row in incompleteList:
    completionStrings.append(autoComplete(row))

scoreList = []
for row in completionStrings:
    score = 0
    for x in range(len(row)):
        match row[x]:
            case "]":
                value = 2
            case ")":
                value = 1
            case "}":
                value = 3
            case ">":
                value = 4
        score = score*5+value
    scoreList.append(score)

scoreList.sort()
print("The answer for part 2 is: ", scoreList[len(scoreList)//2])
f.close()
end = current_milli_time()
print(str(end - start) + "ms")
f.close()
