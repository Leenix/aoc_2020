import numpy as np


def load_input(input_file):
    output = []
    with open(input_file) as f:
        for line in f.readlines():
            output.append(list(line.strip('\n')))
    return output


def get_num_trees(input_rows, down=1, right=3):
    num_trees = 0
    row = 0
    column = 0
    while row < len(input_rows):
        if input_rows[row][column % len(input_rows[0])] == '#':
            num_trees += 1
        row += down
        column += right
    return num_trees


if __name__ == '__main__':
    data = load_input("input.txt")
    trees = get_num_trees(data)
    print(f'Num trees: {trees}')

    part_2_input = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    part_2_output = []
    for slope in part_2_input:
        part_2_output.append(get_num_trees(data, slope[1], slope[0]))

    part_2_output_product = 1
    for output in part_2_output:
        part_2_output_product *= output
    print(part_2_output)
    print(part_2_output_product)

