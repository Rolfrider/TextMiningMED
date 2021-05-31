import itertools
from typing import List, Set


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
        return val[0] % self.max_child

    def recur_insert(self, node, itemset, index, cnt):
        #print('index: ',index)
        #print('itemset: ',itemset)
        if index == len(itemset):
            if itemset in node.bucket:
                node.bucket[itemset] += cnt
            else:
                node.bucket[itemset] = cnt
            return
        if node.isLeaf:
            if itemset in node.bucket:
                node.bucket[itemset] += cnt
            else:
                node.bucket[itemset] = cnt

            if len(node.bucket) == self.max_leaf:
                # bucket has reached its maximum capacity and its intermediate node so
                # split and redistribute entries.
                for old_itemset, old_cnt in node.bucket.items():
                    hash_key = self.hash(old_itemset[index])
                    if hash_key not in node.children:
                        node.children[hash_key] = Node()
                    self.recur_insert(
                        node.children[hash_key], old_itemset, index + 1, old_cnt)
                del node.bucket
                node.isLeaf = False
        else:
            hash_key = self.hash(itemset[index])
            # print(hash_key)
            if hash_key not in node.children:
                node.children[hash_key] = Node()
            self.recur_insert(node.children[hash_key], itemset, index + 1, cnt)

    def insert(self, itemset):
        itemset = tuple(tuple(i) for i in itemset.itemsets)
        # print(itemset)
        self.recur_insert(self.root, itemset, 0, 0)

    def add_support(self, itemset):
        curr_node = self.root
        # print(itemset)
        itemset = tuple(tuple(i) for i in itemset)
        index = 0
        while True:
            if curr_node.isLeaf:
                if itemset in curr_node.bucket:
                    curr_node.bucket[itemset] = curr_node.bucket[itemset] + 1
                break
            hash_key = self.hash(itemset[index])
            # print(itemset[index])
            if hash_key in curr_node.children:
                curr_node = curr_node.children[hash_key]
            else:
                break
            index += 1

    def dfs(self, node, support_cnt):
        if node.isLeaf:
            for key, value in node.bucket.items():
                if value >= support_cnt:
                    self.frequent_itemsets.append((list(key), value))
            return

        for child in node.children.values():
            self.dfs(child, support_cnt)

    def get_frequent_itemsets(self, support_cnt):
        self.frequent_itemsets = []
        self.dfs(self.root, support_cnt)
        return self.frequent_itemsets


def generate_hash_tree(candidate_itemsets, length, max_leaf=4, max_child=5):
    htree = HashTree(max_child, max_leaf)
    for itemset in candidate_itemsets:
        htree.insert(itemset)
    return htree

# czy ok - nwm TO DO


def generate_k_subsets(sequences, length):
    subitemsets = []
    subsets = []
    for seq in sequences:
        # print(seq)
        items = [[item] for itemset in seq.itemsets for item in itemset]
        # print('items',items)
        subsets.extend(map(list, itertools.combinations(items, length)))
    return subsets
