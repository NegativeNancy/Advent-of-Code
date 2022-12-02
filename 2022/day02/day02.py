""" Script that takes a list of letters that is supposed to be the solution for a
    rock, paper, scissor game. Based on the input a calculation will be done to
    determine what your score is after playing every single round.
    Advent of Code question: https://adventofcode.com/2022/day/2
"""


def get_input(input_file):
    """ " Takes a file as input and places all entries into a list."""
    with open(input_file) as fhand:
        input_data = [line.strip() for line in fhand]
    return input_data


def play_round_on_shapes(opponent_shape, player_shape):
    """Calculates the score and returns the score that the player got.

    :param opponent_shape: range from A = Rock, B = Paper and C = Scissors
    :param player_shape:  range from X = Rock, Y = Paper and Z = Scissors
    :return: Result of the game based on the score given.
    """
    if (
        (opponent_shape == "A" and player_shape == "Y")
        or (opponent_shape == "B" and player_shape == "Z")
        or (opponent_shape == "C" and player_shape == "X")
    ):
        score = score_of_shape(player_shape) + 6
    elif (
        (opponent_shape == "A" and player_shape == "X")
        or (opponent_shape == "B" and player_shape == "Y")
        or (opponent_shape == "C" and player_shape == "Z")
    ):
        score = score_of_shape(player_shape) + 3
    else:
        score = score_of_shape(player_shape)

    return score


def play_round_on_outcome(opponent_shape, player_outcome):
    """Calculates the score and returns the score that the player got.

    :param opponent_shape: range from A = Rock, B = Paper and C = Scissors
    :param player_outcome:  range from X = lose, Y = draw and Z = win
    :return: Result of the game based on the score given.
    """
    if player_outcome == "Z":
        player_shape = find_winning_shape(opponent_shape)
        score = score_of_shape(player_shape) + 6
    elif player_outcome == "Y":
        player_shape = find_draw_shape(opponent_shape)
        score = score_of_shape(player_shape) + 3
    else:
        player_shape = find_losing_shape(opponent_shape)
        score = score_of_shape(player_shape)

    return score


def find_winning_shape(opponent_shape):
    """ Find the wining hand"""
    if opponent_shape == "A":
        player_shape = "Y"
    elif opponent_shape == "B":
        player_shape = "Z"
    else:
        player_shape = "X"
    return player_shape


def find_draw_shape(opponent_shape):
    """ Find the drawing hand"""
    if opponent_shape == "A":
        player_shape = "X"
    elif opponent_shape == "B":
        player_shape = "Y"
    else:
        player_shape = "Z"
    return player_shape


def find_losing_shape(opponent_shape):
    """ Find the losing hand"""
    if opponent_shape == "A":
        player_shape = "Z"
    elif opponent_shape == "B":
        player_shape = "X"
    else:
        player_shape = "Y"
    return player_shape


def score_of_shape(shape):
    """
    Calculates and returns the score of the player_shape
    :param shape: the shape that the player has thrown
    :return: the score that each shape has been given
    """
    if shape == "X":
        shape_score = 1
    elif shape == "Y":
        shape_score = 2
    elif shape == "Z":
        shape_score = 3
    else:
        shape_score = 0

    return shape_score


def solution1(input_data):
    """ Based on the cheat sheet, we determine which hand needs to play to win each game"""
    end_score = 0
    for line in input_data:
        play_list = line.split()
        end_score += play_round_on_shapes(play_list[0], play_list[1])

    print("The player had a total score of", end_score)


def solution2(input_data):
    """ Based on the cheat sheet, we determine which hand needs to play to win each game"""
    end_score = 0
    for line in input_data:
        play_list = line.split()
        end_score += play_round_on_outcome(play_list[0], play_list[1])

    print("The player had a total score of", end_score)


if __name__ == "__main__":
    # data = get_input("test_input")
    data = get_input("input_day02")
    solution1(data)
    solution2(data)
