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


def check_for_winner(boards, drawNumber):
    lastDraw, winBoard, winnerFound = check_horizontal(boards, drawNumber)
    if winnerFound:
        return lastDraw, winBoard, winnerFound
    else:
        return 0, 0, False


def check_horizontal(boards, drawNumber):
    b_counter = 0
    for board in boards:
        for j in board:
            x_counter = 0
            for k in j:
                if 'x' in k:
                    x_counter += 1

            if x_counter == 5:
                lastDraw, winBoard = drawNumber, b_counter
                print('Winning board found! Board number %d is the winning board!' % (b_counter + 1))
                return lastDraw, winBoard, True
        b_counter += 1
    return 0, 0, False


# def check_vertical(boards, drawNumber):
#     b_counter = 0
#     for board in boards:
#         for j in board:
#             x_counter = 0
#             for k in j:
#                 if 'x' in k:
#                     x_counter += 1

#             if x_counter == 5:
#                 lastDraw, winBoard = drawNumber, b_counter
#                 print('Winning board found! Board number %d is the winning board!' % (b_counter + 1))
#                 return lastDraw, winBoard, True
#         b_counter += 1
#     return 0, 0, False


def solution1(data):
    drawNumbers = data[0].split(',')
    boards = create_boards(data)
    winnerFound, lastDraw, winBoard = False, 0, 0
    
    for drawNumber in drawNumbers:
        b_counter = 0
        for board in boards:
            j_counter = 0
            for j in board:
                k_counter = 0
                for k in j: 
                    if drawNumber == k:
                        board[j_counter][k_counter] += 'x'
                    k_counter += 1
                j_counter += 1
            b_counter += 1
        
        lastDraw, winBoard, winnerFound = check_for_winner(boards, drawNumber)

        if winnerFound:
            break
        
    unmarkedSum = 0
    print('Winning Number:', lastDraw)
    for line in boards[winBoard]:
        print(line)
        for number in line:
            if 'x' not in number:
                unmarkedSum += int(number)
                print('Unmarked number:', number)
    
    print('Final board score:', (unmarkedSum * int(lastDraw)))


def solution2(data):
    pass


if __name__ == '__main__':
    # data = get_input("test-data.txt")
    data = get_input("input-d4.txt")
    solution1(data)
    solution2(data)