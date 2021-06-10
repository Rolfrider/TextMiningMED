import itertools
from model.sequence import Sequence
from typing import List, Set
from algorithm.support_counting import is_subseq


class Node:
    def __init__(self):
        self.children = {}
        self.isLeaf = True
        self.bucket = {}


class HashTree:
    def __init__(self, max_leaf, max_child):
        self.root = Node()
        self.max_leaf = max_leaf
        self.max_child = max_child
        self.frequent_itemsets = []

    def hash(self, val):
        return val % self.max_child

    def recur_insert(self, node, seq: Sequence, index, cnt):
        if index == seq.size:
            if seq in node.bucket:
                node.bucket[seq] += cnt
            else:
                node.bucket[seq] = cnt
            return
        if node.isLeaf:
            if seq in node.bucket:
                node.bucket[seq] += cnt
            else:
                node.bucket[seq] = cnt

            if len(node.bucket) == self.max_leaf:
                # bucket has reached its maximum capacity and its intermediate node so
                # split and redistribute entries.
                for old_seq, old_cnt in node.bucket.items():
                    hash_key = old_seq.hashcode(index, self.max_child)
                    if hash_key not in node.children:
                        node.children[hash_key] = Node()
                    self.recur_insert(
                        node.children[hash_key], old_seq, index + 1, old_cnt)
                del node.bucket
                node.isLeaf = False
        else:
            hash_key = seq.hashcode(index, self.max_child)
            if hash_key not in node.children:
                node.children[hash_key] = Node()
            self.recur_insert(node.children[hash_key], seq, index + 1, cnt)

    def insert(self, seq: Sequence):
        self.recur_insert(self.root, seq, 0, 0)

    def add_support(self, seq):
        curr_node = self.root
        index = 0
        while True:
            if curr_node.isLeaf:
            	for bucket_seq in curr_node.bucket:
            		if bucket_seq == seq:
            			curr_node.bucket[bucket_seq] += 1
            	break
            hash_key = seq.hashcode(index, self.max_child)
            if hash_key in curr_node.children:
            	curr_node = curr_node.children[hash_key]
            else:
                break
            index += 1

    def dfs(self, node, support_cnt):
        if node.isLeaf:
            for key, value in node.bucket.items():
            	if value >= support_cnt:
            		self.frequent_itemsets.append((key, value))
            return

        for child in node.children.values():
            self.dfs(child, support_cnt)

    def get_frequent_itemsets(self, support_cnt):
        self.frequent_itemsets = []
        self.dfs(self.root, support_cnt)
        return self.frequent_itemsets


def generate_hash_tree(candidate_sequences: [Sequence], length, max_leaf=4, max_child=5):
    htree = HashTree(max_child, max_leaf)
    for seq in candidate_sequences:
        htree.insert(seq)
    return htree


def get_flatten_itemsets(sequences: [Sequence]) -> List[int]:
    flatten_itemsets = map(lambda seq: list(itertools.chain(
        *seq.itemsets)), sequences)
    return flatten_itemsets


def generate_k_subsets(sequences, length):
    subsets = []
    for seq in sequences:
        #print(seq.itemsets)
        # subsets.extend(map(lambda x: (x, seq), map(
        #     list, itertools.combinations(seq.flatten_items, length))))
        new_subseq = map(
            list, itertools.combinations(seq.flatten_items, length))
        #print(len(list(new_subseq)))
        for sub_seq in new_subseq:
            if (sub_seq, seq) not in subsets:
                subsets.append((sub_seq, seq))
    return subsets

def map_tmp(can_list):
	return list(map(lambda x: x if isinstance(x, list) else [x], can_list))
	
def generate_k_subsets_3(sequences, length):
	results_0 = []
	results_1 = []
	results = []
	for seq in sequences:
		s = seq.flatten_items
		results_temp = list(map(list, itertools.combinations(s, length)))
		#print('len(results_temp) before',len(results_temp))
		r_set = set(tuple(x) for x in results_temp)
		results_temp = [list(ele) for ele in r_set]
		#print('len(results_temp) after',len(results_temp))
		results_0.extend(results_temp)
		#print(results_0)

		for r in results_0:
			for i in range(1,length):
				left_slice = r[:i]
				l = (len(r)-i)
				right_slice = r[-l:]
				results_1.append([left_slice, right_slice])
				# results.append([left_slice, right_slice])
			results_1 = [[tuple(ele) for ele in sub] for sub in results_1]
			r_set = set(tuple(x) for x in results_1)
			results_1 = [[list(ele) for ele in sub] for sub in r_set]
			# print(results_1)
	results.extend(results_0)
	results.extend(results_1)
	results = list(map(lambda x: map_tmp(x), results))
	#results = [[tuple(ele) for ele in sub] for sub in results]
	#r_set = set(tuple(x) for x in results)
	#results = [[list(ele) for ele in sub] for sub in r_set]
	return list(map(lambda x: Sequence(x), results))