def get_input(filename):
    inputFile = "input/" + filename
    with open(inputFile) as fhand:
        data = [line.strip() for line in fhand]
    return data


def get_postion(data):
    movement, steps = data.split()
    return movement, int(steps)
    

def calculate_aim(movement, step, aim):
    if movement == 'up':
        return (aim - step)
    else:
        return (aim + step)


def solution1(data):
    data_l = len(data)
    c, horizontal, depth = 0, 0, 0

    while c < data_l:
        movement, steps = get_postion(data[c])
        if (movement == 'forward'):
            horizontal, c = (horizontal + steps), (c + 1)
        elif (movement == 'down'):
            depth, c = (depth + steps), (c + 1)
        else:
            depth, c = (depth - steps), (c + 1)

    final_calc = horizontal * depth
    print("Solution 1 caluclation: ", final_calc)

def solution2(data):
    data_l = len(data)
    c, horizontal, depth, aim = 0, 0, 0, 0

    while c < data_l:
        movement, steps = get_postion(data[c])
        if (movement == 'down'):
            aim, c = calculate_aim(movement, steps, aim), (c + 1)
        elif (movement == 'up'):            
            aim, c = calculate_aim(movement, steps, aim), (c + 1)
        else: 
            horizontal, c = (horizontal + steps), (c + 1)
            depth = depth + (steps * aim)
        
    final_calc = horizontal * depth
    print("Solution 2 caluclation: ", final_calc)
            

def main():
    # data = get_input("test-data.txt")
    data = get_input("input-d2.txt")
    solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
