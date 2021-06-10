import sys
from input_parser.input_parser import parse_file
from algorithm.algorithm import search
from algorithm.algorithm_improve import search as improve_search
from model.sequence import Sequence
from algorithm.support_counting import count_support
from experiments.experiment import save_experiment_to_csv

file_name = sys.argv[1]
sequences = parse_file(file_name)
#for sequence in sequences:
#    print(sequence)

min_sup = float(sys.argv[2])

experiment = 'astra'  # ustawić w zależności od eksperymentu

result = search(min_sup, sequences)
print("Results")

data_ = []
for sequence in result:
    seq_sup = count_support(sequence, sequences)
    print("Seq: {}, sup: {}".format(seq_sup[0], seq_sup[1]))
    data_.append([seq_sup[0], seq_sup[1]])


result = improve_search(min_sup, sequences)
print("Results improved")

data_ = []
for sequence in result:
	print(sequence)
	seq_sup = count_support(sequence, sequences)
	print("Seq: {}, sup: {}".format(seq_sup[0], seq_sup[1]))
	data_.append([seq_sup[0], seq_sup[1]])

#save_experiment_to_csv(data_, experiment, 'experiments/')
#save_experiment_to_txt(data_, 'experiments/result.txt')
