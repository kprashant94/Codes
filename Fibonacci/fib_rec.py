
def fib_rec(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fib_rec(n-1)+fib_rec(n-2)

print fib_rec(0)
print fib_rec(1)
print fib_rec(2)
print fib_rec(3)
print fib_rec(4)
print fib_rec(5)
print fib_rec(30)