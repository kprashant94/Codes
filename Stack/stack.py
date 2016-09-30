
class Stack:
	def __init__(self):
		self.S = []

	def isEmpty(self):
		return self.S == []

	def push(self, a):
		self.S.append(a)

	def pop(self):
		if (self.S != []):
			return self.S.pop()
		else:
			print 'Stack is empty'

	def top(self):
		if (self.S != []):
			return self.S[len(self.S)-1]
		else:
			print 'Stack is empty'

	def display(self):
		print self.S

s = Stack()


while(True):
	op = raw_input().split(':')
	if(op[0]=='push'):
		s.push(op[1])

	if(op[0]=='pop'):
		print s.pop()

	if(op[0]=='top'):
		print s.top()

	if(op[0]=='print'):
		s.display()

	if(op[0]=='isEmpty'):
		print s.isEmpty()

	if(op[0] == 'exit'):
		break

