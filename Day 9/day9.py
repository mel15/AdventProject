import copy


def main():
    with open("input.txt", "r") as file:
        content = file.read()

    id = 0
    # decode disk
    diskmap = []
    for i, value in enumerate(content):
        if i % 2 == 0:
            for v in range(int(value)):
                diskmap.append(id)
            id += 1
        else:
            for v in range(int(value)):
                diskmap.append(".")

    """print("Initial diskmap")
    print(diskmap)
    print("Optimized diskmap")
    output_diskmap_part1 = calculate_output_diskmap_part1(diskmap)
    print(output_diskmap_part1)

    total_value = 0
    for i, value in enumerate(output_diskmap_part1):
        if value == ".":
            break
        total_value = total_value + i * int(value)
    print(f"Total value part 1: {total_value}")"""
    print("Initial diskmap")
    print(diskmap)
    print("Optimized diskmap")
    output_diskmap_part2 = calculate_output_diskmap_part2(diskmap)
    print(output_diskmap_part2)
    total_value = 0
    for i, value in enumerate(output_diskmap_part2):
        if value == ".":
            continue
        total_value = total_value + i * int(value)
    print(f"Total value part 2: {total_value}")


def calculate_output_diskmap_part2(diskmap):
    copy_diskmap = copy.deepcopy(diskmap)
    ids_moved = []
    for i in range(len(diskmap) - 1, 0, -1):
        found_point = False
        print(i)
        if diskmap[i] in ids_moved:
            continue
        if diskmap[i] != ".":
            for j in range(len(copy_diskmap)):
                if found_point:
                    break
                if copy_diskmap[j] == "." and not found_point and j < i:
                    count_times = diskmap.count(diskmap[i])
                    ids_moved.append(diskmap[i])
                    if copy_diskmap[j:j + count_times].count(".") == count_times:
                        found_point = True
                        for count in range(count_times):
                            copy_diskmap[j + count] = diskmap[i]
                            copy_diskmap[i - count] = "."
    return copy_diskmap


def calculate_output_diskmap_part1(diskmap):
    copy_diskmap = copy.deepcopy(diskmap)
    length_final_chr = len(diskmap) - diskmap.count(".")

    for i in range(len(diskmap) - 1, 0, -1):
        found_point = False
        print(i)
        if diskmap[i] != ".":
            for j in range(len(copy_diskmap)):
                if found_point:
                    break
                if copy_diskmap[j] == "." and not found_point:
                    copy_diskmap[j] = diskmap[i]
                    copy_diskmap[i] = "."
                    found_point = True
                    copy_diskmap.count(".")
                    if copy_diskmap[0:length_final_chr].count(".") == 0:
                        return copy_diskmap


if __name__ == "__main__":
    main()
