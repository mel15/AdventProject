from tqdm import tqdm


def calculate_number(number, dict_saving, count):
    if dict_saving.get(number, 0) == 0:
        return

    if number == 0:
        dict_saving[1] = dict_saving.get(1, 0) + count
    elif len(str(number)) % 2 == 0:
        stone_string = str(number)
        half_length = int(len(stone_string) / 2)
        dict_saving[int(stone_string[:half_length])] = dict_saving.get(
            int(stone_string[:half_length]), 0) + count
        dict_saving[int(stone_string[half_length:])] = dict_saving.get(
            int(stone_string[half_length:]), 0) + count
    else:
        dict_saving[number * 2024] = dict_saving.get(number * 2024, 0) + count
    dict_saving[number] = dict_saving.get(number, 0) - count


def main():
    with open("input.txt", "r") as file:
        contents = file.read()

    contents = contents.split()
    stones = [int(stone) for stone in contents]
    print(stones)
    dict_stones = {}
    for i, stone in enumerate(stones):
        dict_stones[stone] = dict_stones.get(stone, 0) + 1

    blinking_times = 75

    for blink in tqdm(range(blinking_times)):
        dict_stones_copy = dict(dict_stones)
        for stone, count in dict_stones_copy.items():
            calculate_number(stone, dict_stones, count)
        dict_stones = {k: v for k, v in dict_stones.items() if v != 0}

        """print(f"blink {blink + 1}")
        print("prev dict")
        print(dict_stones_copy)
        print("last dict")
        print(dict_stones)"""

    total_value = 0
    for key, values in dict_stones.items():
        total_value = total_value + values
    print(f"The total number of stones is {total_value}")


if __name__ == "__main__":
    main()
