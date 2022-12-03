#!/usr/bin/env python3
from string import ascii_letters

if __name__ == "__main__":
    # file_name = "day3_test.input"
    file_name = "day3.input"
    rucksacks = []
    with open(file_name, "r") as input_file:
        rucksacks = input_file.readlines()

    total_priority = 0

    for index in range(0, len(rucksacks), 3):
        rucksack1 = rucksacks[index]
        rucksack2 = rucksacks[index + 1]
        rucksack3 = rucksacks[index + 2]
        thing = str()
        for thing in rucksack1:
            if thing in rucksack2 and thing in rucksack3:
                break

        # Calculate priority on item
        priority = ascii_letters.index(thing) + 1
        total_priority += priority

    print(total_priority)
