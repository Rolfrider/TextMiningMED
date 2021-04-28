import sys
from input_parser.input_parser import parse_file, get_first_pass
from model.gsp_alg import GSP
from model.sequence_database import SequenceDB

file_name = sys.argv[1]
#sequences = parse_file(file_name)

#a = get_first_pass()

#print(list(a.items())[2])


#for sequence in sequences:
#    print(sequence.id)

seq = SequenceDB()
seq.parse_file(file_name)
seq.print_sequences()

GSP(min_support=1,min_gap=2,max_gap=3, window_size=5)

