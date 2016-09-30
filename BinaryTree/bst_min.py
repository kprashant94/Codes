
########################################################################
# Title: Binary Search Tree
# Algrithm: Minimum
# Project: codewarm.in
#
# Description:
# 1. Start with root.
# 2. Follow the left child untill the leaf node is reached.
# 3. return the key stored at that leaf node which is the
#    minimum element in the tree.
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

	def min(self):
		temp = self._min(self.root)
		if temp:
			return temp.key
		else:
			return None

	def _min(self,node):
		if node:
			if node.left:
				return self._min(node.left)
			else:
				return node
		else:
			return None


