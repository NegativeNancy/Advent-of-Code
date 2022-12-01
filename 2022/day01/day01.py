""" Script that takes a list of integers and sums every group till the next empty row
    and place them in a dict. Two solutions have been created to display the info that
    is requested in the Advent of Code question:
    https://adventofcode.com/2022/day/1
"""


def get_input(input_file):
    """ " Takes a file as input and places all entries into a list."""
    with open(input_file) as fhand:
        input_data = [line.strip() for line in fhand]
    return input_data


def sum_backpacks(input_data):
    """Take the input data and calculates per group what the sum is and place that in a dict.

    return: dict of calories per elf.
    """
    backpack_elf = 0
    elf_number = {}
    counter = 0

    for calories in input_data:
        if calories != "":
            backpack_elf += int(calories)
        else:
            elf_number[counter] = backpack_elf
            counter += 1
            backpack_elf = 0

    elf_number[counter] = backpack_elf

    return elf_number


def solution1(input_data):
    """Prints out which elf has the highest calories in his backpack and what that amount is"""
    elf_number = sum_backpacks(input_data)

    print(
        "Elf number",
        max(elf_number, key=elf_number.get),
        "is carrying the most calories with",
        elf_number[max(elf_number, key=elf_number.get)],
        "calories.",
    )


def solution2(input_data):
    """Prints out the combined calories of the three highest elves."""
    elf_number = sum_backpacks(input_data)
    my_keys = sorted(elf_number, key=elf_number.get, reverse=True)[:3]

    sum_of_calories = 0
    for key in my_keys:
        sum_of_calories += elf_number[key]

    print("The top three elves have a combined calorie count of", sum_of_calories)


if __name__ == "__main__":
    # data = get_input("test_input_day01")
    data = get_input("input_day01")
    solution1(data)
    solution2(data)
