def get_input(filename):
    inputFile = "2021/input/" + filename
    with open(inputFile) as fhand:
        data = [line.strip() for line in fhand]
    return data
    

def create_boards(data):
    data_c, data_l = 0, len(data)
    board, board_list = [], []

    while data_c < data_l:
        x = data[data_c]
        if (len(x) > 0) and (len(x) < 20) and (data_c != (data_l - 1)):
            board.append(x.split())
            data_c += 1
        elif (len(x) > 0) and (len(x) < 20) and (data_c == (data_l - 1)):
            board.append(x.split())
            board_list.append(board)
            data_c += 1
        elif (x == '') and (data_c > 2):
            board_list.append(board)
            board = []
            data_c += 1
        else:
            data_c += 1

    return board_list


def check_for_winner(board):
    if winner_horizontal(board):
        return True
    elif winner_vertical(board):
        return True
    else:
        return False


def winner_horizontal(board):
    for j in board:
        x_counter = 0
        for k in j:
            if 'x' in k:
                x_counter += 1
        if x_counter == 5:
            return True
    return False


def winner_vertical(board):
    counter = 0
    while counter < len(board[0]):
        x_counter = 0
        for line in board:
            if 'x' in (line[counter]):
                x_counter += 1
        if x_counter == 5:
            return True
        counter += 1
    return False


def mark_number(drawNumber, board):
    j_counter = 0
    for j in board:
        k_counter = 0
        for k in j: 
            if drawNumber == k:
                board[j_counter][k_counter] += 'x'
            k_counter += 1
        j_counter += 1
    return board


def calc_score(lastDraw, board):
    unmarkedSum = 0
    for line in board:
        print(line)
        for number in line:
            if 'x' not in number:
                unmarkedSum += int(number)
    return (unmarkedSum * int(lastDraw))


def solution1(data):
    drawNumbers = data[0].split(',')
    boards = create_boards(data)
    winnerFound, lastDraw, winBoard = False, 0, 0
    
    for drawNumber in drawNumbers:
        b_counter = 0
        for board in boards:
            board = mark_number(drawNumber, board)

            winnerFound = check_for_winner(board)
            if winnerFound:
                lastDraw, winBoard = drawNumber, b_counter
                break
            else:
                b_counter += 1
        if winnerFound:
            break
        
    print('Winning Number:', lastDraw)
    print('First board winning score:', calc_score(lastDraw, boards[winBoard]) )


def solution2(data):
    pass


if __name__ == '__main__':
    # data = get_input("test-data.txt")
    data = get_input("input-d4.txt")
    solution1(data)
    # solution2(data)