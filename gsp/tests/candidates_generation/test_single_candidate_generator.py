import pytest
from model.sequence import Sequence
from algorithm.candidates_generation import SingleCandidatesGenerator


@pytest.fixture
def single_candidates_generator():
    '''Returns SingleCandidatesGenerator instance'''
    return SingleCandidatesGenerator()


def test_creates_valid_candidates(single_candidates_generator):
    sequences = [
        Sequence([{1}, {2, 3}]),
        Sequence([{4, 5}, {6}])
    ]
    result = single_candidates_generator.generate_candidates(sequences)
    print(result)
    expected = [
        Sequence([{1}]),
        Sequence([{2}]),
        Sequence([{3}]),
        Sequence([{4}]),
        Sequence([{5}]),
        Sequence([{6}])
    ]
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])


def test_items_repetitions(single_candidates_generator):
    sequences = [
        Sequence([{1}, {2, 3}]),
        Sequence([{4, 5}, {2}])
    ]
    result = single_candidates_generator.generate_candidates(sequences)
    print(result)
    expected = [
        Sequence([{1}]),
        Sequence([{2}]),
        Sequence([{3}]),
        Sequence([{4}]),
        Sequence([{5}])
    ]
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(result, expected)])
