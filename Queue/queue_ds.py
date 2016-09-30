
#####################################################################
# Title: Queues
# Project: codewarm.in
#
# Description: 
# Queues are dynamic sets in which the element deleted form the
# set is the one that has been in the set for the longest time. 
# Queue implements the first-in, first out (FIFO) policy.
# Here the queue is implemented using list.
# Queue has head and tail.
# Insert operation on queue is called 'enqueue' , it inserts 
# the element at the tail of the queue.
# Delete operation on stack is called 'dequeue' , it deletes the
# element at the head of the queue.
#
# In the this code the class 'Queue' is the stack data structure.  
#
#####################################################################



class Queue:
	def __init__(self):
		self.Q = []

		
