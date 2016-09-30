
#####################################################################
# Title: Stacks
# Algorithm: push
# Project: codewarm.in
# 
# Description:
# In the this code the method 'push' takes the 'stack' and the key
# (to be inserted in stack) as its aruguments and inserts it at the 
# top of the stack by appending the key in the list. 
#
#####################################################################

class Stack:
	def __init__(self):
		self.S = []

	def push(self, a):
		self.S.append(a)



		