import sys
from input_parser.input_parser import parse_file

file_name = sys.argv[1]
sequences = parse_file(file_name)
for sequence in sequences:
    print(sequence)
