import sys
from input_parser.input_parser import parse_file
from gsp_alg import GSP
from model.sequence_database import SequenceDB

file_name = sys.argv[1]
#sequences = parse_file(file_name)

#a = get_first_pass()

#print(list(a.items())[2])


#for sequence in sequences:
#    print(sequence.id)

seqDB = SequenceDB()
seqDB.print_sequences()
seqDB.parse_file(file_name, 0.1)
seqDB.print_sequences()

g = GSP(min_support=1,min_gap=2,max_gap=3, window_size=5)
g.run(seqDB)

