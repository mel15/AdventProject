import copy


def print_board(board):
    for line in board:
        print(line)


def part_1(board):
    initial_position = None
    len_board = len(board)
    len_line = len(board[0])
    possible_guard = ["^", ">", "v", "<"]
    for i in range(len_board):
        for j in range(len(board[i])):
            if board[i][j] in possible_guard:
                initial_position = [i, j]

    current_position = initial_position
    in_board = (len_board > current_position[0] >= 0) and (
            len(board[0]) > current_position[1] >= 0)

    print("INITIAL BOARD")
    print_board(board)
    while in_board:
        if board[current_position[0]][current_position[1]] == "^":
            if (current_position[0] - 1 >= 0) and (
                    board[current_position[0] - 1][current_position[1]] != "#"):
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("^", "X")
                next_line = board[current_position[0] - 1]
                next_line = next_line[:current_position[1]] + "^" + next_line[
                                                                    current_position[1] + 1:]
                board[current_position[0] - 1] = next_line
                current_position = [current_position[0] - 1, current_position[1]]
            elif current_position[0] - 1 < 0:
                current_position = [current_position[0] - 1, current_position[1]]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("^", ">")
        elif board[current_position[0]][current_position[1]] == ">":
            if (current_position[1] + 1 < len_line) and (
                    board[current_position[0]][current_position[1] + 1] != "#"):
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace(">", "X")
                next_line = board[current_position[0]]
                next_line = next_line[:current_position[1] + 1] + ">" + next_line[
                                                                        current_position[1] + 2:]
                board[current_position[0]] = next_line
                current_position = [current_position[0], current_position[1] + 1]
            elif current_position[1] + 1 == len_line:
                current_position = [current_position[0], current_position[1] + 1]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace(">", "v")
        elif board[current_position[0]][current_position[1]] == "v":
            if (current_position[0] + 1 < len_board) and (
                    board[current_position[0] + 1][current_position[1]] != "#"):
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("v", "X")
                next_line = board[current_position[0] + 1]
                next_line = next_line[:current_position[1]] + "v" + next_line[
                                                                    current_position[1] + 1:]
                board[current_position[0] + 1] = next_line
                current_position = [current_position[0] + 1, current_position[1]]
            elif current_position[0] + 1 == len_board:
                current_position = [current_position[0] + 1, current_position[1]]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("v", "<")
        elif board[current_position[0]][current_position[1]] == "<":
            if (current_position[1] - 1 >= 0) and (
                    board[current_position[0]][current_position[1] - 1] != "#"):
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("<", "X")
                next_line = board[current_position[0]]
                next_line = next_line[:current_position[1] - 1] + "<" + next_line[
                                                                        current_position[1]:]
                board[current_position[0]] = next_line
                current_position = [current_position[0], current_position[1] - 1]
            elif current_position[1] - 1 < 0:
                current_position = [current_position[0], current_position[1] - 1]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("<", "^")

        in_board = (len_board > current_position[0] >= 0) and (
                len(board[0]) > current_position[1] >= 0)

    # The last one counts, but we dont update the last position
    total_Xs = 1
    for line in board:
        total_Xs = total_Xs + line.count("X")

    print()
    print("FINAL BOARD")
    print_board(board)

    print("How many X:")
    print(total_Xs)


def CanEscape(board, in_board, initial_position, current_position):
    i = 0
    len_board = len(board)
    len_line = len(board[0])
    canEscape = True
    prev_X = 0
    current_X = 0
    times_repeated = 0
    prev_pos = current_position
    spots_on_board = len_board * len_line
    total_obs = 0
    for line in board:
        total_obs = total_obs + line.count("#")
    spots_on_board = spots_on_board - total_obs
    while in_board:
        prev_X = current_X
        total_Xs = 1
        current_X = total_Xs
        if prev_X == current_X and prev_pos != current_position:
            if times_repeated > spots_on_board:
                canEscape = False
                break
            else:
                times_repeated += 1

        prev_pos = current_position
        if board[current_position[0]][current_position[1]] == "^":
            if (current_position[0] - 1 >= 0) and (
                    board[current_position[0] - 1][current_position[1]] != "#"):
                if board[current_position[0] - 1][current_position[1]] == ".":
                    total_Xs += 1
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("^", "X")
                next_line = board[current_position[0] - 1]
                next_line = next_line[:current_position[1]] + "^" + next_line[
                                                                    current_position[1] + 1:]
                board[current_position[0] - 1] = next_line
                current_position = [current_position[0] - 1, current_position[1]]
            elif current_position[0] - 1 < 0:
                current_position = [current_position[0] - 1, current_position[1]]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("^", ">")
        elif board[current_position[0]][current_position[1]] == ">":
            if (current_position[1] + 1 < len_line) and (
                    board[current_position[0]][current_position[1] + 1] != "#"):
                if board[current_position[0]][current_position[1] + 1] == ".":
                    total_Xs += 1
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace(">", "X")
                next_line = board[current_position[0]]
                next_line = next_line[:current_position[1] + 1] + ">" + next_line[
                                                                        current_position[1] + 2:]
                board[current_position[0]] = next_line
                current_position = [current_position[0], current_position[1] + 1]
            elif current_position[1] + 1 == len_line:
                current_position = [current_position[0], current_position[1] + 1]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace(">", "v")
        elif board[current_position[0]][current_position[1]] == "v":
            if (current_position[0] + 1 < len_board) and (
                    board[current_position[0] + 1][current_position[1]] != "#"):
                if board[current_position[0] + 1][current_position[1]] == ".":
                    total_Xs += 1
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("v", "X")
                next_line = board[current_position[0] + 1]
                next_line = next_line[:current_position[1]] + "v" + next_line[
                                                                    current_position[1] + 1:]
                board[current_position[0] + 1] = next_line
                current_position = [current_position[0] + 1, current_position[1]]
            elif current_position[0] + 1 == len_board:
                current_position = [current_position[0] + 1, current_position[1]]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("v", "<")
        elif board[current_position[0]][current_position[1]] == "<":
            if (current_position[1] - 1 >= 0) and (
                    board[current_position[0]][current_position[1] - 1] != "#"):
                if board[current_position[0]][current_position[1] - 1] == ".":
                    total_Xs += 1
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("<", "X")
                next_line = board[current_position[0]]
                next_line = next_line[:current_position[1] - 1] + "<" + next_line[
                                                                        current_position[1]:]
                board[current_position[0]] = next_line
                current_position = [current_position[0], current_position[1] - 1]
            elif current_position[1] - 1 < 0:
                current_position = [current_position[0], current_position[1] - 1]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("<", "^")

        in_board = (len_board > current_position[0] >= 0) and (
                len_line > current_position[1] >= 0)
        i += 1

    return canEscape


