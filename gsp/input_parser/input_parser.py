import sys
from model.sequence import Sequence
from typing import List


def parse_file(file_name: str) -> List[Sequence]:
    result = []
    for line in read_lines(file_name):
        result.append(parse_line(line.rstrip('\n')))
    # return [parse_line(line.rstrip('\n')) for line in read_lines(file_name)]
    return result


def read_lines(file_name: str) -> List[str]:
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    return lines


def parse_line(line: str) -> Sequence:
    divide_sign = ' '
    itemset_end = '-1'
    sequence_end = '-2'
    sequence = Sequence([])
    itemset = list()
    for sign in line.split(divide_sign):
        if sign == itemset_end:
            sequence.itemsets.append(itemset)
            itemset = list()
        elif sign == sequence_end:
            return sequence
        else:
            itemset.append(int(sign))
    return sequence
