def parse_elfs(file_name):
    elfs = {}
    with open(file_name, "r") as input_file:
        current_elf = 1
        for row in input_file.readlines():
            if row.strip() == "":
                current_elf += 1
                continue
            if current_elf in elfs:
                elfs[current_elf] += int(row)
            else:
                elfs[current_elf] = int(row)
    return elfs


def most_calories(elfs):
    highest_calory_count = max(elfs.values())
    return [x[0] for x in elfs.items() if x[1] == highest_calory_count][0]
