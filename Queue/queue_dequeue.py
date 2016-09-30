
#####################################################################
# Title: Queue
# Algorithm: Dequeue
# Project: codewarm.in
# 
# Description:
# In the this code the method 'dequeue' takes the 'queue' as its arugument
# and removes the element at the head in the queue and retruns it. 
#
#####################################################################



class Queue:
	def __init__(self):
		self.Q = []

	def dequeue(self):
		if (self.Q != []):
			temp = self.Q[0]
			del self.Q[0]
			return temp
		else:
			print 'Queue is empty'


			