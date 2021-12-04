def get_input(filename):
    inputFile = "2021/input/" + filename
    with open(inputFile) as fhand:
        data = [line.strip() for line in fhand]
    return data


def get_fequency(data):
    len_d, len_b = len(data), len(data[0])
    binary_c = 0
    mostFrequent, leastFrequent = '', ''

    while binary_c < len_b:
        data_c = 0
        numList = []
        while data_c < len_d:
            binary = data[data_c]
            numList.append(binary[binary_c])
            data_c += 1
        mostFrequent += (max(set(numList), key=numList.count))
        leastFrequent += (min(set(numList), key=numList.count))
        binary_c += 1
    
    return mostFrequent, leastFrequent


def solution1(data):
    gamma, epsilon = get_fequency(data)
    
    print("Gamma: ", gamma, " Epsilon: ", epsilon)
    print("Gamma: ", int(gamma, 2), " Epsilon: ", int(epsilon, 2))
    print("Consumption of submarine: ", (int(gamma, 2) * int(epsilon, 2)))
            

def solution2(data):
    pass


if __name__ == '__main__':
    # data = get_input("test-data.txt")
    data = get_input("input-d3.txt")
    solution1(data)
    solution2(data)