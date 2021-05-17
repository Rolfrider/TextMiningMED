import pytest
from model.sequence import Sequence
from algorithm.candidates_generation import CandidateGenerator


@pytest.fixture
def candidates_generator():
    '''Returns CandidatesGenerator instance'''
    return CandidateGenerator()


def test_single_item_seq(candidates_generator):
    sequences = [
        Sequence([[1]]),
        Sequence([[2]]),
        Sequence([[3]])
    ]
    result = candidates_generator.generate_candidates(sequences)
    expected = [
        Sequence([[1], [1]]),
        Sequence([[1], [2]]),
        Sequence([[1, 2]]),
        Sequence([[1], [3]]),
        Sequence([[1, 3]]),
        Sequence([[2], [1]]),
        Sequence([[2], [2]]),
        Sequence([[2], [3]]),
        Sequence([[2, 3]]),
        Sequence([[3], [1]]),
        Sequence([[3], [2]]),
        Sequence([[3], [3]])
    ]
    # assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_two_creates_two(candidates_generator):
    sequences = [
        Sequence([[1], [2]]),
        Sequence([[2], [1]])
    ]
    result = candidates_generator.generate_candidates(sequences)
    expected = [
        Sequence([[1], [2], [1]]),
        Sequence([[2], [1], [2]])
    ]
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_two_creates_one(candidates_generator):
    sequences = [
        Sequence([[1], [2]]),
        Sequence([[2, 3]]),
    ]
    result = candidates_generator.generate_candidates(sequences)
    expected = [
        Sequence([[1], [2, 3]])
    ]
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_two_creates_one_variant_2(candidates_generator):
    sequences = [
        Sequence([[1], [2]]),
        Sequence([[3, 1]]),
    ]
    result = candidates_generator.generate_candidates(sequences)
    expected = [
        Sequence([[3, 1], [2]])
    ]
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_two_creates_one_separate(candidates_generator):
    sequences = [
        Sequence([[1], [2]]),
        Sequence([[2], [3]]),
    ]
    result = candidates_generator.generate_candidates(sequences)
    expected = [
        Sequence([[1], [2], [3]])
    ]
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_two_creates_one_separate_variant_2(candidates_generator):
    sequences = [
        Sequence([[1], [2]]),
        Sequence([[3], [1]]),
    ]
    result = candidates_generator.generate_candidates(sequences)
    expected = [
        Sequence([[3], [1], [2]])
    ]
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_two_creates_zero(candidates_generator):
    sequences = [
        Sequence([[1], [2]]),
        Sequence([[4], [3]]),
    ]
    result = candidates_generator.generate_candidates(sequences)
    expected = []
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_three_one(candidates_generator):
    sequences = [
        Sequence([[1], [2], [2, 1]]),
        Sequence([[2], [2, 1], [3]])
    ]
    result = candidates_generator.generate_candidates(sequences)
    expected = [
        Sequence([[1], [2], [2, 1], [3]])
    ]
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_three_two(candidates_generator):
    sequences = [
        Sequence([[1], [2], [3, 1]]),
        Sequence([[2, 3], [1], [3]])
    ]
    result = candidates_generator.generate_candidates(sequences)
    expected = [
        Sequence([[1], [2], [3, 1], [3]])
    ]
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])
