#####################################################################
# Title: Stacks
# Algorithm: pop
# Project: codewarm.in
# 
# Description:
# In the this code the method 'pop' takes the 'stack' as its arugument
# and removes the top element in the stack and retruns it. 
#
#####################################################################

class Stack:
	def __init__(self):
		self.S = []

	def pop(self):
		if (self.S != []):
			return self.S.pop()
		else:
			print 'Stack is empty'