from typing import List, Set


class Sequence:
    def __init__(self):
        self.itemsets: List[Set[int]] = []

    def __str__(self) -> str:
        return self.itemsets.__str__()
