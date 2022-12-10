#!/usr/bin/env python3
class CRT():
    def __init__(self):
        self.width = 40
        self.height = 6
        self.row = 0
        self.col = 0
        self.screen: list[list[str]] = []
        for _ in range(self.height):
            self.screen.append([" " for _ in range(self.width)])


if __name__ == "__main__":
    # file_name = "day10_simple.input"
    # file_name = "day10_test.input"
    file_name = "day10.input"

    crt = CRT()
    cycle = 0
    x = 1
    cycle_values: list[tuple[int, int]] = [(1,1)]
    with open(file_name, "r") as input_file:
        for instruction in input_file.readlines():
            instruction = instruction.strip()
            value = str()
            if " " in instruction:
                instruction, value = instruction.split(" ")

            def draw_crt(crt):
                if crt.col == x or crt.col -1 == x or crt.col + 1 == x:
                    mark = "#"
                    crt.screen[crt.row][crt.col] = mark

                crt.col += 1
                if crt.col == crt.width:
                    crt.col = 0
                    crt.row += 1


            match instruction:
                case "noop":
                    cycle += 1
                    cycle_values.append((cycle, x))
                    draw_crt(crt)
                case "addx":
                    cycle += 1
                    cycle_values.append((cycle, x))
                    draw_crt(crt)
                    cycle += 1
                    cycle_values.append((cycle, x))
                    draw_crt(crt)
                    x += int(value)


    x_value_every_40_cycles_starting_from_cycle_20 = [x for x in cycle_values[20::40]]
    # print(x_value_every_40_cycles_starting_from_cycle_20)


    total_signal_strength = 0
    for cycle, val in x_value_every_40_cycles_starting_from_cycle_20:
        signal_strength = cycle * val
        # print(cycle, val, signal_strength)
        total_signal_strength += signal_strength

    print(total_signal_strength)

    for row in crt.screen:
        print("".join(row))
