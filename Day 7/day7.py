def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.replace("\n", "") for line in lines]

    print("Part 1:")
    print(part_1(lines))

    print("Part 2:")
    print(part_2(lines))


def part_2(lines):
    total_value = 0
    for line in lines:
        prev_values = []
        values = []
        line_numbers = line.split(":")
        test_value = int(line_numbers[0])
        values_to_try = [int(number) for number in line_numbers[1].split()]

        for i in range(len(values_to_try) - 1):
            if i == 0:
                values = try_operation_part2(values_to_try[i], values_to_try[i + 1])
            else:
                prev_values = values
                values = []
                for prev_value in prev_values:
                    local_values = try_operation_part2(prev_value, values_to_try[i + 1])
                    values.extend(local_values)

        if test_value in values:
            total_value = total_value + test_value

    return total_value


def part_1(lines):
    total_value = 0
    for line in lines:
        prev_values = []
        values = []
        line_numbers = line.split(":")
        test_value = int(line_numbers[0])
        values_to_try = [int(number) for number in line_numbers[1].split()]

        for i in range(len(values_to_try) - 1):
            if i == 0:
                values = try_operation_part1(values_to_try[i], values_to_try[i + 1])
            else:
                prev_values = values
                values = []
                for prev_value in prev_values:
                    local_values = try_operation_part1(prev_value, values_to_try[i + 1])
                    values.extend(local_values)

        if test_value in values:
            total_value = total_value + test_value

    return total_value


def try_operation_part2(num1, num2):
    return multiplication(num1, num2), addition(num1, num2), concatenation(num1, num2)


def concatenation(num1, num2):
    concat_num = str(num1) + str(num2)
    return int(concat_num)


def try_operation_part1(num1, num2):
    return multiplication(num1, num2), addition(num1, num2)


def multiplication(num1, num2):
    return num1 * num2


def addition(num1, num2):
    return num1 + num2


if __name__ == "__main__":
    main()
