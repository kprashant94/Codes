
########################################################################
# Title: Binary Search Tree
# Algrithm: Predeccessor
# Project: codewarm.in
#
# Description:
# To find the prdecessor of the key k:
# 1. Fnd the node storing key k, let it be x.
# 2. If the x has left subtree then the node having maximum element 
#    in the left subtree is the predecessor of the node x.
# 3. If left subtree of the node x is empty, then the lowest ancestor
#    of the node x, say node y, such that x lies in the right subtree
#    of the node y, is the predecessor of node x.
# Time complexity : O(logn))
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

	def predecessor(self,key):
		temp = self._predecessor(self._search(self.root,key))
		if temp:
			return temp.key
		else:
			return None

	def _predecessor(self,node):
		if node:
			if node.left:
				return self._max(node.left)
			temp = node.parent
			while temp != None and node == temp.left:
				node = temp
				temp = temp.parent
			return temp
		else:
			return None


