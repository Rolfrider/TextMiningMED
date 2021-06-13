import sys
from model.sequence import Sequence
from typing import List


def parse_file(file_name: str) -> List[Sequence]:
    result = []
    divide_sign = ' '
    itemset_end = '-1'
    sequence_end = '-2'
    sequence = Sequence([])
    itemset = list()
    for line in read_lines(file_name):
        for sign in line.rstrip('\n').split(divide_sign):
            if sign == itemset_end:
                sequence.itemsets.append(itemset)
                itemset = list()
            elif sign == sequence_end:
                result.append(sequence)
                sequence.calc_all_items()
                sequence = Sequence([])
            elif sign == '':
                continue
            else:
                itemset.append(int(sign))
    return result


def read_lines(file_name: str) -> List[str]:
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    return lines


def parse_seq(line: str) -> Sequence:
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
    sequence.calc_all_items()
    return sequence
