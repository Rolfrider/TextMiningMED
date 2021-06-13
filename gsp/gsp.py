import sys
from input_parser.input_parser import parse_file
from algorithm.algorithm import search
from algorithm.algorithm_improve import search as improve_search
from model.sequence import Sequence
from algorithm.support_counting import count_support
from experiments.experiment import save_experiment_to_csv
from experiments.visualise import Visualise
import time

file_name = sys.argv[1]
sequences = parse_file(file_name)
for sequence in sequences:
    print(sequence)

min_sup = float(sys.argv[2])

experiment = 'astra'  # ustawić w zależności od eksperymentu
start_time = time.time()
result = search(min_sup, sequences)
end_time = time.time()
print("Results in {}".format(end_time - start_time))

#visulaise frequent sequences
data_viz = []
for sequence in result:
    seq_sup = count_support(sequence, sequences)
    data_viz.append(seq_sup[0])
    
visualiser = Visualise(data_viz)
visualiser.draw()

seqces = sequences
start_time = time.time()
result = improve_search(min_sup, seqces)
end_time = time.time()
print("Results improved in {}".format(end_time - start_time))

#save_experiment_to_csv(data_, experiment, 'experiments/')
#save_experiment_to_txt(data_, 'experiments/result.txt')
