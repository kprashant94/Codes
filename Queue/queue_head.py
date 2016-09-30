
#####################################################################
# Title: Queue
# Algorithm: head element
# Project: codewarm.in
# 
# Description:
# In the this code the method 'head' takes the 'queue' as its 
# arugument and returns the element at the head in the 'queue'.
#
#####################################################################



class Queue:
	def __init__(self):
		self.Q = []

	def head(self):
		if (self.Q != []):
			return self.Q[0]
		else:
			print 'Queue is empty'