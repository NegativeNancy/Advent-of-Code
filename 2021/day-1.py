def get_input(filename):
    inputFile = "input/" + filename
    with open(inputFile) as fhand:
        data = [int(line.strip()) for line in fhand]
    return data


def count_larger(data):
    data_l, previous, total, counter = len(data), data[0], 0, 0

    while counter < data_l:
        if data[counter] > previous:
            previous, total, counter = (data[counter]), (total + 1), (counter + 1)
        else:
            previous, counter = (data[counter]), (counter + 1)
    return total


def calculate_sum(data):
    data_l, counter, total = len(data), 0, list()

    while counter < (data_l - 2):
        v1, v2, v3 = (data[counter]), (data[counter + 1]), (data[counter + 2])
        total.append(v1 + v2 + v3)
        counter += 1
    return total


def solution1(data):
    total = count_larger(data)    
    print(total, "measurments are larger than the previous")


def solution2(data):
    total = count_larger(calculate_sum(data))
    print(total, "sums are larger than the previous")

if __name__ == '__main__':
    # data = get_input("test-data.txt")
    data = get_input("input-d1.txt")
    solution1(data)
    solution2(data)
