import copy


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

        ordering_rules = []
        updates = []
        for line in lines:
            if "|" in line:
                num_tuple = (int(line[0:2]), int(line[3:5]))
                ordering_rules.append(num_tuple)

            if "," in line:
                update = line.split(",")
                update = [int(number.replace("\n", "")) for number in update]
                updates.append(update)

        print("Part 1:")
        print(part_1(ordering_rules, updates))

        print("Part 2:")
        print(part_2(ordering_rules, updates))


def part_2(ordering_rules, updates):
    total_middle = 0

    for update in updates:
        isCorrectOrder = isSafe(update, ordering_rules)

        new_update = copy.deepcopy(update)
        isCorrectOrderNew = copy.deepcopy(isCorrectOrder)
        while not isCorrectOrderNew:
            rules_to_think = []
            previous_numbers = []
            len_new_update = len(new_update)
            for i in range(len_new_update):
                number = new_update[i]
                for rule in ordering_rules:
                    if rule[0] == number:
                        rules_to_think.append(rule)

                for rule_to_think in rules_to_think:
                    if rule_to_think[0] == number and rule_to_think[1] in previous_numbers:
                        new_index = previous_numbers.index(rule_to_think[1])
                        bad_index = new_update.index(number)
                        element_bad = new_update.pop(bad_index)
                        new_update.insert(new_index, element_bad)
                previous_numbers.append(number)

            isCorrectOrderNew = isSafe(new_update, ordering_rules)

        if not isCorrectOrder:
            middleIndex = int((len(new_update) - 1) / 2)
            total_middle = total_middle + new_update[middleIndex]

    return total_middle


def isSafe(update, ordering_rules):
    isCorrectOrder = True
    rules_to_think = []
    previous_numbers = []
    for i, number in enumerate(update):
        for rule in ordering_rules:
            if rule[0] == number:
                rules_to_think.append(rule)

        for rule_to_think in rules_to_think:
            if rule_to_think[0] == number and rule_to_think[1] in previous_numbers:
                isCorrectOrder = False

        previous_numbers.append(number)

    return isCorrectOrder


def part_1(ordering_rules, updates):
    total_middle = 0

    for update in updates:
        isCorrectOrder = isSafe(update, ordering_rules)

        if isCorrectOrder:
            middleIndex = int((len(update) - 1) / 2)
            total_middle = total_middle + update[middleIndex]
    return total_middle


if __name__ == "__main__":
    main()
