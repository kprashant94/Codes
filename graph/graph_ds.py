
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


