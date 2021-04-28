from typing import List, Set

from model.item import Item

class Sequence:
    def __init__(self):
        self.itemsets: List[Set[Item]] = []
        self.id = hash(self)

    def __str__(self) -> str:
        return self.itemsets.__str__()
    
    def __hash__(self):
        h = abs(hash(str(self.itemsets)))
        #print(h)
        return h
        
    def __eq__(self, other):
        if isinstance(other, Sequence):
            return self.itemsets == other_item.itemsets
        return NotImplemented
