#!/usr/bin/env python3
from helpers import parse_elfs, most_calories


if __name__ == "__main__":
    elfs = parse_elfs("day1.input")
    elfs_carrying_most_calories = most_calories(elfs)
    calories_carried = elfs[elfs_carrying_most_calories[0]]
    print(f"calories carried by top elf: {calories_carried}")
    elfs_carrying_most_calories = most_calories(elfs, how_many=3)
    calories_carried = sum([elfs[elf] for elf in elfs_carrying_most_calories])
    print(f"calories carried by top3 elfs: {calories_carried}")
