import copy


def part_1(dict_antennas, temp_board):
    len_board = len(temp_board)
    len_line = len(temp_board[0])
    for key, value in dict_antennas.items():
        delta = []
        for i in range(len(value)):
            for j in range(len(value)):
                if value[i] != value[j]:
                    delta = [value[j][0] - value[i][0], value[j][1] - value[i][1]]
                    pos1 = [value[i][0] - delta[0], value[i][1] - delta[1]]

                    if 0 <= pos1[0] < len_board and 0 <= pos1[1] < len_line:
                        new_line = temp_board[pos1[0]]
                        new_line = new_line[:pos1[1]] + "#" + new_line[pos1[1] + 1:]
                        temp_board[pos1[0]] = new_line

                    pos2 = [value[j][0] + delta[0], value[j][1] + delta[1]]
                    if 0 <= pos2[0] < len_board and 0 <= pos2[1] < len_line:
                        new_line = temp_board[pos2[0]]
                        new_line = new_line[:pos2[1]] + "#" + new_line[pos2[1] + 1:]
                        temp_board[pos2[0]] = new_line


def part_2_backup(dict_antennas, temp_board):
    len_board = len(temp_board)
    len_line = len(temp_board[0])
    for key, value in dict_antennas.items():
        delta = []
        for i in range(len(value)):
            for j in range(len(value)):
                if value[i] != value[j]:
                    delta = [value[j][0] - value[i][0], value[j][1] - value[i][1]]
                    pos1 = [value[i][0] - delta[0], value[i][1] - delta[1]]
                    mult_delta = 1
                    while 0 <= pos1[0] < len_board and 0 <= pos1[1] < len_line:
                        new_line = temp_board[pos1[0]]
                        new_line = new_line[:pos1[1]] + "#" + new_line[pos1[1] + 1:]
                        temp_board[pos1[0]] = new_line
                        mult_delta += 1
                        pos1 = [value[i][0] - mult_delta * delta[0],
                                value[i][1] - mult_delta * delta[1]]

                    pos2 = [value[j][0] + delta[0], value[j][1] + delta[1]]
                    mult_delta = 1
                    while 0 <= pos2[0] < len_board and 0 <= pos2[1] < len_line:
                        new_line = temp_board[pos2[0]]
                        new_line = new_line[:pos2[1]] + "#" + new_line[pos2[1] + 1:]
                        temp_board[pos2[0]] = new_line
                        mult_delta += 1
                        pos2 = [value[j][0] + mult_delta * delta[0],
                                value[j][1] + mult_delta * delta[1]]


def part_2(dict_antennas, temp_board):
    len_board = len(temp_board)
    len_line = len(temp_board[0])
    for key, value in dict_antennas.items():
        delta = []
        for i in range(len(value)):
            for j in range(len(value)):
                if value[i] != value[j]:
                    # print(value[i])
                    # print(value[j])
                    new_line = temp_board[value[i][0]]
                    new_line = new_line[:value[i][1]] + "#" + new_line[value[i][1] + 1:]
                    temp_board[value[i][0]] = new_line

                    delta = [value[j][0] - value[i][0], value[j][1] - value[i][1]]
                    pos1 = [value[i][0] - delta[0], value[i][1] - delta[1]]
                    mult_delta = 1
                    while 0 <= pos1[0] < len_board and 0 <= pos1[1] < len_line:
                        new_line = temp_board[pos1[0]]
                        new_line = new_line[:pos1[1]] + "#" + new_line[pos1[1] + 1:]
                        temp_board[pos1[0]] = new_line
                        mult_delta += 1
                        pos1 = [value[i][0] - mult_delta * delta[0],
                                value[i][1] - mult_delta * delta[1]]

                    new_line = temp_board[value[j][0]]
                    new_line = new_line[:value[j][1]] + "#" + new_line[value[j][1] + 1:]
                    temp_board[value[j][0]] = new_line
                    pos2 = [value[j][0] + delta[0], value[j][1] + delta[1]]
                    mult_delta = 1
                    while 0 <= pos2[0] < len_board and 0 <= pos2[1] < len_line:
                        new_line = temp_board[pos2[0]]
                        new_line = new_line[:pos2[1]] + "#" + new_line[pos2[1] + 1:]
                        temp_board[pos2[0]] = new_line
                        mult_delta += 1
                        pos2 = [value[j][0] + mult_delta * delta[0],
                                value[j][1] + mult_delta * delta[1]]


def main():
    with open("input.txt", "r") as file:
        board = file.readlines()

    board = [line.replace("\n", "") for line in board]
    print("INPUT BOARD")
    print_board(board)
    print()
    temp_board_part1 = copy.deepcopy(board)
    temp_board_part2 = copy.deepcopy(board)

    len_board = len(board)
    len_line = len(board[0])
    dict_antennas = {}
    for i in range(len_board):
        for j in range(len_line):
            box = board[i][j]
            if box.isdigit() or box.isalpha():
                indexes = [i, j]
                if board[i][j] not in dict_antennas:
                    dict_antennas[box] = [indexes]
                else:
                    dict_antennas[board[i][j]].append(indexes)

    part_1(dict_antennas, temp_board_part1)

    print("OUTPUT BOARD PART 1")
    print_board(temp_board_part1)
    total_sign = 0
    for line in temp_board_part1:
        total_sign = total_sign + line.count("#")
    print(f"Total signs # for part 1 is: {total_sign}")

    part_2(dict_antennas, temp_board_part2)

    print("OUTPUT BOARD PART 2")
    print_board(temp_board_part2)
    total_sign = 0
    for line in temp_board_part2:
        total_sign = total_sign + line.count("#")
    print(f"Total signs # for part 2 is: {total_sign}")


def print_board(board):
    for line in board:
        print(line)


if __name__ == "__main__":
    main()
