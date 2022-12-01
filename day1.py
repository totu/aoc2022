#!/usr/bin/env python3
from helpers import parse_elfs, most_calories


if __name__ == "__main__":
    elfs = parse_elfs("day1.input")
    elf_carrying_most_calories = most_calories(elfs)
    calories_carried = elfs[elf_carrying_most_calories]
    print(calories_carried)
