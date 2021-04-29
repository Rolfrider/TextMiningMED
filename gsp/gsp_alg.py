import math
import time
from typing import List, Set

from model.sequences import Sequences
from model.pattern import Pattern

class GSP():
    def __init__(self, min_support, min_gap, max_gap, window_size):
        self.min_support = min_support
        self.min_gap = min_gap
        self.max_gap = max_gap
        self.window_size = window_size
        self.patterns = Sequences()
    def run(self, seqDB):
        sup = int(math.ceil(self.min_support*len(seqDB.sequences)))
        if sup<1:
            sup = 1
        #print(sup)
        self.gsp(seqDB)
        return self.patterns
        
    def gsp(self, seqDB):
        frequent_items = seqDB.get_frequent_items()
        #print(frequent_items)
        #print(frequent_items)
        self.patterns.add_sequences(frequent_items, 1)
    def print_statistics():
        pass
