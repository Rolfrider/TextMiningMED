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

def map_tmp(can_list):
	return list(map(lambda x: x if isinstance(x, list) else [x], can_list))

#https://rosettacode.org/wiki/Non-continuous_subsequences	
def ncsub(seq, s=0):
    if seq:
        x = seq[:1]
        xs = seq[1:]
        p2 = s % 2
        p1 = not p2
        return [x + ys for ys in ncsub(xs, s + p1)] + ncsub(xs, s + p2)
    else:
        return [[]] if s >= 3 else []
	
def generate_k_subsets(sequences):
	subsets = {}
	max_len = 0
	for seq in sequences:
		s = seq.flatten_items
		if len(s)>max_len:
			max_len = len(s)
	for i in range(3, max_len):
		subsets[i] = []
	for seq in sequences:
		s = seq.flatten_items
		results_temp = 	ncsub(s)
		subsets_k = {}
		for i in range(3,len(s)):
			subsets_k[i] = []
			for r in results_temp:
				if len(r) == i:
					subsets_k[i].append(r)
			r_set = set(tuple(x) for x in subsets_k[i])
			subsets_k[i] = [list(ele) for ele in r_set]
		for i in range(3, len(s)):
			results_it = []
			for r in subsets_k[i]:
				for l in range(1,len(r)):
					left_slice = r[:l]
					right_slice = r[-(len(r)-l):]
					new_subset = [left_slice, right_slice]
					if new_subset not in results_it:
						results_it.append(new_subset)
			
			for j in results_it:
				subsets_k[i].append(j)
		for i in range(3, len(s)):
			subsets_k[i] = list(map(lambda x: map_tmp(x), subsets_k[i]))
			subsets_k[i] = list(map(lambda x: Sequence(x), subsets_k[i]))
			subsets[i].extend(subsets_k[i])
		
	return subsets		
	#return list(map(lambda x: Sequence(x), results))
	