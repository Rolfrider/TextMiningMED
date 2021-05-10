from typing import List, Tuple, Iterator
from model.sequence import Sequence


def count_support(candidate: Sequence, sequences: List[Sequence]) -> Tuple[Sequence, int]:
    result = 0
    for seq in sequences:
        seq_iter = iter(seq.itemsets)
        is_supported = False
        for items in candidate.itemsets:
            is_supported = __find_items_in_seq(items, seq_iter)
        if is_supported:
            result += 1
    return (candidate, result)


def __find_items_in_seq(items: List[int], seq_iter: Iterator) -> bool:
    while True:
        try:
            seq_items = next(seq_iter)
            if all(item in seq_items for item in items):
                return True
        except StopIteration:
            return False
