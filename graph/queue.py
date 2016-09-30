
class Queue:
	def __init__(self):
		self.Q = []

	def isEmpty(self):
		return self.Q == []

	def enqueue(self, a):
		self.Q.append(a)

	def dequeue(self):
		if (self.Q != []):
			temp = self.Q[0]
			del self.Q[0]
			return temp
		else:
			print 'Queue is empty'

	def head(self):
		if (self.Q != []):
			return self.Q[0]
		else:
			print 'Queue is empty'

	def tail(self):
		if (self.Q != []):
			return self.Q[len(self.Q)-1]
		else:
			print 'Queue is empty'

	def display(self):
		print self.Q

'''
q = Queue()

while(True):
	op = raw_input().split(':')
	if(op[0]=='e'):
		q.enqueue(op[1])

	if(op[0]=='d'):
		q.dequeue()

	if(op[0]=='h'):
		print q.head()

	if(op[0]=='t'):
		print q.tail()

	if(op[0]=='p'):
		q.display()

	if(op[0] == 'exit'):
		break


'''
