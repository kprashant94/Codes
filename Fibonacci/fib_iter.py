
########################################################################
# Title: Dynamic Programming
# Algrithm: Fibonacci numbers
# Project: codewarm.in
#
# Problem statement:
# Given a number n, find nth fibonacci number.
#
# Approach: Iterative
# Time complexity: O(n)
# F(0)=0, F(1)=1
# F(i) = F(i-1)+F(i-2), i>1
# Calculating F(i) for all i<=n iteratively will find the F(n). 
#
########################################################################



def fib_iter(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		a=0
		b=1
		for i in range(2,n+1):
			temp = b
			b = a+b
			a = temp
	return b

print fib_iter(0)
print fib_iter(1)
print fib_iter(2)
print fib_iter(3)
print fib_iter(4)
print fib_iter(30)
