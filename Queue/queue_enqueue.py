
#####################################################################
# Title: Queue
# Algorithm: enqueue
# Project: codewarm.in
# 
# Description:
# In the this code the method 'enqueue' takes the 'queue' and the key
# (to be inserted in queue) as its aruguments and inserts it at the 
# tail of the queue by appending the key in the list. 
#
#####################################################################



class Queue:
	def __init__(self):
		self.Q = []

	def enqueue(self, a):
		self.Q.append(a)