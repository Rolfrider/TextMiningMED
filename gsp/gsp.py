import sys
from input_parser.input_parser import parse_file
from algorithm.algorithm import search
from model.sequence import Sequence
from algorithm.support_counting import count_support

file_name = sys.argv[1]
sequences = parse_file(file_name)
for sequence in sequences:
    print(sequence)

min_sup = float(sys.argv[2])

result = search(min_sup, sequences)
print("Results")
for sequence in result:
    seq_sup = count_support(sequence, sequences)
    print("Seq: {}, sup: {}".format(seq_sup[0], seq_sup[1]))
