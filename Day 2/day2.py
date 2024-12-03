import copy


def main():
    total_safe = 0
    with (open("input.txt", "r") as file):
        lines = file.readlines()
        lines = [line.replace("\n", "") for line in lines]
        for line in lines:
            decreasing_values = []
            difference_values = []
            new_line = line.split()
            line_numbers = [int(number) for number in new_line]
            if check_safe(line_numbers, decreasing_values, difference_values):
                total_safe = total_safe + 1
                continue

            true_count = decreasing_values.count(True)
            false_count = decreasing_values.count(False)
            line_copy = copy.deepcopy(line_numbers)
            line_copy2 = copy.deepcopy(line_numbers)

            if true_count == 1:
                true_index = decreasing_values.index(True)
                del line_copy[true_index]
                del line_copy2[true_index + 1]
                decreasing_values_true = []
                difference_values_true = []
                if check_safe(line_copy, decreasing_values_true, difference_values_true):
                    total_safe = total_safe + 1
                    continue
                if check_safe(line_copy2, decreasing_values_true, difference_values_true):
                    total_safe = total_safe + 1
                    continue

            elif false_count == 1:
                false_index = decreasing_values.index(False)
                del line_copy[false_index]
                del line_copy2[false_index + 1]
                decreasing_values_false = []
                difference_values_false = []
                if check_safe(line_copy, decreasing_values_false, difference_values_false):
                    total_safe = total_safe + 1
                    continue
                if check_safe(line_copy2, decreasing_values_false, difference_values_false):
                    total_safe = total_safe + 1
                    continue

            problematic_num = [number for number in difference_values if
                               abs(number) > 3 or abs(number) < 1]
            if len(problematic_num) == 1:
                line_copy = copy.deepcopy(line_numbers)
                line_copy2 = copy.deepcopy(line_numbers)

                index_value = difference_values.index(problematic_num[0])

                del line_copy[index_value]
                decreasing_values_diff = []
                difference_values_diff = []
                if check_safe(line_copy, decreasing_values_diff, difference_values_diff):
                    total_safe = total_safe + 1
                    continue

                del line_copy2[index_value + 1]
                decreasing_values_diff = []
                difference_values_diff = []
                if check_safe(line_copy2, decreasing_values_diff, difference_values_diff):
                    total_safe = total_safe + 1
                    continue

            decreasing_values_diff_last = []
            difference_values_diff_last = []
            if check_safe(line_numbers[:-1], decreasing_values_diff_last,
                          difference_values_diff_last):
                total_safe = total_safe + 1
                continue

            decreasing_values_diff_first = []
            difference_values_diff_first = []
            if check_safe(line_numbers[1:], decreasing_values_diff_first,
                          difference_values_diff_first):
                total_safe = total_safe + 1
                continue

    print(total_safe)


def part_1_clean():
    total_safe = 0
    with (open("input.txt", "r") as file):
        lines = file.readlines()
        lines = [line.replace("\n", "") for line in lines]
        for line in lines:
            decreasing_values = []
            difference_values = []
            new_line = line.split()
            line_numbers = [int(number) for number in new_line]
            if check_safe(line_numbers, decreasing_values, difference_values):
                total_safe = total_safe + 1

    print(total_safe)


def check_safe(line_numbers, decreasing_values, difference_values):
    is_line_safe = True
    for i in range(len(line_numbers) - 1):
        total_value = line_numbers[i] - line_numbers[i + 1]
        decreasing_values.append(total_value > 0)
        difference_values.append(total_value)

        if abs(total_value) < 1 or abs(total_value) > 3:
            is_line_safe = False
            continue

    # There is both True and False in the list
    if len(set(decreasing_values)) != 1:
        is_line_safe = False

    return is_line_safe


def part_1():
    total_safe = 0
    with (open("input.txt", "r") as file):
        lines = file.readlines()
        lines = [line.replace("\n", "") for line in lines]
        for line in lines:
            decreasing_values = []
            is_line_safe = True
            new_line = line.split()
            line_numbers = [int(number) for number in new_line]
            for i in range(len(line_numbers) - 1):
                total_value = line_numbers[i] - line_numbers[i + 1]
                decreasing_values.append(total_value > 0)
                if abs(total_value) < 1 or abs(total_value) > 3:
                    is_line_safe = False
                    continue
            # There is both True and False in the list
            if len(set(decreasing_values)) != 1:
                is_line_safe = False
            if is_line_safe:
                total_safe = total_safe + 1
    print(total_safe)


if __name__ == "__main__":
    main()
