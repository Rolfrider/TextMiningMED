import sys
from input_parser.input_parser import parse_file
from algorithm.algorithm import search
from algorithm.algorithm_improve import search as improve_search
from model.sequence import Sequence
from algorithm.support_counting import count_support
from experiments.experiment import save_experiment_to_csv
from experiments.visualise import Visualise

file_name = sys.argv[1]
sequences = parse_file(file_name)
for sequence in sequences:
    print(sequence)

min_sup = float(sys.argv[2])

#experiment = 'moderna'  # ustawić w zależności od eksperymentu

result = search(min_sup, sequences)
print("Results")

data_ = []
data_viz = []
for sequence in result:
    seq_sup = count_support(sequence, sequences)
    print("Seq: {}, sup: {}".format(seq_sup[0], seq_sup[1]))
    data_.append([seq_sup[0], seq_sup[1]])
    data_viz.append(seq_sup[0])

#save_experiment_to_csv(data_, experiment, 'experiments/')

visualiser = Visualise(data_viz)
visualiser.draw()

result = improve_search(min_sup, sequences)
print("Results improved")

data_ = []
for sequence in result:
	seq_sup = count_support(sequence, sequences)
	print("Seq: {}, sup: {}".format(seq_sup[0], seq_sup[1]))
	data_.append([seq_sup[0], seq_sup[1]])