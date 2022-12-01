#!/usr/bin/env python3
import pytest
from helpers import parse_elfs, most_calories


@pytest.fixture
def elfs():
    return parse_elfs("day1_test.input")


def test_parse_elfs(elfs):
    expected_elfs = {
        1: 6000,
        2: 4000,
        3: 11000,
        4: 24000,
        5: 10000,
    }
    assert elfs == expected_elfs


def test_most_calories(elfs):
    elf_carrying_most_calories = most_calories(elfs)
    assert elf_carrying_most_calories == 4


def test_how_many_calories_elf_is_carrying(elfs):
    elf_carrying_most_calories = most_calories(elfs)
    calories_carried = elfs[elf_carrying_most_calories]
    assert calories_carried == 24000
