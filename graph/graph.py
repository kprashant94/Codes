
########################################################################
# Title: Graph
# Project: codewarm.in
#
# Description:
# Graph can be represented in two ways:
# 1. Adjacency list,
# 2. Adjacency matrix.
# Here adjacency list is used for representing graphs.
########################################################################



class Vertex:
	def __init__(self,vertex,weight=None):
		self.vertex = vertex
		self.weight = weight

class Graph:
	def __init__(self):
		self.graph = {}

	def add_vertex(self,vertex):
		self.graph[vertex] = []

	def add_edge(self,from_vertex,to_vertex,weight=None):
		self.graph[from_vertex].append(Vertex(to_vertex,weight))

	def delete_vertex(self,vertex):
		del self.graph[vertex]
		for i in self.graph :
			for temp in self.graph[i] :
				if temp.vertex == vertex :
					print 'temp=',temp.vertex
					self.graph[i].remove(temp)

	def delete_edge(self,from_vertex,to_vertex):
		for temp in self.graph[from_vertex] :
				if temp.vertex == to_vertex :
					self.graph[from_vertex].remove(temp)


	def adjacent(self,vertex):
		return self.graph[vertex]

'''
g = Graph()
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(8)
g.add_edge(5,6,7)
g.add_edge(5,8,10)
g.add_edge(6,8,56)
g.add_edge(6,5,7)
#g.delete_vertex(5)
g.delete_edge(6,8)
ad = g.adjacent(6)

for neb in ad :
	print neb.vertex,neb.weight

'''


