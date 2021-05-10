import pytest
from model.sequence import Sequence
from algorithm.support_counting import count_support


def test_one():
    candidate = Sequence([[1], [2]])
    seq = [
        Sequence([[1], [1, 2, 3], [1, 3], [4], [3, 6]]),
        Sequence([[1, 4], [3], [2, 3], [1, 5]]),
        Sequence([[5, 6], [1, 2], [4, 6], [3], [2]]),
        Sequence([[5], [7], [1, 6], [3], [2], [3]])
    ]
    result = count_support(candidate, seq)
    assert result[0] == candidate
    assert result[1] == 4


def test_two():
    candidate = Sequence([[1, 2]])
    seq = [
        Sequence([[1], [1, 2, 3], [1, 3], [4], [3, 6]]),
        Sequence([[1, 4], [3], [2, 3], [1, 5]]),
        Sequence([[5, 6], [1, 2], [4, 6], [3], [2]]),
        Sequence([[5], [7], [1, 6], [3], [2], [3]])
    ]
    result = count_support(candidate, seq)
    assert result[0] == candidate
    assert result[1] == 2


def test_three():
    candidate = Sequence([[1, 2], [3]])
    seq = [
        Sequence([[1], [1, 2, 3], [1, 3], [4], [3, 6]]),
        Sequence([[1, 4], [3], [2, 3], [1, 5]]),
        Sequence([[5, 6], [1, 2], [4, 6], [3], [2]]),
        Sequence([[5], [7], [1, 6], [3], [2], [3]])
    ]
    result = count_support(candidate, seq)
    assert result[0] == candidate
    assert result[1] == 2


def test_four():
    candidate = Sequence([[1], [2], [3]])
    seq = [
        Sequence([[1], [1, 2, 3], [1, 3], [4], [3, 6]]),
        Sequence([[1, 4], [3], [2, 3], [1, 5]]),
        Sequence([[5, 6], [1, 2], [4, 6], [3], [2]]),
        Sequence([[5], [7], [1, 6], [3], [2], [3]])
    ]
    result = count_support(candidate, seq)
    assert result[0] == candidate
    assert result[1] == 2
