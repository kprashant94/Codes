
##################################################################
# Title: Max Heaps
# Sub-Title: Max Priority Queue
# Algorithm: Max Heapify
# 
# Description:
# max_heapify(S,i): method maintains max heap property at index i.
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

	def max_heapify(self,i):
		l = self.left(i)
		r = self.right(i)
		if l<self.heap_size() and self.heap[l]>self.heap[i]:
			largest = l
		else:
			largest = i
		if r<self.heap_size() and self.heap[r]>self.heap[largest]:
			largest=r
		if largest != i:
			temp = self.heap[i]
			self.heap[i]=self.heap[largest]
			self.heap[largest]=temp
			self.max_heapify(largest)
