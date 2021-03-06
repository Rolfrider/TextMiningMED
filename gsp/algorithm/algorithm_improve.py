from algorithm.candidates_generation import CandidateGenerator, CandidatesGenerationStrategy, SingleCandidatesGenerator
from model.sequence import Sequence
from model.hash_tree import generate_hash_tree, generate_k_subsets
from typing import List
from algorithm.support_counting import count_support

__single_candidate_generator = SingleCandidatesGenerator()
__candidates_generator = CandidateGenerator()


def search(min_sup: float, sequences: [Sequence]) -> List[Sequence]:
    min_sup_absolute = min_sup * len(sequences)
    print("Absolute min support: {}".format(min_sup_absolute))
    candidate_generator: CandidateGenerator = None
    candidates: List[Sequence] = []
    count_freq_seq = 0
    k = 1
    while True:
        # Generate new candidates
        new_candidates: List[Sequence] = []
        if k == 1:
            candidate_generator = __single_candidate_generator
            new_candidates = candidate_generator.generate_candidates(
                sequences)
            # Count support
            candidates_with_sup = map(
                lambda can: count_support(can, sequences), new_candidates)
            # Prune candidates
            pruned_candidates = list(filter(
                lambda can_sup: can_sup[1] >= min_sup_absolute, candidates_with_sup))
            if not pruned_candidates:
                break
            else:
                candidates = list(
                    map(lambda can_sup: can_sup[0], pruned_candidates))
            # sequences = list(
            #     map(lambda x: x.prune_not_freq(candidates), sequences))
            for seq in sequences:
                seq.prune_not_freq(candidates)
        elif k == 2:
            candidate_generator = __candidates_generator
            new_candidates = candidate_generator.generate_candidates(
                candidates)
            # Count support
            candidates_with_sup = map(
                lambda can: count_support(can, sequences), new_candidates)
            # Prune candidates
            pruned_candidates = list(filter(
                lambda can_sup: can_sup[1] >= min_sup_absolute, candidates_with_sup))
            candidates = list(
                map(lambda can_sup: can_sup[0], pruned_candidates))
            for seq in sequences:
                seq.prune_not_freq(candidates)
        else:
            candidate_generator = __candidates_generator
            new_candidates = candidate_generator.generate_candidates(
                candidates)
            h_tree = generate_hash_tree(
                new_candidates, 1, max_leaf=4, max_child=5)
            # For each sequence find all possible subsets of size "length"
            print(k)
            sequences_subsets = generate_k_subsets(sequences, k)
            # Count sypport - hash tree
            for subset in sequences_subsets:
                h_tree.add_support(subset)

            candidates_frequent_hash = h_tree.get_frequent_itemsets(
                min_sup_absolute)
            for seq, sup in candidates_frequent_hash:
                print("{} - {}".format(seq.itemsets, sup))
            if not candidates_frequent_hash:
                print('break!')
                break
            else:
                candidates = list(
                    map(lambda can_sup: can_sup[0], candidates_frequent_hash))
            for seq in sequences:
                seq.prune_not_freq(candidates)
        k += 1
    print("Freq seq: {}".format(count_freq_seq))
    return candidates
