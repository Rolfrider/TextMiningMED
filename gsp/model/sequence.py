from typing import List, Set


class Sequence:
    def __init__(self, itemsets: List[Set[int]] = []):
        self.itemsets = itemsets

    def __str__(self) -> str:
        return self.itemsets.__str__()

    def __eq__(self, other) -> bool:
