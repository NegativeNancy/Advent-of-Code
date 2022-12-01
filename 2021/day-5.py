from util import get_input
from collections import defaultdict


def get_cords(line):
    cord_a, cord_b = line.split('->')
    a_x, a_y = cord_a.split(',')
    b_x, b_y = cord_b.split(',')
    return int(a_x), int(a_y), int(b_x), int(b_y)


def horizon_vertical(a_x, a_y, b_x, b_y, vents_loc, solution):
    if a_x == b_x:
        for i in range(min(a_y, b_y), max(a_y, b_y) + 1):
            vents_loc[(a_x, i)] += 1
    elif a_y == b_y:
        for i in range(min(a_x, b_x), max(a_x, b_x) + 1):
            vents_loc[(i, a_y)] += 1
    elif solution == 2:
        diagonal(a_x, a_y, b_x, b_y, vents_loc)
    return vents_loc


def diagonal(a_x, a_y, b_x, b_y, vents_loc):
    c_x = (1 if a_x < b_x else -1)
    c_y = (1 if a_y < b_y else -1)

    while a_x != b_x and a_y != b_y:
        vents_loc[(a_x, a_y)] += 1
        a_x += c_x
        a_y += c_y
    vents_loc[(a_x, a_y)] += 1
    return vents_loc


def get_overlap(vents_loc):
    overlap = 0
    for i in vents_loc:
        if vents_loc.get(i) >= 2:
            overlap += 1
    return overlap


def solution1(data):
    vents_loc = defaultdict(int)

    for line in data:
        a_x, a_y, b_x, b_y = get_cords(line)
        vents_loc = horizon_vertical(a_x, a_y, b_x, b_y, vents_loc, 1)
    
    print("Number of points that are overlap at least twice, horizontal or vertical:", get_overlap(vents_loc))


def solution2(data):
    vents_loc = defaultdict(int)

    for line in data:
        a_x, a_y, b_x, b_y = get_cords(line)
        vents_loc = horizon_vertical(a_x, a_y, b_x, b_y, vents_loc, 2)
    
    print("Number of points that are overlap at least twice, horizontal, vertical or diagonal:", get_overlap(vents_loc))

def main():
    # data = get_input("test-data.txt")
    data = get_input("input-d5.txt")
    solution1(data)
    solution2(data)


if __name__ == '__main__':
    main()
