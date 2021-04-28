from model.pattern import Pattern

class PatternFactory:
    def __init__(self):
    	pass

    def create_pattern(self, sequence_ids, elements):
    	new_pattern = Pattern(sequence_ids, elements)
    	return new_pattern
