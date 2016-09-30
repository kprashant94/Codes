
#####################################################################
# Title: Queue
# Algorithm: head element
# Project: codewarm.in
# 
# Description:
# In the this code the method 'tail' takes the 'queue' as its 
# arugument and returns the element at the tail in the 'queue'.
#
#####################################################################



class Queue:
	def __init__(self):
		self.Q = []

	def tail(self):
		if (self.Q != []):
			return self.Q[len(self.Q)-1]
		else:
			print 'Queue is empty'


			