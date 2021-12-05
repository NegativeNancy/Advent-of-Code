def get_input(filename):
    inputFile = "2021/input/" + filename
    with open(inputFile) as fhand:
        data = [line.strip() for line in fhand]
    return data


def get_int_input(filename):
    inputFile = "2021/input/" + filename
    with open(inputFile) as fhand:
        data = [int(line.strip()) for line in fhand]
    return data