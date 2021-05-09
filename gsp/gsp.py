import sys
from input_parser.input_parser import parse_file
from algorithm.candidates_generation import CandidateGenerator
from model.sequence import Sequence

# file_name = sys.argv[1]
# sequences = parse_file(file_name)
# for sequence in sequences:
#     print(sequence)

sequences = [
    Sequence([{1}, {2}]),
    Sequence([{3}, {1}]),
]

gen = CandidateGenerator()
gen.generate_candidates(sequences)
