#!/usr/bin/env python3
if __name__ == "__main__":
    # file_name = "day4_test.input"
    file_name = "day4.input"
    pairs = []
    with open(file_name, "r") as input_file:
        pairs = input_file.readlines()

    total_fully_contained_sections = 0
    for pair in pairs:
        first, second = pair.split(",")
        first = [x for x in map(int, first.split("-"))]
        second = [x for x in map(int, second.split("-"))]

        # find possible intersection points
        starting_section = max(first[0], second[0])
        ending_section = min(first[1], second[1])
        # run points through range() and see if we get something (negative ranges don't have lenght)
        # also add +1 to ending_section since range it exclusive on the end
        over_laps = len(range(starting_section, ending_section + 1))
        if over_laps:
            total_fully_contained_sections += 1

    print(total_fully_contained_sections)
