#####################################################################
# Title: Stacks
# Algorithm: top element
# Project: codewarm.in
# 
# Description:
# In the this code the method 'top' takes the 'stack' as its arugument
# and returns the top element of the stack. 
#
#####################################################################

class Stack:
	def __init__(self):
		self.S = []

	def top(self):
		if (self.S != []):
			return self.S[len(self.S)-1]
		else:
			print 'Stack is empty'