#!/usr/bin/env python3

def check_buffer(buffer):
    for char in buffer:
        count = buffer.count(char)
        if count > 1:
            return False
    return True

if __name__ == "__main__":
    # file_name = "day6_test.input"
    file_name = "day6.input"
    with open(file_name, "r") as input_file:
        for row in input_file.readlines():
            buffer = row[0:14]
            for index, char in enumerate(row):
                if check_buffer(buffer):
                    print(index)
                    break
                buffer = buffer[1:] + char

