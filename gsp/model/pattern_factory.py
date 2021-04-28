from model.pattern import Pattern

class PatternFactory:
    def __init__(self):
    	pass

    def create_pattern(self, sequence_id, elements=None):
    	new_pattern = Pattern(sequence_id, elements)
    	return new_pattern
