import itertools
from model.sequence import Sequence
from typing import List, Set
from algorithm.support_counting import is_subseq
from algorithm.candidates_generation import remove_duplicates


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
        # print(val)
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
            # print(hash_key)
            if hash_key not in node.children:
                node.children[hash_key] = Node()
            self.recur_insert(node.children[hash_key], seq, index + 1, cnt)

    def insert(self, seq: Sequence):
        self.recur_insert(self.root, seq, 0, 0)

    def add_support(self, seq):
        curr_node = self.root
        #itemset = tuple(items_seq)
        index = 0
        while True:
            if curr_node.isLeaf:
                for bucket_seq in curr_node.bucket:
                    if bucket_seq == seq:
                        curr_node.bucket[bucket_seq] += 1
                break
            #hash_key = items_seq[0][index] % self.max_child
            # print(items_seq)
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
        print("Generate subseq for candidate: {}".format(seq.itemsets))
        new_itemsets = generate_k_itemsets(seq.itemsets, length)
        new_sequences = list(map(lambda x: Sequence(x), new_itemsets))
        unique_sequences = remove_duplicates(new_sequences)
        subsets.extend(unique_sequences)
    return subsets


def generate_k_itemsets(input, length):
    if length <= 0:
        return []
    result = []
    for index, itemset in enumerate(input):
        if len(itemset) > 1:
            for itemset_l in range(1, min(len(itemset) + 1, length + 1)):
                for itemset_subset in itertools.combinations(itemset, itemset_l):
                    endings = generate_k_itemsets(
                        input[index+1:], length - itemset_l)
                    if endings:
                        for ending in endings:
                            result.append([list(itemset_subset)] + ending)
                    else:
                        result.append([list(itemset_subset)])
        else:
            endings = generate_k_itemsets(
                input[index+1:], length - 1)
            if endings:
                for ending in endings:
                    result.append([itemset] + ending)
            else:
                result.append([itemset])
    return result


def map_tmp(can_list):
    return list(map(lambda x: x if isinstance(x, list) else [x], can_list))
