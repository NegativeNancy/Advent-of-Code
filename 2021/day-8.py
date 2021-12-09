from util import get_input


def solution1(data):
    numbersList = []
    for line in data:
        signalPatterns, signalNumbers = line.split('|')
        numbersList.append(signalNumbers.split())

    numbers = {1: 0, 4: 0, 7: 0, 8: 0}

    for number in numbersList:
        for item in number:
            if len(item) == 2:
                numbers[1] += 1
            elif len(item) == 4:
                numbers[4] += 1
            elif len(item) == 3:
                numbers[7] += 1
            elif len(item) == 7:
                numbers[8] += 1
    print('Total of easy numbers:', (numbers[1] + numbers[4] + numbers[7] +
          numbers[8]))


def solution2(data):
    total = 0
    for line in data:
        signalPatterns, signalNumbers = line.split('|')
        numbersList = [''.join(sorted(x)) for x in signalNumbers.split()]
        patternList = [''.join(sorted(x)) for x in signalPatterns.split()]

        patternToNumber = {}
        numberToPattern = {}

        for pattern in patternList:
            if len(pattern) == 2:
                patternToNumber[1] = pattern
                numberToPattern[pattern] = 1
            elif len(pattern) == 3:
                patternToNumber[7] = pattern
                numberToPattern[pattern] = 7
            elif len(pattern) == 4:
                patternToNumber[4] = pattern
                numberToPattern[pattern] = 4
            elif len(pattern) == 7:
                patternToNumber[8] = pattern
                numberToPattern[pattern] = 8

        for pattern in patternList:
            if len(pattern) == 5 and all([x in pattern for x in patternToNumber[7]]):
                patternToNumber[3] = pattern
                numberToPattern[pattern] = 3

        for pattern in patternList:
            if len(pattern) == 6 and all([x in pattern for x in patternToNumber[3]]):
                patternToNumber[9] = pattern
                numberToPattern[pattern] = 9

        for letter in list('abcdefg'):
            if len([pattern for pattern in patternList if letter in pattern]) == 9:
                notInNumberTwo = letter

        for pattern in patternList:
            if len(pattern) == 5 and notInNumberTwo not in pattern:
                patternToNumber[2] = pattern
                numberToPattern[pattern] = 2

        for pattern in patternList:
            if len(pattern) == 5 and pattern not in numberToPattern.keys():
                patternToNumber[5] = pattern
                numberToPattern[pattern] = 5

        for pattern in patternList:
            if len(pattern) == 6 and all([x in pattern for x in patternToNumber[7]]) and pattern not in numberToPattern.keys():
                patternToNumber[0] = pattern
                numberToPattern[pattern] = 0

        for pattern in patternList:
            if len(pattern) == 6 and pattern not in numberToPattern.keys():
                patternToNumber[6] = pattern
                numberToPattern[pattern] = 6

        number = ''
        for pattern in numbersList:
            number += str(numberToPattern[pattern])
        total += int(number)
    print('Sum of all values =', total)


def main():
    # data = get_input("test-data.txt")
    data = get_input("input-d8.txt")
    solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
