
##################################################################
# Title: Max Heaps
# Sub-Title: Max Priority Queue
# Algorithm: Increase key
# 
# Description:
# heap_increase_key(S,i,k): increases the value of element i's key to 
#                      the new value k which is assumed to be at
#					   least as large as  i's current key value.
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

	def heap_increase_key(self,i,key):
		if key<self.heap[i]:
			print 'new key is smaller than current key.'
		self.heap[i] = key
		while i>0 and self.heap[self.parent(i)] < self.heap[i]:
			temp = self.heap[i]
			self.heap[i] = self.heap[self.parent(i)]
			self.heap[self.parent(i)] = temp
			i = self.parent(i)