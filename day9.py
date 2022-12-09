#!/usr/bin/env python3
import math
if __name__ == "__main__":
    # file_name = "day9_test.input"
    file_name = "day9.input"

    h = [0, 0]
    t = [0, 0]
    all_t_pos: list[list[int]] = []
    with open(file_name, "r") as input_file:
        change = (0, 0)
        for row in input_file.readlines():
            _dir, amount = row.strip().split(" ")
            match _dir:
                case "R":
                    change = (1, 0)
                case "L":
                    change = (-1, 0)
                case "D":
                    change = (0, -1)
                case "U":
                    change = (0, 1)

            # print(change, amount)
            for i, c in enumerate(change):
                for x in range(1, int(amount)+1):
                    last_h = list(h)
                    h[i] += c
                    # print("h:", h)

                    # diff
                    x_delta = h[0] - t[0]
                    y_delta = h[1] - t[1]
                    # print(x_delta, y_delta, math.sqrt(x_delta**2 + y_delta**2), t, h, last_h)
                    if math.sqrt(x_delta**2 + y_delta**2) >= 2:
                        t = list(last_h)
                        all_t_pos.append(t)

        # print(all_t_pos)
        max_x = max([x[0] for x in all_t_pos])
        max_y = max([x[1] for x in all_t_pos])

        grid = []
        for y in range(max_y+1):
            row = []
            for x in range(max_x+1):
                mark = "."
                if [x, y] == [0, 0]:
                    mark = "s"
                if [x, y] in all_t_pos:
                    mark = "#"
                row.append(mark)
            grid.append(row)


        for row in reversed(grid):
            print("".join(row))

        # only count unique positions
        unique_t_pos = set([tuple(x) for x in all_t_pos])
        # add starting position
        print(len(unique_t_pos) + 1)

