import math
import time
from typing import List, Set

from model.pattern import Pattern
from model.sequence import Sequence
from model.sequences import Sequences
from utils.candidates_generator import CandidatesGenerator
from utils.support_counter import SupportCounter

class GSP():
    def __init__(self, min_support, min_gap, max_gap, window_size):
        self.min_support = min_support
        self.min_gap = min_gap
        self.max_gap = max_gap
        self.window_size = window_size
        self.patterns = Sequences()
        self.number_of_frequent_patterns = 0
    
    #TO_DO
    def run(self, seq_db):
        sup = int(math.ceil(self.min_support*len(seq_db.sequences)))
        if sup<1:
            sup = 1
        #print(sup)
        
        c_g = CandidatesGenerator()
        s_c = SupportCounter()
        self.gsp(seq_db, c_g, s_c, sup)
        return self.patterns
    
    #TO_DO
    def gsp(self, seq_db, c_g, s_c, sup):
        #we get the frequent items found in the original database
        frequent_items = seq_db.get_frequent_items()
        #print(frequent_items)
        
        #we add the sequences as the 1-level of patterns. NOTE: we need them
        #for generating the candidates
        self.patterns.add_sequences(frequent_items, 1)
        #updating the number of frequent candidates adding the number of frequent items
        self.number_of_frequent_patterns+=len(frequent_items)
        #print(self.number_of_frequent_patterns)
        
        #we define a set where we temporaly keep the current frequent k-level.
        #It was called Lk in the original algorithm and we add it the frequent 1-sequences
        frequent_set = frequent_items
        #print(type(frequent_set))
        
        #we define a candidate set
        candidates: Set[Sequence] = {}
        #print(candidates)
        
        #main loop
        k = 1
        #dict() zwraca False gdy jest puste
        while(frequent_set!= None and frequent_set):
            #we start with the k+1 level
            k+=1
            print('Generating candidates...')
            candidates = c_g.generate_candidates(frequent_set, sup) #TO DO
            #print(candidates)
            frequent_set = None
            #we break the loop if the set of candidates is empty
            if candidates == None: #trzeba uzgodnić z tym co będzie zwracać generate_candidates
                break
            print('Candidates created!')
            
            #otherwise we continue counting the support of each candidate of the set
            print('Checking frequency...')
            
            #check the memory usage for statistics
            
            frequent_set = s_c.count_support(candidates, k, sup) #TO DO
            print('Found {0} frequent patterns'.format(frequent_set))
            
            ##check the memory usage for statistics
            
            #We update the number of frequent patterns, adding the number (k+1)-frequent patterns found
            self.number_of_frequent_patterns+=len(frequent_set)
            
            #And we prepare the next iteration, updating the indexation map and
            #the frequent level capable of generating the new candidates
            
            #Finally, we remove the previous level if we are not interested in
            #keeping the frequent patterns in memory
            
            #When the loop is over, if we were interested in keeping the output in
            #a file, we store the last level found.
            
            #Check the memory usage for statistics
            
            
            
        
    def print_statistics():
        pass
