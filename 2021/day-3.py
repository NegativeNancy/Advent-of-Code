from util import get_input

def get_fequent_bit(data, binary_c, len_d):
    mostFrequent, leastFrequent, data_c, numList = '', '', 0, []

    while data_c < len_d:
        binary = data[data_c]
        numList.append(binary[binary_c])
        data_c += 1
    mostFrequent += (max(sorted(set(numList), reverse=True), key=numList.count))
    leastFrequent += (min(sorted(set(numList)), key=numList.count))
    
    return mostFrequent, leastFrequent


def solution1(data):
    len_d, len_b = len(data), len(data[0])    
    binary_c = 0
    gamma, epsilon = '', ''

    while binary_c < len_b:
        mfb, lfb = get_fequent_bit(data, binary_c, len_d)
        gamma += mfb
        epsilon += lfb
        binary_c += 1
   
    print("Gamma:", gamma, " Epsilon:", epsilon)
    print("Gamma:", int(gamma, 2), " Epsilon:", int(epsilon, 2))
    print("Consumption of submarine:", (int(gamma, 2) * int(epsilon, 2)))
            

def solution2(data):
    len_d, len_b = len(data), len(data[0])    
    binary_c = 0
    data_1, data_0 = data, data

    while binary_c < len_b:
        mfb, lfb = get_fequent_bit(data_1, binary_c, len_d)
        data_temp = []
        for x in data_1:
            if x[binary_c] == mfb:
                data_temp.append(x)
        data_1 = data_temp
        binary_c += 1
        len_d = len(data_1)
    oxygen = data_1[0]
    
    binary_c = 0
    while binary_c < len_b:
        mfb, lfb = get_fequent_bit(data_0, binary_c, len_d)
        data_temp = []
        for x in data_0:
            if x[binary_c] == lfb:
                data_temp.append(x)
        data_0 = data_temp
        binary_c += 1
        len_d = len(data_0)
    co2 = data_0[0]
    
    print("Oxygen:", oxygen, " CO2:", co2)
    print("Oxygen:", int(oxygen, 2), " CO2:", int(co2, 2))
    print("Lifesupport rating:", (int(oxygen, 2) * int(co2, 2)))
   

def main():
    # data = get_input("test-data.txt")
    data = get_input("input-d3.txt")
    solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
