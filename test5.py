#!/usr/bin/env python3
import pytest
from helpers import (
    parse_crate_move_instruction,
    parse_move_instructions,
    parse_stacks,
    get_top_crates,
    parse_top_crates,
)


@pytest.fixture
def stacks():
    return parse_stacks("day5_test.input")


def test_parse_stacks(stacks):
    expected_stacks = {
        0: ["N", "Z"],
        1: ["D", "C", "M"],
        2: ["P"],
    }
    assert stacks == expected_stacks


def test_parse_instruction():
    instructions = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]
    expected_insturctions = [(1, 1, 0), (3, 0, 2), (2, 1, 0), (1, 0, 1)]
    for index, instruction in enumerate(instructions):
        assert parse_crate_move_instruction(instruction) == expected_insturctions[index]


def test_move_instruction(stacks):
    amount, _from, to = parse_crate_move_instruction("move 1 from 2 to 1")
    stacks[to] = stacks[_from][:amount] + stacks[to]
    stacks[_from] = stacks[_from][amount:]

    expected_stacks = {
        0: ["D", "N", "Z"],
        1: ["C", "M"],
        2: ["P"],
    }
    assert expected_stacks == stacks


def test_read_move_instructions_from_file():
    instructions = parse_move_instructions("day5_test.input")
    expected_insturctions = [(1, 1, 0), (3, 0, 2), (2, 1, 0), (1, 0, 1)]
    assert expected_insturctions == instructions


def test_reading_top_crates(stacks):
    top_crates = get_top_crates(stacks)
    assert top_crates == "NDP"


def test_parse_top_crates():
    assert "CMZ" == parse_top_crates("day5_test.input")


def test_parse_top_crates_with_cratemover_9001():
    assert "MCD" == parse_top_crates("day5_test.input", retain_order=True)
