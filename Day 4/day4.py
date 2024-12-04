def IsChristmasTimePart1(content):
    num_xmas = 0
    content = [line.replace("\n", "") for line in content]

    len_lines = len(content)
    for i in range(len_lines):
        len_characters = len(content[i])
        for j in range(len_characters):
            # HORIZONTAL
            if j + 3 < len_characters and content[i][j:j + 4] == "XMAS":
                num_xmas += 1
            # HORIZONTAL BACKWARDS
            if j + 3 < len_characters and content[i][j:j + 4] == "SAMX":
                num_xmas += 1
            # VERTICAL
            if i + 3 < len_lines and content[i][j] == "X":
                list_to_check = [content[i][j], content[i + 1][j], content[i + 2][j],
                                 content[i + 3][j]]
                if list_to_check == ['X', 'M', 'A', 'S']:
                    num_xmas += 1
            # VERTICAL BACKWARDS
            if i + 3 < len_lines and content[i][j] == "S":
                list_to_check = [content[i][j], content[i + 1][j], content[i + 2][j],
                                 content[i + 3][j]]
                if list_to_check == ['S', 'A', 'M', 'X']:
                    num_xmas += 1
            # DIAGONAL DOWN
            if i + 3 < len_lines and j + 3 < len_characters and content[i][j] == "X":
                list_to_check = [content[i][j], content[i + 1][j + 1], content[i + 2][j + 2],
                                 content[i + 3][j + 3]]
                if list_to_check == ['X', 'M', 'A', 'S']:
                    num_xmas += 1
            # DIAGONAL UP
            if i + 3 < len_lines and j + 3 < len_characters and content[i][j] == "S":
                list_to_check = [content[i][j], content[i + 1][j + 1], content[i + 2][j + 2],
                                 content[i + 3][j + 3]]
                if list_to_check == ['S', 'A', 'M', 'X']:
                    num_xmas += 1
            # DIAGONAL DOWN BACKWARDS
            if i + 3 < len_lines and j - 3 >= 0 and content[i][j] == "S":
                list_to_check = [content[i][j], content[i + 1][j - 1], content[i + 2][j - 2],
                                 content[i + 3][j - 3]]
                if list_to_check == ['S', 'A', 'M', 'X']:
                    num_xmas += 1
            # DIAGONAL UP BACKWARDS
            if i + 3 < len_lines and j - 3 >= 0 and content[i][j] == "X":
                list_to_check = [content[i][j], content[i + 1][j - 1], content[i + 2][j - 2],
                                 content[i + 3][j - 3]]
                if list_to_check == ['X', 'M', 'A', 'S']:
                    num_xmas += 1

    return num_xmas


def IsChristmasTimePart2(content):
    num_xmas = 0
    content = [line.replace("\n", "") for line in content]

    len_lines = len(content)
    for i in range(len_lines):
        len_characters = len(content[i])
        for j in range(len_characters):
            if i + 2 < len_lines and j + 2 < len_characters and (
                    content[i][j] == "M" or content[i][j] == "S"):
                list_to_check_1 = [content[i][j], content[i + 1][j + 1], content[i + 2][j + 2]]
                list_to_check_2 = [content[i][j + 2], content[i + 1][j + 1], content[i + 2][j]]
                if (list_to_check_1 == ['S', 'A', 'M'] or list_to_check_1 == ['M', 'A', 'S']) and (
                        list_to_check_2 == ['S', 'A', 'M'] or list_to_check_2 == ['M', 'A', 'S']):
                    num_xmas += 1

    return num_xmas


def main():
    with open("input.txt", "r") as file:
        content = file.readlines()

    print("Part 1:")
    print(IsChristmasTimePart1(content))

    print("Part 2:")
    print(IsChristmasTimePart2(content))


if __name__ == "__main__":
    main()
