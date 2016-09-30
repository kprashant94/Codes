
########################################################################
# Title: Binary Search Tree
# Project: codewarm.in
#
# Description:
# A binary search tree is organized, as the name suggests, in a binary
# tree. We can represent such a tree by a linked data structure in which
# each node is an object. In addition to a key satellite data, each node
# contains attributes left, right, and parent that point to the nodes 
# corresponding to its left child, its right child, and its parent respe-
# -ctively. If a child or the parent is missing, the appropriate attribute
# contains the value 'None'. The root node is the only node in the tree 
# whose parent is None.
# The keys in a binary search tree are always stored in such a way as to
# satisfy the binary-search-tree property:
# Let x be a node in a binary search tree. If y is a node in the left sub-
# -tree of x, then y.key <= x.key.
# If y is a node in the right sub sub-tree of x, then y.key > x.key.
# Here the class Node is the node storing the data of particular node of
# the tree, and the class BinarySearchTree is the data structure for the 
# binary Search tree.
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


