
########################################################################
# Title: Binary Search Tree
# Algorithm: Insert
# Project: codewarm.in
#
# Description:
# To insert a new 'key' in the binary tree:
# 1. start with root.If the tree is empty, then create a node z such 
#    that z.key =key, z.left = None,z.right = None, z.parent=None and 
#    make this node as the root of the tree.
# 2. If key is less than or equal to the key stored at root then go to
#    left subtree of the tree, and if key is greater than the key stored
#    at root then go to right subtree.
# 3. Repeat this untill leaf node is reached. Let the node obtained is x.
# 4. create a node z such that z.key = key, z.left = None, z.right = None
#    z.parent = x.
# 5. If z.key <= x.key then insert the node z as the left child of x, else 
#    if z.key > x.key then insert the node z as the right child of the x.
# 6. Thats it, we are done.
#
# Time complexity : O(nlogn), where n is the size of binary tree.
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

	def insert(self,key):
		if self.root:
			self._insert(self.root,key)
		else:
			self.root = Node(key)

	def _insert(self,node,key):
		if key > node.key:
			if node.right:
				self._insert(node.right,key)
			else:
				node.right = Node(key,None,None,node)

		else:
			if node.left:
				self._insert(node.left,key)
			else:
				node.left = Node(key,None,None,node)


