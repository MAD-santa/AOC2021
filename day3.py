import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()

f = open("day3list.txt", "r")
report = []
for row in f:
    row = row.replace('\n', '')
    report.append(row)

# PART 1
gammaRate = ""
epsilonRate = ""
for col in range(len(report[0])):
    one = 0
    zero = 0
    for row in report:
        match int(row[col]):
            case 0:
                zero += 1
            case 1:
                one += 1
    if one > zero:
        gammaRate += "1"
        epsilonRate += "0"
    elif zero > one:
        gammaRate += "0"
        epsilonRate += "1"

print(int(epsilonRate, 2) * int(gammaRate, 2))

# PART 2
OGRating = [*report]
for col in range(len(OGRating[0])):
    one = 0
    zero = 0
    tempOne = []
    tempZero = []
    if len(OGRating) > 1:
        for row in OGRating:
            match int(row[col]):
                case 0:
                    zero += 1
                    tempZero.append(row)
                case 1:
                    one += 1
                    tempOne.append(row)
        if one >= zero:
           OGRating = [*tempOne]
        elif zero > one:
            OGRating = [*tempZero]
CSRating = [*report]
for col in range(len(CSRating[0])):
    one = 0
    zero = 0
    tempOne = []
    tempZero = []
    if len(CSRating) > 1:
        for row in CSRating:
            match int(row[col]):
                case 0:
                    zero += 1
                    tempZero.append(row)
                case 1:
                    one += 1
                    tempOne.append(row)
        if one < zero:
           CSRating = [*tempOne]
        elif zero <= one:
            CSRating = [*tempZero]
print(int(OGRating[0], 2) * int(CSRating[0], 2))
f.close()
end = current_milli_time()
print(str(end - start) + "ms")
f.close()
