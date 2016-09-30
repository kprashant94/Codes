
##################################################################
# Title: Max Heaps
# Sub-Title: Max Priority Queue
# Algorithm: Maximum
# 
# Description:
# heap_max(S): method returns the maximum element in set S.
# Time complexity: O(1)
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

	def heap_max(self):
		return self.heap[0]