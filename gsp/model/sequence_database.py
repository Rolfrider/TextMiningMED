import sys
from typing import List, Set

from model.sequence import Sequence
from model.item_factory import ItemFactory
from model.pattern_factory import PatternFactory

class SequenceDB:
    def __init__(self):
        self.sequences :List[Sequence] = []
        self.frequent_patterns = {}
        self.p_factory = PatternFactory()
        self.i_factory = ItemFactory()
    
    def first_pass(self):
        for sequence in self.sequences:
            for item in sequence.itemsets:
                pass
    
    def print_sequences(self):
        for sequence in self.sequences:
            print(sequence)

    def parse_file(self, file_name: str) -> List[Sequence]:
        #self.sequences.append(self.parse_line(line) for line in self.read_lines(file_name))
        for line in self.read_lines(file_name):
            s= self.parse_line(line)
            self.sequences.append(s)


    def read_lines(self, file_name: str) -> List[str]:
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()
        return lines


    def parse_line(self, line: str) -> Sequence:
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
                item = self.i_factory.get_item(int(sign))
                pattern = self.frequent_patterns.get(item)
                if pattern == None:
                    pattern = self.p_factory.create_pattern(item, sequence.id)
                    self.frequent_patterns[item] = pattern
        return sequence
