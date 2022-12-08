#!/usr/bin/env python3
if __name__ == "__main__":
    # file_name = "day8_test.input"
    file_name = "day8.input"

    grid: list[list[int]] = []
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
    highest_scenic = 0
    for row_id, row in enumerate(grid[1:-1]):
        row = row[1:-1]
        for index, tree in enumerate(row):
            home_row = grid[row_id + 1]
            home_column = [x[index + 1] for x in grid]

            left_of_tree = home_row[: index + 1]
            right_of_tree = home_row[index + 2 :]
            above_of_tree = home_column[: row_id + 1]
            below_of_tree = home_column[row_id + 2 :]

            home_row = (
                "".join(map(str, left_of_tree))
                + f"\033[33m{tree}\033[0m"
                + "".join(map(str, right_of_tree))
            )
            home_column = (
                "".join(map(str, above_of_tree))
                + f"\033[33m{tree}\033[0m"
                + "".join(map(str, below_of_tree))
            )

            if (
                max(left_of_tree) < tree
                or max(right_of_tree) < tree
                or max(above_of_tree) < tree
                or max(below_of_tree) < tree
            ):
                visible += 1
            # print(pos, tree, home_row, home_column)
            pos += 1

            def count_trees(trees: list[int], tree: int) -> int:
                count = 0
                for t in trees:
                    if t < tree:
                        count += 1
                    if t >= tree:
                        count += 1
                        break

                return count

            trees_on_left = count_trees(list(reversed(left_of_tree)), tree)
            trees_on_right = count_trees(right_of_tree, tree)
            trees_on_above = count_trees(list(reversed(above_of_tree)), tree)
            trees_on_below = count_trees(below_of_tree, tree)
            scenic_score = (
                trees_on_left * trees_on_above * trees_on_below * trees_on_right
            )

            # print(trees_on_left, list(reversed(left_of_tree)), scenic_score, tree)
            # print(trees_on_right, right_of_tree, scenic_score, tree)
            # print(trees_on_above, list(reversed(above_of_tree)), scenic_score, tree)
            # print(trees_on_below, below_of_tree, scenic_score, tree)
            # print("*****")

            if scenic_score > highest_scenic:
                highest_scenic = scenic_score

    print(trees_on_the_edge + visible)
    print(f"hi: {highest_scenic}")
