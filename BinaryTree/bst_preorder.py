
########################################################################
# Title: Binary Search Tree
# Algorithm: Preorder Traversal
# Project: codewarm.in
#
# Description:
# 1. start with root.
# 2. print root.
# 3. print left subtree of the root.
# 4. print right subtree of the root.
# Time complexity : O(n)
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

	def preorder(self):
		if self.root:
			return self._preorder(self.root,[])
		else:
			return None

	def _preorder(self,node,S):
		S.append(node.key)		
		if node.left:
			self._preorder(node.left,S)
		
		if node.right:
			self._preorder(node.right,S)
		
		return S


