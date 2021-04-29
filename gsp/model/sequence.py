import time
from typing import List, Set

from model.item import Item

class Sequence:
    def __init__(self):
        self.itemsets: List[Set[Item]] = []
        self.id = self.__hash__()

    def __str__(self) -> str:
        #return self.itemsets.__str__()
        return ' '.join(str(it) for i in self.itemsets for it in i)+'\n'
    
    def __key(self):
        return (tuple(self.itemsets), str(time.time()).encode('utf-8'))
    
    def __hash__(self):
        return abs(hash(str(self.__key())))
        
    def __eq__(self, other):
        if isinstance(other, Sequence):
            return self.__key() == other.__key()
        return NotImplemented
