from typing import Optional, Dict, List


def sort_dict_by_value(x: Dict) -> Dict:
    return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}


def parse_elfs(file_name: str) -> Dict:
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


def most_calories(elfs: Dict, how_many: Optional[int] = 1) -> List:
    sorted_elfs = sort_dict_by_value(elfs)
    return list(reversed(sorted_elfs.keys()))[:how_many]
