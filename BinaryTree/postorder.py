
########################################################################
# Title: Binary Search Tree
# Algrithm: Postorder Traversal
# Project: codewarm.in
#
# Description:
# 1. start with root.
# 2. print left subtree of the root.
# 4. print right subtree of the root.
# 3. print root
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

	def postorder(self):
		if self.root:
			return self._postorder(self.root,[])
		else:
			return None

	def _postorder(self,node,S):		
		if node.left:
			self._postorder(node.left,S)
		
		if node.right:
			self._postorder(node.right,S)
		
		S.append(node.key)		
		return S


