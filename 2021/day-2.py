def get_input(filename):
    inputFile = "input/" + filename
    with open(inputFile) as fhand:
        data = [line.strip() for line in fhand]
    return data


def get_postion(data):
    movement, steps = data.split()
    return movement, int(steps)
    

def solution1(data):
    data_l = len(data)
    c, horizontal, depth = 0, 0, 0

    while c < data_l:
        movement, steps = get_postion(data[c])
        if (movement == 'forward'):
            horizontal, c = (horizontal + steps), (c + 1)
        elif (movement == 'down'):
            depth, c = (depth + steps), (c + 1)
        elif (movement == 'up'):
            depth, c = (depth - steps), (c + 1)
        else:
            print("Invalid movement detected")

    final_calc = horizontal * depth
    print("Solution 1 caluclation: ", final_calc)

def solution2(data):
    pass


def main():
    # data = get_input("test-data.txt")
    data = get_input("input-d2.txt")
    solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
