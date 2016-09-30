
########################################################################
# Title: Binary Search Tree
# Algorithm: Inorder Traversal
# Project: codewarm.in
#
# Description:
# 1. Start with root.
# 2. First print the left subtree of the root.
# 3. print the root
# 4. Then print the right subtree of the root.
# Inorder traversal prints the binary tree in sorted order.
# Time conplexity : O(n)

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

	def inorder(self):
		if self.root:
			return self._inorder(self.root,[])
		else:
			return None

	def _inorder(self,node,S):
		if node.left:
			self._inorder(node.left,S)
		S.append(node.key)
		if node.right:
			self._inorder(node.right,S)
		return S


