from typing import List, Set
import itertools
import uuid


class Sequence:
    def __init__(self, itemsets: List[List[int]] = []):
        self.itemsets = itemsets
        self.flatten_items = list(itertools.chain(*self.itemsets))
        self.size = len(self.flatten_items)
        self.id = uuid.uuid4()

    def calc_all_items(self):
        self.flatten_items = list(itertools.chain(*self.itemsets))
        self.size = len(self.flatten_items)

    def __str__(self) -> str:
        return self.itemsets.__str__()

    def __eq__(self, other) -> bool:
        return len(self.itemsets) == len(other.itemsets) and all([a == b for a, b in zip(self.itemsets, other.itemsets)])

    def __len__(self) -> int:
        return len(self.itemsets)

    def __hash__(self) -> int:
        return hash(self.id)

    def hashcode(self, index: int, mod_value: int) -> int:
        return self.flatten_items[index] % mod_value
