from typing import List, Set
from model.item import Item


class Pattern:
    def __init__(self, sequence_ids=None, elements=None):
        if elements==None:
            self.elements: List[Set[Item]] = []
            self.sequence_ids:List[Set[string]] = []
        else:
            self.elements: List[Set[Item]] = elements
            self.sequence_ids:List[Set[string]] = sequence_ids

    def __str__(self) -> str:
        return self.itemsets.__str__()
