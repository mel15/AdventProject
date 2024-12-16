import numpy as np


def main():
    # 3 tokens to push the A button
    # 1 token to push the B button
    # Specific amount to the right (along the X axis)
    # Specific amount forward (along the Y axis) each time that button is pressed

    # Each machine contains one prize; to win the prize,
    # the claw must be positioned exactly above the prize
    # on both the X and Y axes.

    # what is the smallest number of tokens you would have to
    # spend to win as many prizes as possible?
    with open("input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.replace("\n", "") for line in lines]
    dict_claw_machines = {}
    number_machine = 1
    A_price = 3
    B_price = 1
    total_tokens = 0
    for i, line in enumerate(lines):
        if "Prize" in line:
            line_two_up = lines[i - 2]
            line_one_up = lines[i - 1]
            first_eq_a = line_two_up.index("X+") + 2
            first_eq_comma = line_two_up.index(",")
            second_eq_a = line_two_up.index("Y+") + 2

            first_eq_b = line_one_up.index("X+") + 2
            second_eq_comma = line_one_up.index(",")
            second_eq_b = line_one_up.index("Y+") + 2
            first_eq = [int(line_two_up[first_eq_a:first_eq_comma]),
                        int(line_one_up[first_eq_b:second_eq_comma])]
            second_eq = [int(line_two_up[second_eq_a:]), int(line_one_up[second_eq_b:])]

            price_x = line.index("X=") + 2
            price_comma = line.index(",")
            price_y = line.index("Y=") + 2

            A = np.array([first_eq, second_eq])
            # B = np.array([int(line[price_x:price_comma]), int(line[price_y:])])
            price_x_corrected = int(line[price_x:price_comma]) + 10000000000000
            price_y_corrected = int(line[price_y:]) + 10000000000000
            B = np.array([price_x_corrected, price_y_corrected])

            solutions = np.linalg.solve(A, B)
            solution_A = round(solutions[0], 2)
            solution_B = round(solutions[1], 2)

            if solution_A == int(solution_A) and solution_B == int(solution_B):
                total_tokens = total_tokens + int(solution_A * A_price) + int(solution_B * B_price)
            print(solutions)
    print(f"Total tokens is: {total_tokens}")


if __name__ == "__main__":
    main()
