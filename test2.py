#!/usr/bin/env python3
import pytest
from helpers import Opponent, Response, play_round, Outcome, play_round_outcome

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

def test_rock_outcomes():
    opponent_rock = Opponent.A
    outcome_lose = Outcome.X
    outcome_draw = Outcome.Y
    outcome_win = Outcome.Z

    # Opponent rock, we are losing (scissors): scissors are worth 3 points, losing is worth nothing
    assert(play_round_outcome((opponent_rock, outcome_lose)) == 3)
    # Opponent rock, we are drawing (rock): rock is worth 1 points, drawing is worth 3
    assert(play_round_outcome((opponent_rock, outcome_draw)) == 4)
    # Opponent rock, we are winning (paper): paper is worth 2 points, winning is worth 6
    assert(play_round_outcome((opponent_rock, outcome_win)) == 8)

def test_paper_outcomes():
    opponent_paper = Opponent.B
    outcome_lose = Outcome.X
    outcome_draw = Outcome.Y
    outcome_win = Outcome.Z

    # Opponent paper, we are losing (rock): rock is worth 1 points, losing is worth nothing
    assert(play_round_outcome((opponent_paper, outcome_lose)) == 1)
    # Opponent paper, we are drawing (paper): paper is worth 2 points, drawing is worth 3
    assert(play_round_outcome((opponent_paper, outcome_draw)) == 5)
    # Opponent paper, we are winning (scissors): scissors are worth 3 points, winning is worth 6
    assert(play_round_outcome((opponent_paper, outcome_win)) == 9)

def test_scissors_outcome():
    opponent_scissors = Opponent.C
    outcome_lose = Outcome.X
    outcome_draw = Outcome.Y
    outcome_win = Outcome.Z

    # Opponent scissors, we are losing (paper): paper is worth 2 points, losing is worth nothing
    assert(play_round_outcome((opponent_scissors, outcome_lose)) == 2)
    # Opponent scissors, we are drawing (scissors): scissors are worth 3 points, drawing is worth 3
    assert(play_round_outcome((opponent_scissors, outcome_draw)) == 6)
    # Opponent scissors, we are winning (rock): rock is worth 1 points, winning is worth 6
    assert(play_round_outcome((opponent_scissors, outcome_win)) == 7)

