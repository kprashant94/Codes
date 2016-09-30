
########################################################################
# Title: Binary Search Tree
# Algrithm: Maximum
# Project: codewarm.in
#
# Description:
# 1. Start with root.
# 2. Follow the right child untill the leaf node is reached.
# 3. return the key stored at that leaf node which is the
#    maximum element in the tree.
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
	
	def max(self):
		temp = self._max(self.root)
		if temp:
			return temp.key
		else:
			return None

	def _max(self,node):
		if node:
			if node.right:
				return self._max(node.right)
			else:
				return node
		else:
			return None


