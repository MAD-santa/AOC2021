import time


def current_milli_time():
    return round(time.time() * 1000)


start = current_milli_time()




# PART 1

def fishSimulator(x):
    if x == 0:
        fishList.append(9)
        return 6
    return x-1
fishList = [4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2]
days = 80
increase = 0
for i in range(days):
    fishList = list(map(fishSimulator, fishList))
print("Rätt 1: ", len(fishList))



# PART 2
singleFish2 = [0]
def fishSimulator2(x):
    if x == 0:
        singleFish2.append(9)
        return 6
    return x-1
fishCounter = {}
days = 128
increase = 0
for startfish in range(9):
    singleFish2 = [startfish]
    for i in range(days):
        singleFish2 = list(map(fishSimulator2, singleFish2))
    match startfish:
        case 0:
            fishCounter[0] = [singleFish2.count(0), singleFish2.count(1), singleFish2.count(2), singleFish2.count(3),
                    singleFish2.count(4), singleFish2.count(5), singleFish2.count(6), singleFish2.count(7),
                    singleFish2.count(8)]
        case 1:
            fishCounter[1] = [singleFish2.count(0), singleFish2.count(1), singleFish2.count(2), singleFish2.count(3),
                    singleFish2.count(4), singleFish2.count(5), singleFish2.count(6), singleFish2.count(7),
                    singleFish2.count(8)]
        case 2:
            fishCounter[2] = [singleFish2.count(0), singleFish2.count(1), singleFish2.count(2), singleFish2.count(3),
                    singleFish2.count(4), singleFish2.count(5), singleFish2.count(6), singleFish2.count(7),
                    singleFish2.count(8)]
        case 3:
            fishCounter[3] = [singleFish2.count(0), singleFish2.count(1), singleFish2.count(2), singleFish2.count(3),
                    singleFish2.count(4), singleFish2.count(5), singleFish2.count(6), singleFish2.count(7),
                    singleFish2.count(8)]
        case 4:
            fishCounter[4] = [singleFish2.count(0), singleFish2.count(1), singleFish2.count(2), singleFish2.count(3),
                    singleFish2.count(4), singleFish2.count(5), singleFish2.count(6), singleFish2.count(7),
                    singleFish2.count(8)]
        case 5:
            fishCounter[5] = [singleFish2.count(0), singleFish2.count(1), singleFish2.count(2), singleFish2.count(3),
                    singleFish2.count(4), singleFish2.count(5), singleFish2.count(6), singleFish2.count(7),
                    singleFish2.count(8)]
        case 6:
            fishCounter[6] = [singleFish2.count(0), singleFish2.count(1), singleFish2.count(2), singleFish2.count(3),
                    singleFish2.count(4), singleFish2.count(5), singleFish2.count(6), singleFish2.count(7),
                    singleFish2.count(8)]
        case 7:
            fishCounter[7] = [singleFish2.count(0), singleFish2.count(1), singleFish2.count(2), singleFish2.count(3),
                    singleFish2.count(4), singleFish2.count(5), singleFish2.count(6), singleFish2.count(7),
                    singleFish2.count(8)]
        case 8:
            fishCounter[8] = [singleFish2.count(0), singleFish2.count(1), singleFish2.count(2), singleFish2.count(3),
                    singleFish2.count(4), singleFish2.count(5), singleFish2.count(6), singleFish2.count(7),
                    singleFish2.count(8)]

fishList = [4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2]
totalfish = 0
for i in range(9):
    if fishList.count(i) > 0:
        singleFish2 = [i]
        for x in range(days):
            singleFish2 = list(map(fishSimulator2, singleFish2))
        for g in singleFish2:
            totalfish+=sum(fishCounter[g])*fishList.count(i)
print("Answer for part2 is: ", totalfish)
end = current_milli_time()
print(str(end - start) + "ms")