from typing import List, Set
from model.item import Item


class Pattern:
    def __init__(self, sequence_ids=[], elements=[]):
        self.elements: List[Set[Item]] = elements
        self.sequence_ids:List[string] = sequence_ids
        self.support = len(self.sequence_ids) #czy ok??

    def __str__(self) -> str:
        return self.elements.__str__()
