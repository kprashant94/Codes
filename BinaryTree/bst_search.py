
########################################################################
# Title: Binary Search Tree
# Algrithm: Search
# Project: codewarm.in
#
# Description:
# 1. Method begins its search with root and traces a simple path downword
#    in the tree.
# 2. For each node x it encounters, it compares the key k with x.key.
# 3. If the two keys are equal, the search method terminates.
# 4. If key k is smaller than x.key, the search method continues in the 
#     left subtree of x, since the bst property implies key k could not
#    be stored in the right subtree of x.
# 5. Similarly if key k is greater than x.key, the search continues in
#    the right subtree of x.
# Time complexity : O(logn)
#
########################################################################



class Node:
	def __init__(self,key,left=None,right=None,parent=None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def search(self,key):
		temp = self._search(self.root,key)
		if temp:
			return temp.key
		else:
			return None

	def _search(self,node,key):
		if node:
			if key == node.key:
				return node
			elif (key > node.key):
				return self._search(node.right,key)
			else:
				return self._search(node.left,key)
		else:
			return None


