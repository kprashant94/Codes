
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

	def heap_max(self):
		return self.heap[0]

	def heap_extract_max(self):
		if len(self.heap)<1:
			print 'Heap underflow'
		max = self.heap[0]
		self.heap[0] = self.heap[self.heap_size()-1]
		del self.heap[self.heap_size()-1]
		self.max_heapify(0)
		return max

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

	def heap_increase_key(self,i,key):
		if key<self.heap[i]:
			print 'new key is smaller than current key.'
		self.heap[i] = key
		while i>0 and self.heap[self.parent(i)] < self.heap[i]:
			temp = self.heap[i]
			self.heap[i] = self.heap[self.parent(i)]
			self.heap[self.parent(i)] = temp
			i = self.parent(i)

	def max_heap_insert(self,key):
		self.heap.append(-9999999999)
		self.heap_increase_key(self.heap_size()-1,key)

	def build_max_heap(self,A):
		self.heap = A
		i = (len(A)-1)/2
		while i>=0:
			self.max_heapify(i)
			i=i-1


pq = MaxPriorityQueue()
pq.max_heap_insert(5)
pq.max_heap_insert(10)
pq.max_heap_insert(8)
pq.max_heap_insert(4)
pq.max_heap_insert(6)
pq.max_heap_insert(3)
pq.max_heap_insert(11)
print pq.heap_max()
print pq.heap_extract_max()
pq.heap_increase_key(4,7)
print pq.heap
arr = [4,1,3,2,16,10,9,14,8,7]
pq1 = MaxPriorityQueue()
pq1.build_max_heap(arr)
print pq1.heap_size()
print arr
print pq1.heap
pq1.max_heap_insert(5)
print pq1.heap_size()
print pq1.heap
print arr
pq1.heap_extract_max()
print pq1.heap_size()
print pq1.heap
print arr
print pq1.heap_max()