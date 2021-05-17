from algorithm.candidates_generation import CandidateGenerator, CandidatesGenerationStrategy, SingleCandidatesGenerator
from model.sequence import Sequence
from typing import List
from algorithm.support_counting import count_support

__single_candidate_generator = SingleCandidatesGenerator()
__candidates_generator = CandidateGenerator()


def search(min_sup: float, sequences: [Sequence]) -> List[Sequence]:
    min_sup_absolute = int(min_sup * len(sequences))
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
            new_candidates = candidate_generator.generate_candidates(sequences)
        else:
            candidate_generator = __candidates_generator
            new_candidates = candidate_generator.generate_candidates(
                candidates)
        # Count support
        candidates_with_sup = map(
            lambda can: count_support(can, sequences), new_candidates)
        # Prune candidates
        pruned_candidates = list(filter(
            lambda can_sup: can_sup[1] > min_sup_absolute, candidates_with_sup))

        print("k = {}".format(k))
        for can in pruned_candidates:
            print("{} and sup: {}".format(can[0], can[1]))
        count_freq_seq += len(pruned_candidates)
        if not pruned_candidates:
            break
        else:
            candidates = list(
                map(lambda can_sup: can_sup[0], pruned_candidates))
        k += 1
    print("Freq seq: {}".format(count_freq_seq))
    return candidates
