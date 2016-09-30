
########################################################################
# Title: Binary Search Tree
# Algrithm: Delete
# Project: codewarm.in
#
# Description:
# To delete key k in binary tree:
# 1. Find the node storing key k, let it be x.
# 2. If x has no children , then we simply remove it by modifying its
#    parent to replace x with None as its child.
# 3. If x has just one child, then we elevate that child to take x's
#    position in the tree by modifying x's parent to replace x by 
#    its child.
# 4. If x has both children, then find successor of x, say y, and raplace
#    x.key by y.key and delete y.
#
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

	def delete(self,key):
		self._delete(self._search(self.root,key))

	def _delete(self,node):
		if node:
			if node.left == None and node.right == None:
				if node.parent:
					if node == node.parent.left:
						node.parent.left = None
					else:
						node.parent.right = None
				else:
					self.root = None
			
			elif node.left == None:
				if node.parent:
					if node == node.parent.left:
						node.parent.left = node.right
					else:
						node.parent.right = node.right
				else:
					self.root = self.root.right
					self.root.parent = None

			elif node.right == None:
				if node.parent:
					if node == node.parent.left:
						node.parent.left = node.left
					else:
						node.parent.right = node.left
				else:
					self.root = self.root.left
					self.root.parent = None

			else:
				temp = self._successor(node)
				node.key = temp.key
				self._delete(temp)


				