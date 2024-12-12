import copy

topo_map = []
trail_heads = {}


def add_trail_to_dict(current_point, starting_point, rail_path):
    if topo_map[current_point[0]][current_point[1]] == 9:
        starting_point_tuple = tuple(starting_point)

        if starting_point_tuple not in trail_heads:
            trail_heads[starting_point_tuple] = [rail_path]
        else:
            paths = trail_heads.get(starting_point_tuple)
            if rail_path not in paths:
                paths.append(rail_path)
                trail_heads[starting_point_tuple] = paths
        return current_point
    else:
        return None


def check_up(point):
    # i - 1
    # j

    # check that the values are not negative
    in_range = point[0] - 1 >= 0
    # check that the value we check goes up by one
    increasing_value = False
    if in_range:
        increasing_value = topo_map[point[0] - 1][point[1]] == topo_map[point[0]][point[1]] + 1
    return in_range and increasing_value


def check_down(point):
    # i + 1
    # j
    len_map = len(topo_map)

    # check if the point is not bigger than the length of the map
    in_range = point[0] + 1 < len_map
    # check that the value we check goes up by one
    increasing_value = False
    if in_range:
        increasing_value = topo_map[point[0] + 1][point[1]] == topo_map[point[0]][point[1]] + 1
    return in_range and increasing_value


def check_right(out_point):
    # i
    # j + 1
    point = copy.deepcopy(out_point)
    len_line = len(topo_map[0])

    # check if the point is not bigger than the length of the line
    in_range = point[1] + 1 < len_line
    # check that the value we check goes up by one
    increasing_value = False
    if in_range:
        increasing_value = topo_map[point[0]][point[1] + 1] == topo_map[point[0]][point[1]] + 1
    return in_range and increasing_value


def check_left(out_point):
    # i
    # j - 1
    point = copy.deepcopy(out_point)

    # check if the point is bigger or grater than zero
    in_range = point[1] - 1 >= 0
    # check that the value we check goes up by one
    increasing_value = False
    if in_range:
        increasing_value = topo_map[point[0]][point[1] - 1] == topo_map[point[0]][point[1]] + 1
    return in_range and increasing_value


def find_end_trail(current_point, starting_point, rail_path):
    len_map = len(topo_map)
    len_line = len(topo_map[0])
    local_current_point = copy.deepcopy(current_point)

    while (topo_map[local_current_point[0]][local_current_point[1]] <= 9 and 0 <=
           local_current_point[0] < len_map and 0 <= local_current_point[1] < len_line):
        prev_point = copy.deepcopy(local_current_point)
        value_up = None
        value_down = None
        value_left = None
        value_right = None

        if check_down(prev_point):
            local_current_point = [prev_point[0] + 1, prev_point[1]]
            down_path = copy.deepcopy(rail_path)
            down_path.append(local_current_point)
            value_down = find_end_trail(local_current_point, starting_point, down_path)
            add_trail_to_dict(local_current_point, starting_point, down_path)
        if check_up(prev_point):
            local_current_point = [prev_point[0] - 1, prev_point[1]]
            up_path = copy.deepcopy(rail_path)
            up_path.append(local_current_point)
            value_up = find_end_trail(local_current_point, starting_point, up_path)
            add_trail_to_dict(local_current_point, starting_point, up_path)
        if check_right(prev_point):
            local_current_point = [prev_point[0], prev_point[1] + 1]
            right_path = copy.deepcopy(rail_path)
            right_path.append(local_current_point)
            value_right = find_end_trail(local_current_point, starting_point, right_path)
            add_trail_to_dict(local_current_point, starting_point, right_path)
        if check_left(prev_point):
            local_current_point = [prev_point[0], prev_point[1] - 1]
            left_path = copy.deepcopy(rail_path)
            left_path.append(local_current_point)
            value_left = find_end_trail(local_current_point, starting_point, left_path)
            add_trail_to_dict(local_current_point, starting_point, left_path)

        if value_left is None and value_right is None and value_up is None and value_down is None:
            return None

        if prev_point == local_current_point:
            break
    return None


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
    lines = [line.replace("\n", "") for line in lines]
    for i in range(len(lines)):
        line = []
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                line.append(int(lines[i][j]))
            else:
                line.append(lines[i][j])
        topo_map.append(line)

    len_map = len(topo_map)
    len_line = len(topo_map[0])

    for i in range(len_map):
        for j in range(len_line):
            if topo_map[i][j] == 0:
                starting_point = [i, j]
                current_point = copy.deepcopy(starting_point)
                rail_path = [starting_point]
                if current_point[0] + 1 < len_map and topo_map[current_point[0] + 1][
                    current_point[1]] == (
                        topo_map[current_point[0]][current_point[1]] + 1):
                    find_end_trail(current_point, starting_point, rail_path)
                if 0 <= current_point[0] - 1 and topo_map[current_point[0] - 1][
                    current_point[1]] == (
                        topo_map[current_point[0]][current_point[1]] + 1):
                    find_end_trail(current_point, starting_point, rail_path)
                if current_point[1] + 1 < len_line and topo_map[current_point[0]][
                    current_point[1] + 1] == (
                        topo_map[current_point[0]][current_point[1]] + 1):
                    find_end_trail(current_point, starting_point, rail_path)
                if current_point[1] - 1 >= 0 and topo_map[current_point[0]][
                    current_point[1] - 1] == (
                        topo_map[current_point[0]][current_point[1]] + 1):
                    find_end_trail(current_point, starting_point, rail_path)

    print(trail_heads)
    total_scores = 0
    for key, values in trail_heads.items():
        total_scores = total_scores + len(values)
    print(f"Total score for part 2: {total_scores}")


if __name__ == "__main__":
    main()
