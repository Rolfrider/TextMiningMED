import sys
from model.sequence import Sequence
from typing import List


def parse_file(file_name: str) -> List[Sequence]:
    return [parse_line(line) for line in read_lines(file_name)]


def read_lines(file_name: str) -> List[str]:
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    return lines


def parse_line(line: str) -> Sequence:
    divide_sign = ' '
    itemset_end = '-1'
    sequence_end = '-2'
    sequence = Sequence()
    itemset = set()
    for sign in line.split(divide_sign):
        if sign == itemset_end:
            sequence.itemsets.append(itemset)
            itemset = set()
        elif sign == sequence_end:
            return sequence
        else:
            itemset.add(int(sign))
    return sequence
