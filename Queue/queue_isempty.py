
#####################################################################
# Title: Queue
# Algorithm: isEmpty
# Project: codewarm.in
# 
# Description:
# In the this code the method 'isEmpty' takes the 'queue' as its 
# arugument and returns 'True' if 'queue' is empty else returns
# 'False'.  
#
#####################################################################



class Queue:
	def __init__(self):
		self.Q = []

	def isEmpty(self):
		return self.Q == []


		