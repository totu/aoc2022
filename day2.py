#!/usr/bin/env python3
from helpers import Opponent, Outcome, play_round_outcome

if __name__ == "__main__":
    # file_name = "day2_test.input"
    file_name = "day2.input"
    with open(file_name, "r") as input_file:
        rounds = [x.replace("\n", "").split(" ") for x in input_file.readlines()]
        rounds = [(Opponent[x[0]], Outcome[x[1]]) for x in rounds]

        total_points = 0
        for _round in rounds:
            points = play_round_outcome(_round)
            total_points += points

        print(total_points)
