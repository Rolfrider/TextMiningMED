import itertools
from typing import List, Set

class Node:
	def __init__(self):
		self.children = {}
		self.isLeaf = True
		#self.isInterior = False
		self.bucket = {}
		
class HashTree:
	def __init__(self, max_leaf, max_child):
		self.root = Node()
		self.max_leaf = max_leaf
		self.max_child = max_child
		self.frequent_itemsets = []
	
	def hash(self, val):
		return val % self.max_child
	
	def recur_insert(self, node, itemset, index, cnt):
		if index == len(itemset):
			#last bucket - simple insert
			if itemset in node.bucket:
				node.bucket[itemset] +=cnt
			else:
				node.bucket[itemset] =cnt
			if len(node.bucket) == self.max_leaf:
			# bucket has reached its maximum capacity and its intermediate node so
			# split and redistribute entries.
				for old_itemset, old_cnt in node.bucket.iteritems():
					hash_key = self.hash(old_itemset[index])
					if hash_key not in node.children:
						node.children[hash_key] = Node()
					self.recur_insert(node.children[hash_key], old_itemset, index + 1, old_cnt)
				del node.bucket
				node.isLeaf = False
		else:
			#print(itemset[index])
			hash_key = self.hash(itemset[index])
			#print(hash_key)
			if hash_key not in node.children:
				node.children[hash_key] = Node()
			self.recur_insert(node.children[hash_key], itemset, index + 1, cnt)
			
	def insert(self, itemset):
		itemset = [i for i in itemset.itemsets][0]
		itemset = tuple(itemset)
		self.recur_insert(self.root, itemset, 0, 0)
		
	def add_support(self, itemset):
		curr_node = self.root
		itemset = tuple(itemset)
		index = 0
		while True:
			if curr_node.isLeaf:
				if itemset in curr_node.bucket:
					curr_node.bucket[itemset] += 1
				break
			hash_key = self.hash(itemset[index])
			if hash_key in curr_node.children:
				curr_node = curr_node.children[hash_key]
			else:
				break
			index += 1
	
	def dfs(self, node, support_cnt):
		if node.isLeaf:
			print(node.bucket.items())
			for key, value in node.bucket.items():
				if value >= support_cnt:
					self.frequent_itemsets.append((list(key), value))
					# print key, value, support_cnt
			return
			
	def get_frequent_itemsets(self, support_cnt):
		self.frequent_itemsets = []
		self.dfs(self.root, support_cnt)
		return self.frequent_itemsets
    	

def generate_hash_tree(candidate_itemsets, length, max_leaf=4, max_child=5):
    htree = HashTree(max_child, max_leaf)
    for itemset in candidate_itemsets:
    	htree.insert(itemset)
    	print(htree.root.children)
    return htree
    
def generate_k_subsets(sequences, length):
	subsets = []
	for seq in sequences:
		for items in seq.itemsets:
			#itemset = [i for i in itemset.itemsets][0]
			#print(items)
			#itemset = tuple(itemset)
			subsets.extend(map(list, itertools.combinations(items, length)))
	#subsets = tuple(subsets)
	#print(subsets)
	return subsets
    	