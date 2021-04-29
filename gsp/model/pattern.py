from typing import List, Set

from model.item import Item
from model.sequence import Sequence


class Pattern:
    def __init__(self, sequence_ids=[], elements=[]):
        self.elements: Sequence = elements
        self.sequence_ids:List[string] = sequence_ids
        self.support = len(self.sequence_ids) #czy ok??

    def __str__(self) -> str:
        return ' '.join(str(i) for i in self.elements)
