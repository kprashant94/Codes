
##################################################################
# Title: Max Heaps
# Sub-Title: Max Priority Queue
# 
# Description:
# A priority queue is a data structure for maintaining a set S of
# elements, each with an associated value called a key.
# A max-priority queue supports the following operations:
# Insert(S,x): inserts the elements x into the set S, which is
#              equivalent to the operation S=S U {x}.
# Maximum(S): returns the element of S with the largest key.
# Extract-Max(S): removes and returns the elements of S with the
#                 largest key.
# Increase-Key(S,x,k): increases the value of element x's key to 
#                      the new value k which is assumed to be at
#					   least as large as  x's current key value.
# 
##################################################################



class MaxPriorityQueue:
	def __init__(self):
		self.heap = []

	def parent(self,i):
		return i/2
	def left(self,i):
		return 2*i
	def right(self,i):
		return 2*i+1
	def heap_size(self):
		return len(self.heap)


		