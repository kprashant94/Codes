
##################################################################
# Title: Max Heaps
# Sub-Title: Max Priority Queue
# Algorithm: Insert
# 
# Description:
# max_heap_insert(S,x) method inserts key x in the set S.
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

	def max_heap_insert(self,key):
		self.heap.append(-9999999999)
		self.heap_increase_key(self.heap_size()-1,key)


		