def CanEscape_backup(board, in_board, initial_position, current_position):
    i = 0
    len_board = len(board)
    len_line = len(board[0])
    canEscape = True
    prev_X = 0
    current_X = 0
    times_repeated = 0
    prev_pos = current_position
    while in_board:
        prev_X = current_X
        total_Xs = 1
        for line in board:
            total_Xs = total_Xs + line.count("X")
        current_X = total_Xs
        if prev_X == current_X and prev_pos != current_position:
            if times_repeated > len_board * len_line:
                canEscape = False
                break
            else:
                times_repeated += 1

        prev_pos = current_position
        if board[current_position[0]][current_position[1]] == "^":
            if (current_position[0] - 1 >= 0) and (
                    board[current_position[0] - 1][current_position[1]] != "#"):
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("^", "X")
                next_line = board[current_position[0] - 1]
                next_line = next_line[:current_position[1]] + "^" + next_line[
                                                                    current_position[1] + 1:]
                board[current_position[0] - 1] = next_line
                current_position = [current_position[0] - 1, current_position[1]]
            elif current_position[0] - 1 < 0:
                current_position = [current_position[0] - 1, current_position[1]]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("^", ">")
        elif board[current_position[0]][current_position[1]] == ">":
            if (current_position[1] + 1 < len_line) and (
                    board[current_position[0]][current_position[1] + 1] != "#"):
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace(">", "X")
                next_line = board[current_position[0]]
                next_line = next_line[:current_position[1] + 1] + ">" + next_line[
                                                                        current_position[1] + 2:]
                board[current_position[0]] = next_line
                current_position = [current_position[0], current_position[1] + 1]
            elif current_position[1] + 1 == len_line:
                current_position = [current_position[0], current_position[1] + 1]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace(">", "v")
        elif board[current_position[0]][current_position[1]] == "v":
            if (current_position[0] + 1 < len_board) and (
                    board[current_position[0] + 1][current_position[1]] != "#"):
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("v", "X")
                next_line = board[current_position[0] + 1]
                next_line = next_line[:current_position[1]] + "v" + next_line[
                                                                    current_position[1] + 1:]
                board[current_position[0] + 1] = next_line
                current_position = [current_position[0] + 1, current_position[1]]
            elif current_position[0] + 1 == len_board:
                current_position = [current_position[0] + 1, current_position[1]]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("v", "<")
        elif board[current_position[0]][current_position[1]] == "<":
            if (current_position[1] - 1 >= 0) and (
                    board[current_position[0]][current_position[1] - 1] != "#"):
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("<", "X")
                next_line = board[current_position[0]]
                next_line = next_line[:current_position[1] - 1] + "<" + next_line[
                                                                        current_position[1]:]
                board[current_position[0]] = next_line
                current_position = [current_position[0], current_position[1] - 1]
            elif current_position[1] - 1 < 0:
                current_position = [current_position[0], current_position[1] - 1]
            else:
                current_line = board[current_position[0]]
                board[current_position[0]] = current_line.replace("<", "^")

        in_board = (len_board > current_position[0] >= 0) and (
                len_line > current_position[1] >= 0)
        i += 1

    return canEscape


def part_2(board):
    initial_position = None
    len_board = len(board)
    len_line = len(board[0])
    possible_guard = ["^", ">", "v", "<"]
    for i in range(len_board):
        for j in range(len_line):
            if board[i][j] in possible_guard:
                initial_position = [i, j]

    looped_guard = 0
    for i in range(len_board):
        print(f"on line: {i}")
        for j in range(len_line):
            if board[i][j] == "." or board[i][j] == "X":
                # print(f"Iteration i={i} j={j}")
                temp_board = copy.deepcopy(board)
                current_position = initial_position
                in_board = (len_board > current_position[0] >= 0) and (
                        len_line > current_position[1] >= 0)

                current_line = temp_board[i]
                current_line = current_line[:j] + "#" + current_line[j + 1:]
                temp_board[i] = current_line
                if not CanEscape(temp_board, in_board, initial_position, current_position):
                    looped_guard += 1
                    # print("CANNOT ESCAPE")
                # else:
                # print("CAN ESCAPE")

    # print(temp_board)
    print(looped_guard)


def main():
    with open("input.txt", "r") as file:
        board = file.readlines()

    board = [line.replace("\n", "") for line in board]

    # print("PART 1")
    # part_1(board)

    print("PART 2")
    part_2(board)


if __name__ == "__main__":
    main()
