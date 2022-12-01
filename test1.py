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
    assert elf_carrying_most_calories == [4]


def test_most_calories_with_3_elfs(elfs):
    elfs_carrying_most_calories = most_calories(elfs, how_many=3)
    assert elfs_carrying_most_calories == [4, 3, 5]


def test_how_many_calories_elf_is_carrying(elfs):
    elf_carrying_most_calories = most_calories(elfs)[0]
    calories_carried = elfs[elf_carrying_most_calories]
    assert calories_carried == 24000

def test_how_many_calories_top3_elfs_are_carrying(elfs):
    elfs_carrying_most_calories = most_calories(elfs, how_many=3)
    calories_carried = sum([elfs[elf] for elf in elfs_carrying_most_calories])
    assert calories_carried == 24000 + 11000 + 10000
