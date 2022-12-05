#!/usr/bin/env python3
from helpers import parse_top_crates

if __name__ == "__main__":
    # file_name = "day5_test.input"
    file_name = "day5.input"
    print(parse_top_crates(file_name, retain_order=True))
