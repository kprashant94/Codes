#####################################################################
# Title: Binary Search Tree
# Sub-title: data structure
# Project: codewarm.in
#
# Description: Data Structure
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
#
# Description: Insert
# To insert a new 'key' in the binary tree:
# 
# 1. start with root.If the tree is empty, then create a node z such that z.key =key,
#    z.left = None,z.right = None, z.parent=None and make this node as
#    the root of the tree.
# 2. If key is less than or equal to the key stored at root then go to left 
#    subtree of the tree, and if key is greater than the key stored at root
#    then go to right subtree.
# 3. Repeat this untill leaf node is reached. Let the node obtained is x.
# 4. create a node z such that z.key = key, z.left = None, z.right = None
#    z.parent = x.
# 5. If z.key <= x.key then insert the node z as the left child of x, else if 
#    z.key > x.key then insert the node z as the right child of the x.
# 6. Thats it, we are done.
# Time complexity : O(nlogn), where n is the size of binary tree.
#
# Description: Inorder Traversal
#
# 1. Start with root.
# 2. First print the left subtree of the root.
# 3. print the root
# 4. Then print the right subtree of the root.
# Inorder traversal prints the binary tree in sorted order.
# Time conplexity : O(n)
#
# Description : Preorder Traversal
#
# 1. start with root.
# 2. print root.
# 3. print left subtree of the root.
# 4. print right subtree of the root.
# Time complexity : O(n)
#
#
# Description : Postorder Traversal
#
# 1. start with root.
# 2. print left subtree of the root.
# 4. print right subtree of the root.
# 3. print root
# Time complexity : O(n)
#
#
# Description : Search
# 1. Method begins its search with root and traces a simple path downword
#    in the tree.
# 2. For each node x it encounters, it compares the key k with x.key.
# 3. If the two keys are equal, the search method terminates.
# 4. If key k is smaller than x.key, the search method continues in the 
#     left subtree of x, since the bst property implies key k could not
#    be stored in the right subtree of x.
# 5. Similarly if key k is greater than x.key, the search continues in
#    the right subtree of x.
# Time complexity : O(logn)
#
# Description : Max
# 1. Start with root.
# 2. Follow the right child untill the leaf node is reached.
# 3. return the key stored at that leaf node which is the maximum
#    maximum element in the tree.
# Time complexity : O(logn)
#
#
# Description : Min
# 1. Start with root.
# 2. Follow the left child untill the leaf node is reached.
# 3. return the key stored at that leaf node which is the maximum
#    minimum element in the tree.
# Time complexity : O(logn)
#
# Description : Predecessor
# To find the prdecessor of the key k:
# 1. Fnd the node storing key k, let it be x.
# 2. If the x has left subtree then the node having maximum element 
#    in the left subtree is the predecessor of the node x.
# 3. If left subtree of the node x is empty, then the lowest ancestor
#    of the node x, say node y, such that x lies in the right subtree
#    of the node y, is the predecessor of node x.
# Time complexity : O(logn)
#
#
#
# Description : Successor
# To find the successor of the key k:
# 1. Fnd the node storing key k, let it be x.
# 2. If the x has left subtree then the node having minimum element in
#    the right subtree is the successor of the node x.
# 3. If right subtree of the node x is empty, then the lowest ancestor
#    of the node x, say node y, such that x lies in the right subtree
#    of the node y, is the successor of node x.
# Time complexity : O(logn)
#
# Description : Delete
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
#    Time complexity : O(logn)
#
#####################################################################

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


	def search(self,key):
		temp = self._search(self.root,key)
		if temp:
			return temp.key
		else:
			return None

	def _search(self,node,key):
		if node:
			if key == node.key:
				return node
			elif (key > node.key):
				return self._search(node.right,key)
			else:
				return self._search(node.left,key)
		else:
			return None

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
		

			



	



	





tree = BinarySearchTree()

tree.insert(5)
tree.insert(7)
tree.insert(2)
tree.insert(0)
tree.insert(9)
tree.insert(6)
tree.insert(8)
tree.insert(10)
print tree.inorder()
print tree.search(8)
print tree.search(10)
print tree.preorder()
print tree.postorder()
print tree.max()
print tree.min()
print tree.predecessor(9)
print tree.successor(9)
#tree.delete(6)
print tree.inorder()
tree.delete(5)
print tree.inorder()
print tree.search(15)
print tree.root.key
print tree.successor(7)

tree1 = BinarySearchTree()

tree1.insert(20)
tree1.insert(10)
tree1.insert(30)
print tree1.inorder()
tree1.delete(20)
print tree1.inorder()
tree1.delete(10)
print tree1.inorder()
tree1.delete(30)
print tree1.inorder()
tree1.insert(40)
tree1.insert(50)
tree1.insert(15)
tree1.insert(45)
tree1.insert(47)
print tree1.inorder()
print tree1.root.key
print tree1.root.left.key
print tree1.root.right.key
print tree1.root.right.left.right.key

print tree1.predecessor(47)
print tree1._predecessor(tree1.root.right.left.right).key
