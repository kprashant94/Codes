
########################################################################
# Title: Graph
# Algorithm: Add vertex
# Project: codewarm.in
#
# Description:
# A vertex can be added in graph by simply initializing empty list with
# the index the name of the vertex in the graph dictionary.
# Time complexity: O(1)
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


		