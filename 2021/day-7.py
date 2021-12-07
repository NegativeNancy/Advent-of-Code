from statistics import median
from util import get_int_input


def solution1(data):
    numbers = list()
    for i in data:
        numbers.append(int(i))

    level = int(median(numbers))

    totalFuelUsed = 0
    for number in data:
        fuelUsed = 0
        if int(number) > level:
            fuelUsed = int(number) - level
            totalFuelUsed += fuelUsed
        elif int(number) < level:
            fuelUsed = level - int(number)
            totalFuelUsed += fuelUsed
        print('Move from %i to %i: %i' % (int(number), level, fuelUsed))
    print('Total Fuel used:', totalFuelUsed)


def solution2(data):
    numbers = list(map(int, data))

    totalFuelUsed = 0
    level = 0
    for n in range(min(numbers), max(numbers)):
        fuelUsed = 0
        for number in numbers:
            fuel = 0
            for i in range(1, abs(n - number) + 1):
                fuel += i
            fuelUsed += fuel
        if (totalFuelUsed == 0) or (fuelUsed < totalFuelUsed):
            totalFuelUsed = fuelUsed
            level = n
    print('Total Fuel used:', totalFuelUsed, 'to reach level', level)


def main():
    # data = get_int_input("test-data.txt")
    data = get_int_input("input-d7.txt")
    dataInt = data[0]
    solution1(dataInt)
    solution2(dataInt)


if __name__ == '__main__':
    main()
