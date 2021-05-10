import pytest
from model.sequence import Sequence
from input_parser.input_parser import parse_line


def test_parse_line():
    line = "1 -1 1 2 3 -1 1 3 -1 4 -1 3 6 -1 -2"
    result = parse_line(line)
    expected_seq = Sequence([[1], [1, 2, 3], [1, 3], [4], [3, 6]])
    assert result == expected_seq
