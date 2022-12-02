#!/usr/bin/env python3
import pytest
from helpers import Opponent, Response, play_round

def test_paper_beats_rock():
    opponent_rock = Opponent.A
    opponent_paper = Opponent.B
    response_rock = Response.X
    response_paper = Response.Y

    # rock is worth 1 point, losing is worth nothing
    assert(play_round((opponent_paper, response_rock)) == 1)
    # paper is worth 2 point, winning is worth 6
    assert(play_round((opponent_rock, response_paper)) == 8)

def test_rock_beast_scissors():
    opponent_rock = Opponent.A
    opponent_scissors = Opponent.C
    response_rock = Response.X
    response_scissors = Response.Z

    # scissors are worth 3 point, losing is worth nothing
    assert(play_round((opponent_rock, response_scissors)) == 3)
    # rock is worth 1 point, winning is worth 6
    assert(play_round((opponent_scissors, response_rock)) == 7)

def test_scissors_beast_paper():
    opponent_paper = Opponent.B
    opponent_scissors = Opponent.C
    response_paper = Response.Y
    response_scissors = Response.Z

    # paper is  worth 2 point, losing is worth nothing
    assert(play_round((opponent_scissors, response_paper)) == 2)
    # scissors are worth 3 point, winning is worth 6
    assert(play_round((opponent_paper, response_scissors)) == 9)

def test_all_draws():
    opponent_rock = Opponent.A
    opponent_paper = Opponent.B
    opponent_scissors = Opponent.C
    response_rock = Response.X
    response_paper = Response.Y
    response_scissors = Response.Z

    # rock is worth 1, draw is worth 3
    assert(play_round((opponent_rock, response_rock)) == 4)
    # paper is worth 2, draw is worth 3
    assert(play_round((opponent_paper, response_paper)) == 5)
    # scissors are worth 3, draw is worth 3
    assert(play_round((opponent_scissors, response_scissors)) == 6)
