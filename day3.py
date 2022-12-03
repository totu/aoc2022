#!/usr/bin/env python3
from string import ascii_letters

if __name__ == "__main__":
    # file_name = "day3_test.input"
    file_name = "day3.input"
    rucksacks = []
    with open(file_name, "r") as input_file:
        rucksacks = input_file.readlines()

    total_priority = 0

    for rucksack in rucksacks:
        # Split pockets
        item_count = len(rucksack)
        pocket1 = rucksack[:item_count//2]
        pocket2 = rucksack[item_count//2:]
        assert rucksack == pocket1 + pocket2, "wat"

        # Go through pockets
        thing = str()
        for thing in pocket1:
            if thing in pocket2:
                break

        # Calculate priority on item
        priority = ascii_letters.index(thing) + 1
        total_priority += priority

    print(total_priority)

