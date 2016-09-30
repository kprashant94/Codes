
##################################################################
# Title: Max Heaps
# Sub-Title: Max Priority Queue
# Algorithm: Build max heap
# 
# Description:
# build_max_heap(A): method takes array A as input and converts it
#					 into max heap.
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

	def build_max_heap(self,A):
		self.heap = A
		i = (len(A)-1)/2
		while i>=0:
			self.max_heapify(i)
			i=i-1