import copy


def part_1(list_left, list_right):
    total_distance = 0

    local_left = copy.deepcopy(list_left)
    local_right = copy.deepcopy(list_right)
    while len(local_left) != 0:
        min_left = min(local_left)
        min_right = min(local_right)

        index_min_left = local_left.index(min(local_left))
        index_min_right = local_right.index(min(local_right))

        total_distance = total_distance + abs(min_left - min_right)
        del local_left[index_min_left]
        del local_right[index_min_right]

    print(total_distance)


def part_2(list_left, list_right):
    total_similarity = 0
    for number_left in list_left:
        occurrences = list_right.count(number_left)
        current_similarity = number_left * occurrences
        total_similarity = total_similarity + current_similarity

    print(total_similarity)


def main():
    list_left = []
    list_right = []
    with open("input.txt", "r") as file:
        content = file.readlines()
        for line in content:
            clean_line = line.replace("\n", "")
            split_line = clean_line.split()
            list_left.append(int(split_line[0]))
            list_right.append(int(split_line[1]))

    print("Part 1 answer:")
    part_1(list_left, list_right)

    print("Part 2 answer:")
    part_2(list_left, list_right)


if __name__ == "__main__":
    main()
