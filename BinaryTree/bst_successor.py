
########################################################################
# Title: Binary Search Tree
# Algrithm: Successor
# Project: codewarm.in
#
# Description:
# To find the successor of the key k:
# 1. Fnd the node storing key k, let it be x.
# 2. If the x has left subtree then the node having minimum element in
#    the right subtree is the successor of the node x.
# 3. If right subtree of the node x is empty, then the lowest ancestor
#    of the node x, say node y, such that x lies in the right subtree
#    of the node y, is the successor of node x.
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

	def successor(self,key):
		temp = self._successor(self._search(self.root,key))
		if temp:
			return temp.key
		else:
			return None

	def _successor(self,node):
		if node:
			if node.right:
				return self._min(node.right)
			temp = node.parent
			while temp != None and node == temp.left:
				node = temp
				temp = temp.parent
			return temp
		else:
			return None


			