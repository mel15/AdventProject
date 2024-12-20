import math
from dataclasses import dataclass

length_column = 103
length_line = 101


@dataclass
class Robot:
    position: list
    velocity: list

    def update_position(self):
        possible_new_position = [self.position[0] + self.velocity[0],
                                 self.position[1] + self.velocity[1]]

        if possible_new_position[0] < 0:
            possible_new_position[0] = length_column + possible_new_position[0]

        if possible_new_position[1] < 0:
            possible_new_position[1] = length_line + possible_new_position[1]

        if possible_new_position[0] >= length_column:
            possible_new_position[0] = possible_new_position[0] - length_column

        if possible_new_position[1] >= length_line:
            possible_new_position[1] = possible_new_position[1] - length_line

        self.position = possible_new_position

    def get_position(self):
        return self.position


def print_board(board):
    print()
    for line in board:
        for value in line:
            print(value, end="")
        print()


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
    lines = [line.replace("\n", "") for line in lines]
    robots = []
    for line in lines:
        robot_line = line.split()
        index_x_position_robot = robot_line[0].index("p=") + 2
        index_comma_position_robot = robot_line[0].index(",")
        position_robot = [int(robot_line[0][index_comma_position_robot + 1:]),
                          int(robot_line[0][index_x_position_robot:index_comma_position_robot])]
        index_x_velocity_robot = robot_line[1].index("v=") + 2
        index_comma_velocity_robot = robot_line[1].index(",")
        velocity_robot = [int(robot_line[1][index_comma_velocity_robot + 1:]),
                          int(robot_line[1][index_x_velocity_robot:index_comma_velocity_robot])]
        robots.append(Robot(position=position_robot, velocity=velocity_robot))

    print("initial board")
    board = update_board(robots)
    print_board(board)
    update_board(robots)
    seconds = 100
    for i in range(seconds):
        for robot in robots:
            robot.update_position()
    print("final board")
    board = update_board(robots)
    print_board(board)

    print("Safety factor is:")
    print(calculate_quadrants_safety(board))


def calculate_quadrants_safety(board):
    half_columns = math.floor(length_column / 2)
    half_lines = math.floor(length_line / 2)

    quadrant_1 = 0
    quadrant_2 = 0
    quadrant_3 = 0
    quadrant_4 = 0
    for i, line in enumerate(board):
        for j, value in enumerate(line):
            if value != ".":
                if 0 <= i < half_columns and 0 <= j < half_lines:
                    quadrant_1 = quadrant_1 + int(value)
                elif 0 <= i < half_columns and length_line - half_lines <= j < length_line:
                    quadrant_2 = quadrant_2 + int(value)
                elif length_column - half_columns <= i < length_column and 0 <= j < half_lines:
                    quadrant_3 = quadrant_3 + int(value)
                elif (length_column - half_columns <= i < length_column and
                      length_line - half_lines <= j < length_line):
                    quadrant_4 = quadrant_4 + int(value)
    return quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4


def update_board(robots):
    board = []
    robots_positions = []
    for robot in robots:
        robots_positions.append(robot.get_position())

    for i in range(length_column):
        line = []
        for j in range(length_line):
            if [i, j] in robots_positions:
                how_many_robots = robots_positions.count([i, j])
                line.append(how_many_robots)
            else:
                line.append(".")
        board.append(line)
    return board


if __name__ == "__main__":
    main()
