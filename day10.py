#!/usr/bin/env python3
if __name__ == "__main__":
    # file_name = "day10_simple.input"
    # file_name = "day10_test.input"
    file_name = "day10.input"

    cycle = 0
    X = 1
    cycle_values: list[tuple[int, int]] = [(1,1)]
    with open(file_name, "r") as input_file:
        for instruction in input_file.readlines():
            instruction = instruction.strip()
            value = str()
            if " " in instruction:
                instruction, value = instruction.split(" ")

            match instruction:
                case "noop":
                    cycle += 1
                    cycle_values.append((cycle,X))
                case "addx":
                    cycle += 1
                    cycle_values.append((cycle,X))
                    cycle += 1
                    cycle_values.append((cycle,X))
                    X += int(value)


    x_value_every_40_cycles_starting_from_cycle_20 = [x for x in cycle_values[20::40]]
    print(x_value_every_40_cycles_starting_from_cycle_20)


    total_signal_strength = 0
    for cycle, val in x_value_every_40_cycles_starting_from_cycle_20:
        signal_strength = cycle * val
        print(cycle, val, signal_strength)
        total_signal_strength += signal_strength

    print(total_signal_strength)
