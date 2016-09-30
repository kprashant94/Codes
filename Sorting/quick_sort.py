
##################################################################
# Title: Sorting
# Algorithm: Quicksort
#
# Description:
# Quicksort, like merge sort, applies the divide-and-conquer 
# paradigm. Here is the three-step divide-and-conquer process
# for sorting a typical subarray A[p..r]:
# Divide: Partition (rearrange) the array A[p..r] into two 
#         subarrays A[p..q-1] and A[q+1..r] such that each element
#         of A[p..q-1] is less than or equal to A[q], which is, in
#		  turn, less than or equal to each element of A[q+1..r].
#		  Compute index q as part of this partitioning procedure.
# Conquer: Sort the two subarrays A[p..q-1] and A[q+1..r] by 
#		   recursive calls to quicksort.
# Combine: Because the subarrays are already sorted, no work is
#		   needed to combine them: the entire array A[p..r] is now
#		   sorted. 
#################################################################



def quick_sort(list):
 	_quick_sort(list,0,len(list)-1)

def _quick_sort(list,p,r):
 	if (p<r):
 		q = partition(list,p,r)
 		_quick_sort(list,p,q-1)
 		_quick_sort(list,q+1,r)

def partition(list,p,r):
	pivot = list[r]
	i = p-1
	for j in range(p,r):
		if (list[j] <= pivot):
			i=i+1
			temp = list[i]
			list[i] = list[j]
			list[j] = temp
	temp = list[i+1]
	list[i+1] = list[r]
	list[r] = temp
	return i+1

s = [48,46,23,90,-20,25,120,240,-4,8]
quick_sort(s)
print s


