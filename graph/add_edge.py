
########################################################################
# Title: Graph
# Algorithm: Add edge
# Project: codewarm.in
#
# Description:
# An edge can be added in the graph by appending the target vertex in
# the list of which index is source vertex in graph dictionary.
# Time complexity: O(1)
########################################################################



class Vertex:
	def __init__(self,vertex,weight=None):
		self.vertex = vertex
		self.weight = weight

class Graph:
	def __init__(self):
		self.graph = {}

	def add_edge(self,from_vertex,to_vertex,weight=None):
		self.graph[from_vertex].append(Vertex(to_vertex,weight))


		