from model.sequence import Sequence
from typing import List, Set
from __future__ import annotations
from abc import ABC, abstractmethod


class CandidatesGenerationStrategy(ABC):
    @abstractmethod
    def generate_candidates(self, source: List[Sequence]) -> List[Sequence]:
        pass


class SingleCandidatesGenerator(CandidatesGenerationStrategy):

    def generate_candidates(self, source: List[Sequence]) -> List[Sequence]:
        unique_items: Set[int] = set()
        for seq in source:
            for itemset in seq.itemsets:
                unique_items.union(itemset)
        return list(map(lambda x: Sequence(itemsets=[Set(x)]), unique_items))


class CandidateGenerator(CandidatesGenerationStrategy):
    def generate_candidates(self, source: List[Sequence]) -> List[Sequence]:
        pass
