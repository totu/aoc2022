#!/usr/bin/env python3
if __name__ == "__main__":
    # file_name = "day8_test.input"
    file_name = "day8.input"

    grid = []
    with open(file_name, "r") as input_file:
        for row in input_file.readlines():
            grid.append([x for x in map(int, row.strip())])

    dimensions = (len(grid), len(grid[0]))
    trees_on_the_edge = dimensions[0] * 2 + (dimensions[1] - 2) * 2
    print(dimensions, trees_on_the_edge)

    # for row in grid:
    #     print(row)

    # print("".join(["*"]*10))

    pos = 1
    visible = 0
    for row_id, row in enumerate(grid[1:-1]):
        row = row[1:-1]
        for index, tree in enumerate(row):
            home_row = grid[row_id+1]
            home_column = [x[index+1] for x in grid]

            left_of_tree = home_row[:index+1]
            right_of_tree = home_row[index+2:]
            above_tree = home_column[:row_id+1]
            below_tree = home_column[row_id+2:]

            home_row = "".join(map(str, left_of_tree)) + f"\033[33m{tree}\033[0m" + "".join(map(str, right_of_tree))
            home_column = "".join(map(str, above_tree)) + f"\033[33m{tree}\033[0m" + "".join(map(str, below_tree))

            if max(left_of_tree) < tree or max(right_of_tree) < tree or max(above_tree) < tree or max(below_tree) < tree:
                visible += 1
            # print(pos, tree, home_row, home_column)
            pos += 1

    print(trees_on_the_edge + visible)
