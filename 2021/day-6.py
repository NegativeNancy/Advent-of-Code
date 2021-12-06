from util import get_input


def get_fishes(data):
    days = []
    for n in data:
        day = n.split(',')
    for d in day:
        days.append(int(d))
    return days


def count_fish(daysOld, daysToCount):
    c = 0

    while c < daysToCount:
        # print("Calculating day:", c)
        daysNew = []
        fishToAdd = 0
        for day in daysOld:
            if (day > 0):
                daysNew.append((day) - 1)
            elif (day == 0):
                daysNew.append(6)
                fishToAdd += 1

        fish = 0
        while fish < fishToAdd:
            daysNew.append(8)
            fish += 1

        daysOld = daysNew
        c += 1
    return daysOld


def solution1(data):
    daysToCount = 80
    totalFish = count_fish(get_fishes(data), daysToCount)
    print("Total fish after %i:" % daysToCount, len(totalFish))


def solution2(data):
    daysToCount = 256
    fishes = get_fishes(data)

    numberAmount = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for f in fishes:
        numberAmount[f] += 1
    for f in range(daysToCount):
        newNumberAmount = {}
        newNumberAmount[0] = numberAmount[1]
        newNumberAmount[1] = numberAmount[2]
        newNumberAmount[2] = numberAmount[3]
        newNumberAmount[3] = numberAmount[4]
        newNumberAmount[4] = numberAmount[5]
        newNumberAmount[5] = numberAmount[6]
        newNumberAmount[6] = numberAmount[7] + numberAmount[0]
        newNumberAmount[7] = numberAmount[8]
        newNumberAmount[8] = numberAmount[0]
        numberAmount = newNumberAmount

    print("Total fish after %i:" % daysToCount, sum(newNumberAmount.values()))


def main():
    # data = get_input("test-data.txt")
    data = get_input("input-d6.txt")
    solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
