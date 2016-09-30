
##################################################################
# Title: Heaps
# 
# Description:
# The heap data strucuture is an array object that we can view
# as a nearly complete binary tree. Each node of the tree
# corresponds to an element of the array. The tree is completely
# filled on all levels except possibly the lowest, which is filled
# from the left up tp to a point. The root of the tree is at index
# 0 in the array and given the index i of the node, we can easily
# compute the indices of its parent,left child and right child:
# parent(i): i/2
# left(i): 2*i
# right(i): 2*i+1
# There are two kinds of heaps: max heaps and min heaps. Here we
# implement the max heaps. The values in the nodes satisfy a max
# heaps property which is for every node i other than root,
# A[parent(i)] >= A[i]
# that is value of a node is at most the value of its parent.
# Thus the largest element in a max heap is stored at the root.
# - The max_heapify method, which runs in O(logn) time, is the key
#   to maintain the max-heap property.
# - The build_max_heap method, which runs in linear time, produces 
#   a max-heap from an unordered input array.
# - The heapsort method, which runs in O(nlogn) time, sorts an
#   array in place.
##################################################################



def parent(i):
	return i/2
def left(i):
	return 2*i
def right(i):
	return 2*i+1

def max_heapify(A,i,heap_size):
	l = left(i)
	r = right(i)
	if l<heap_size and A[l]>A[i]:
		largest = l
	else:
		largest = i
	if r<heap_size and A[r]>A[largest]:
		largest=r
	if largest != i:
		temp = A[i]
		A[i]=A[largest]
		A[largest]=temp
		max_heapify(A,largest,heap_size)

def build_max_heap(A):
	heap_size = len(A)
	i = (len(A)-1)/2
	while i>=0:
		max_heapify(A,i,heap_size)
		i=i-1

def heapsort(A):
	build_max_heap(A)
	heap_size = len(A)
	i=len(A)-1
	while i>=0:
		temp = A[i]
		A[i]=A[0]
		A[0]=temp
		heap_size = heap_size-1
		max_heapify(A,0,heap_size) 
		i=i-1

arr = [4,1,3,2,16,10,9,14,8,7]
build_max_heap(arr)
print arr
heapsort(arr)
print arr
