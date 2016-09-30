#complexity O(n)

def max_subarray(A):
	s=[A[0]]
	sum = A[0]
	for i in range(1,len(A)):
		if s[i-1]<=0:
			s.append(A[i])
		if s[i-1]>0:
			s.append(s[i-1]+A[i])
		if sum < s[i]:
			sum = s[i]
	return sum

arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
arr1 = [3,-4,-5,-6]
print max_subarray(arr)