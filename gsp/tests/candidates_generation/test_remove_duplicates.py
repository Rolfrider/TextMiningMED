import pytest
from model.sequence import Sequence
from algorithm.candidates_generation import remove_duplicates


def test_one():
    initial = [
        Sequence([[1], [2]]),
        Sequence([[1, 2]]),
        Sequence([[2, 1]]),
        Sequence([[2], [1]]),
        Sequence([[2], [3]]),
        Sequence([[2, 3]]),
        Sequence([[3], [1]]),
        Sequence([[3], [2]])
    ]
    expected = [
        Sequence([[1], [2]]),
        Sequence([[1, 2]]),
        Sequence([[2], [1]]),
        Sequence([[2], [3]]),
        Sequence([[2, 3]]),
        Sequence([[3], [1]]),
        Sequence([[3], [2]])
    ]
    result = remove_duplicates(initial)
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_two():
    initial = [
        Sequence([[1, 2], [2]]),
        Sequence([[1, 2], [3]]),
        Sequence([[2, 1], [2]]),
        Sequence([[2, 1], [1]])
    ]
    expected = [
        Sequence([[1, 2], [2]]),
        Sequence([[1, 2], [3]]),
        Sequence([[2, 1], [1]])
    ]
    result = remove_duplicates(initial)
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_three():
    initial = [
        Sequence([[1, 2], [2]]),
        Sequence([[1, 2], [3]]),
        Sequence([[2, 1], [1]])
    ]
    expected = [
        Sequence([[1, 2], [2]]),
        Sequence([[1, 2], [3]]),
        Sequence([[2, 1], [1]])
    ]
    result = remove_duplicates(initial)
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])
