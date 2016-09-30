
########################################################################
# Title: Graph
# Algorithm: Delete edge
# Project: codewarm.in
#
# Description:
# An edge can be deleted by removing the target vertex from the list
# whose indeex is source vertex in graph dictionary. 
# Time complexity: O(k), k:no. of adjacent vertex of source vertex.
########################################################################



class Vertex:
	def __init__(self,vertex,weight=None):
		self.vertex = vertex
		self.weight = weight

class Graph:
	def __init__(self):
		self.graph = {}

	def delete_edge(self,from_vertex,to_vertex):
		for temp in self.graph[from_vertex] :
				if temp.vertex == to_vertex :
					self.graph[from_vertex].remove(temp)


					