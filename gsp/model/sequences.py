import time
from typing import List, Set

from model.pattern import Pattern

class Sequences:
    def __init__(self):
        self.levels: List[List[Pattern]] = [List[Pattern]]
        self.number_of_frequent_sequences = 0
        self.description: string = ''

    def __str__(self) -> str:
        str = ''
        lvl_cnt = 0
        for l in levels:
            str+'Level '+str(lvl_cnt)+'\n'
            for s in l:
                str+='\n' #dodać== drukowanie sekwencji
            lvl_cnt+=1
        return str
    
    def add_sequence(self, sequence, level):
        #print(sequence)
        if len(self.levels) <= level:
            while len(self.levels) <= level:
                if len(self.levels) == level:
                    self.levels.append([sequence])
        else:
            self.levels[level].append(sequence)
        self.number_of_frequent_sequences+=1
    
    def add_sequences(self, sequences, level):
        #print(sequences.values())
        #print(self.levels)
        for s in sequences.values():
            self.add_sequence(s, level)
        #print(self.levels)
        #print(self.levels[1][1].elements)
