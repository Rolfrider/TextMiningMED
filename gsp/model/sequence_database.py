import sys
import math
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
    
    
    def print_sequences(self):
        for sequence in self.sequences:
            print('Sequence '+str(sequence.id) +': '+str(sequence))

    def parse_file(self, file_name: str, support) -> List[Sequence]:
        #self.sequences.append(self.parse_line(line) for line in self.read_lines(file_name))
        for line in self.read_lines(file_name):
            s= self.parse_line(line.rstrip())
            #print(s)
            self.sequences.append(s)
        
        sup = int(math.ceil(support*len(self.sequences))) #czy ok?
        print("Support = " +str(sup))
        frequent_items = self.frequent_patterns.keys()
        for i in list(frequent_items):
            #print(i)
            pat = self.frequent_patterns.get(i)
            #print(len(self.frequent_patterns))
            if pat.support < sup:
                self.frequent_patterns.pop(i)
            #print(len(self.frequent_patterns))
            #print('---------')
        self.update_sequences(self.frequent_patterns.keys())

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
                #itemset.add(int(sign))
                item = self.i_factory.get_item(int(sign))
                pattern = self.frequent_patterns.get(item)
                if pattern == None:
                    pattern = self.p_factory.create_pattern(sequence_ids=[sequence.id],elements=item)
                    self.frequent_patterns[item] = pattern
                else:
                    pattern.support+=1
                #print(str(item))
                itemset.add(item)
                #print(itemset)
        return sequence
    
    def update_sequences(self, items):
        for sequence in self.sequences:
            for itemset in sequence.itemsets:
                for item in itemset.copy():
                    if self.frequent_patterns.get(item) == None:
                        #print('Itemset before updating '+ str(itemset))
                        itemset.remove(item)
                        #print('Removed item '+ str(item))
                        #print('Itemset after updating '+ str(itemset))
    
    def get_frequent_items(self):
        result = {k: v for k, v in sorted(self.frequent_patterns.items(), key=lambda item: item[0].value)}
        #print(list(result.keys())[6])
        return result
        
