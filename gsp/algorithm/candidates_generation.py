from __future__ import annotations
from model.sequence import Sequence
from typing import List, Set
from abc import ABC, abstractmethod


def remove_duplicates(candidates: List[Sequence]) -> List[Sequence]:
    unique_candidates = []
    for candidate in candidates:
        is_unique = True
        for u_candidate in unique_candidates:
            if not candidates_diffrent(candidate, u_candidate):
                is_unique = False
        if is_unique:
            unique_candidates.append(candidate)
    return unique_candidates


def candidates_diffrent(can_a: Sequence, can_b: Sequence) -> bool:
    result = True
    for items_a, items_b in zip(can_a.itemsets, can_b.itemsets):
        if len(items_a) != len(items_b):
            return True
        if all(a_i in items_b for a_i in items_a):
            result = False
        else:
            return True
    return result


class CandidatesGenerationStrategy(ABC):
    @abstractmethod
    def generate_candidates(self, source: List[Sequence]) -> List[Sequence]:
        pass


class SingleCandidatesGenerator(CandidatesGenerationStrategy):

    def generate_candidates(self, source: List[Sequence]) -> List[Sequence]:
        unique_items: Set[int] = set()
        for seq in source:
            for itemset in seq.itemsets:
                unique_items = unique_items.union(itemset)
        return list(map(lambda x: Sequence(itemsets=[[x]]), unique_items))


class CandidateGenerator(CandidatesGenerationStrategy):
    def generate_candidates(self, source: List[Sequence]) -> List[Sequence]:
        candidates = []
        for seq_a in source:
            for seq_b in source:
                candidates += self.new_candidates(seq_a, seq_b)
        return remove_duplicates(candidates)

    def new_candidates(self, seq_a: Sequence, seq_b: Sequence) -> List[Sequence]:
        result = []
        items_a = [item for itemset in seq_a.itemsets for item in itemset]
        items_b = [item for itemset in seq_b.itemsets for item in itemset]
        if items_a[1:] == items_b[:-1]:
            if len(items_a) == 1 and len(items_b) == 1:
                result.append(Sequence([items_a, items_b]))
                if items_a[0] != items_b[0]:
                    result.append(Sequence([[items_a[0], items_b[0]]]))
            else:
                if items_b[-1] in seq_b.itemsets[-1] and len(seq_b.itemsets[-1]) == 1:
                    new_seq = Sequence([list(a_items)
                                        for a_items in seq_a.itemsets])
                    new_seq.itemsets.append([items_b[-1]])
                    result.append(new_seq)
                if items_b[-1] in seq_b.itemsets[-1] and len(seq_b.itemsets[-1]) > 1:
                    new_seq = Sequence([list(a_items)
                                        for a_items in seq_a.itemsets])
                    new_seq.itemsets[-1].append(items_b[-1])
                    result.append(new_seq)
        return result
