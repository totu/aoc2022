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

        if first[0] >= second[0] and first[1] <= second[1] or second[0] >= first[0] and second[1] <= first[1]:
            print(first, second)
            total_fully_contained_sections += 1

    print(total_fully_contained_sections)

