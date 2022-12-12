#!/usr/bin/env python3
import copy

def get_val(grid: list[list[int]], coords: tuple[int, int]) -> int:
    if -1 in coords:
        return 0
    try:
        val = grid[coords[1]][coords[0]]
        return val
    except IndexError:
        return 0

def get_move_choices(grid: list[list[int]], coords: tuple[int, int]) -> list[tuple[int, tuple[int, int]]]:
    left = (coords[0]-1, coords[1])
    right = (coords[0]+1, coords[1])
    up = (coords[0], coords[1]-1)
    down = (coords[0], coords[1]+1)

    left_val = get_val(grid, left)
    right_val = get_val(grid, right)
    up_val = get_val(grid, up)
    down_val = get_val(grid, down)
    # print(left, right, up, down)
    # print(left_val, right_val, up_val, down_val)
    move_choices = [(left_val, left), (right_val, right), (up_val, up), (down_val, down)]
    return move_choices

def parse_grid(file_name: str) -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    grid: list[list[int]] = []
    start: tuple[int, int] = (0, 0)
    end: tuple[int, int] = (0, 0)

    with open(file_name, "r") as input_file:
        for row_id, row in enumerate(input_file.readlines()):
            if "S" in row:
                column_id = row.index("S")
                row = row.replace("S", "a")
                start = (column_id, row_id)
            elif "E" in row:
                column_id = row.index("E")
                row = row.replace("E", "z")
                end = (column_id, row_id)

            row = row.strip()
            grid.append([x for x in map(ord, row)])

    return grid, start, end

def find_path(grid: list[list[int]], _from: tuple[int,int], to: tuple[int,int]) -> list[list[tuple[int, tuple[int, int]]]]:
    val1 = get_val(grid, _from)
    val2 = get_val(grid, to)
    if val1 < val2:
        start_val = val1
        start = _from
        end = to
    else:
        start_val = val2
        start = to
        end = _from

    paths: list[list[tuple[int, tuple[int, int]]]] = []
    new_paths: list[list[tuple[int, tuple[int, int]]]] = []
    good_paths: list[list[tuple[int, tuple[int, int]]]] = []
    # bad_paths: list[list[tuple[int, tuple[int, int]]]] = []

    paths.append([(start_val, start)])
    import math
    best_path = math.inf
    while paths:
        print(len(paths))
        for path in paths:
            if len(path) > best_path:
                continue

            coords = path[-1][1]
            current_val = path[-1][0]
            move_choices = get_move_choices(grid, coords)

            for choice in move_choices:
                if choice[0] == current_val or choice[0] == current_val + 1:
                    if choice[1] == end:
                        good_paths.append(path)
                    elif choice in path:
                        pass
                        #bad_paths.append(path + [choice])
                    else:
                        new_paths.append(path + [choice])

        paths = copy.deepcopy(new_paths)
        new_paths = []

    return good_paths

if __name__ == "__main__":
    # file_name = "day12_test.input"
    file_name = "day12.input"

    grid, start, end = parse_grid(file_name)
    good_paths = find_path(grid, start, end)

    shortest_path = good_paths[0]
    for path in good_paths[1:]:
        if len(path) < len(shortest_path):
            shortest_path = path

    print(len(shortest_path))
    # for path in bad_paths:
    #     print(path)
    #     print("***")
    # for g in grid:
    #     print(g)

    # print(start, end)
