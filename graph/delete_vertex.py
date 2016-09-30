
########################################################################
# Title: Graph
# Algorithm: Delete Vertex
# Project: codewarm.in
#
# Description:
# A vertex can be deleted by simply deleting the element from the graph
# dictionary whose index is that vertex and deleting all the edges with
# this vertex.
# Time complexity: O(nm) where n: |vertex|,m: |edges|
########################################################################



class Vertex:
	def __init__(self,vertex,weight=None):
		self.vertex = vertex
		self.weight = weight

class Graph:
	def __init__(self):
		self.graph = {}

	def delete_vertex(self,vertex):
		del self.graph[vertex]
		for i in self.graph :
			for temp in self.graph[i] :
				if temp.vertex == vertex :
					print 'temp=',temp.vertex
					self.graph[i].remove(temp)


					