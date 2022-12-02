from typing import Optional, Dict, List, Tuple
from enum import Enum, auto


class Opponent(Enum):
    A = "rock"
    B = "paper"
    C = "scissors"


class Response(Enum):
    X = "rock"
    Y = "paper"
    Z = "scissors"

class Outcome(Enum):
    X = "lose"
    Y = "draw"
    Z = "win"



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


def play_round(_round: Tuple[Enum, Enum]) -> int:
    RPS = {
        "rock": {
            "paper": 0,
            "rock": 3,
            "scissors": 6,
            "worth": 1,
        },
        "paper": {
            "paper": 3,
            "rock": 6,
            "scissors": 0,
            "worth": 2,
        },
        "scissors": {
            "paper": 6,
            "rock": 0,
            "scissors": 3,
            "worth": 3,
        },
    }

    opponent = _round[0]
    response = _round[1]
    points = RPS[response.value][opponent.value] + RPS[response.value]["worth"]
    return points

def play_round_outcome(_round: Tuple[Enum, Enum]) -> int:
    RPS = {
        "rock": {
            "win": 6 + 2, # we are paper (2 points)
            "lose": 3, # we are scissors (3 points)
            "draw": 3 + 1 # we are rock (1 points)
        },
        "paper": {
            "win": 6 + 3, # we are scissors (3 points)
            "lose": 1, # we are rock (1 points)
            "draw": 3 + 2, # we are paper (2 points)
        },
        "scissors": {
            "win": 6 + 1, # we are rock (1 points)
            "lose": 2, # we are paper (2 points)
            "draw": 3 + 3, # we are scissors (3 points)
        },
    }

    opponent = _round[0]
    outcome = _round[1]
    points = RPS[opponent.value][outcome.value]
    return points
