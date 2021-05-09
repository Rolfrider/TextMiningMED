import pytest
from model.sequence import Sequence
from algorithm.candidates_generation import candidates_diffrent


def test_one():
    seq_a = Sequence([[1, 3]])
    seq_b = Sequence([[1], [3]])
    assert candidates_diffrent(seq_a, seq_b)


def test_two():
    seq_a = Sequence([[1], [3]])
    seq_b = Sequence([[1], [3]])
    assert not candidates_diffrent(seq_a, seq_b)


def test_three():
    seq_a = Sequence([[1, 3]])
    seq_b = Sequence([[3, 1]])
    assert not candidates_diffrent(seq_a, seq_b)


def test_four():
    seq_a = Sequence([[4], [3]])
    seq_b = Sequence([[1], [3]])
    assert candidates_diffrent(seq_a, seq_b)


def test_five():
    seq_a = Sequence([[1], [5]])
    seq_b = Sequence([[1], [3]])
    assert candidates_diffrent(seq_a, seq_b)
