import time
from typing import List, Set

from model.pattern import Pattern

class Sequences:
    def __init__(self):
        self.levels: List[List[Pattern]] = [[Pattern()]] #tu chyba średnio (level 0)
        self.number_of_frequent_sequences = 0
        self.description: string = ''

    def __str__(self) -> str:
        result =''
        idx = 0
        for l in self.levels:
            result+='Level '+str(idx)
            result+='\n'
            for p in l:
                result+=str(p)+' '
            result+='\n'
            idx+=1
        return result
        
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
