
########################################################################
# Title: Divide & Conquer
# Algrithm: Maximum subarray 
# Project: codewarm.in
#
# Problem statement:
# Given an array storing n numbers, find its subarray the sum
# of whose elements is maximum.
#
# Solution:
# Approach: Divide & Conquer
# Time complexity: O(nlogn)
# Suppose we want to find a maximum subarray of the subarray A[low..high].
# Divide & conquer suggests that we divide the subarray into two subarray
# of as equal size as possible. That is, we find the midpoint, say mid, of
# the subarray, and consider the subarrays A[low...mid] and A[mid+1..high].
# Any contiguous subarray A[i..j] of A[low..high] must lie in exactly one
# of the following places:
# 1. entirely in the subarray A[low..mid], so that low<=i<=j<=mid,
# 2. entirely in the subarray A[mid+1..high], so that mid<i<=j<=high, or
# 3. crossing the midpoint, so that low<=i<=mid<j<=high.
# Therefore, a maximum subarray of A[low..high] must lie in exactly one of
# these places. In fact, a maximum subarray of A[low..high] must have the
# greatest sum over all subarrays entirely in A[low..mid], entirely in 
# A[mid+1..high], or crossing the midpoint. We can find maximum subarrays
# of A[low..md] and A[mid+1..high] recursively, because these two subproblems
# are smaller instances of the problem of finding a maximum subarray. Thus,
# all that is left to do is find a maximum subarray that crosses the midpoint, 
# and take a subarray with the largest sum of the three.
# We can easily find a maximum subarray crossing the midpoint in time linear
# in the size of the subarray A[low..high]. This problem is not a smaller
# instance of our original problem, because it has the added restriction
# that the subarray it chooses must cross the midpoint. Any subarray crossing 
# the midpoint is itself made of two subarrays A[i..mid] and A[mid+1..j],
# where low<=i<=mid and mid<j<=high. Therefore, we just need to find maximum
# subarrays of the form A[i..mid] and A[mid+1..j] and then combine them.
# The method find_max_crossing_subarray takes as input the array A and
# the indices low,mid,and high, and returns a tuple containing the indicees
# demarcating a maximum subarray that crosses the midpoint, along with the
# sum of the values in a maximum subarray.
# 
########################################################################



def find_max_crossing_subarrary(A,low,mid,high):
	left_sum = -999999999
	sum = 0
	i=mid
	while i>=low:
		sum = sum+A[i]
		if sum > left_sum :
			left_sum = sum
			max_left = i
		i=i-1
	right_sum = -999999999
	sum = 0
	for j in range(mid+1,high+1):
		sum = sum+A[j]
		if sum > right_sum :
			right_sum = sum
			max_right = j
	return (max_left,max_right,left_sum+right_sum)


def find_max_subarray(A,low,high):
	if high == low:
		return (low,high,A[low])
	else:
		mid = (low+high)/2
		left_tuple = find_max_subarray(A,low,mid)
		right_tuple = find_max_subarray(A,mid+1,high)
		cross_tuple = find_max_crossing_subarrary(A,low,mid,high)
		if (left_tuple[2] >= right_tuple[2]) and (left_tuple[2] >= cross_tuple[2]):
			return left_tuple
		elif (right_tuple[2] >= left_tuple[2]) and (right_tuple[2] >= cross_tuple[2]):
			return right_tuple
		else:
			return cross_tuple

arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
arr1 = [1,3,-4,7]
res = find_max_subarray(arr,0,len(arr)-1)
print res
