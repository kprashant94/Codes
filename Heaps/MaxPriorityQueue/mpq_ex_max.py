
##################################################################
# Title: Max Heaps
# Sub-Title: Max Priority Queue
# Algorithm: Extract-Max
# 
# Description:
# heap_extract_max(S): method removes and returns the maximum from 
#					   the set S.
# time complexity : O()
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

	def heap_extract_max(self):
		if len(self.heap)<1:
			print 'Heap underflow'
		max = self.heap[0]
		self.heap[0] = self.heap[self.heap_size()-1]
		del self.heap[self.heap_size()-1]
		self.max_heapify(0)
		return max