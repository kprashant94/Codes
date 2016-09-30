'''
Breadth-first search is one of the simplest algorithms for searching a graph.
Given a graph G = (V,E) and a distiguised source vertex s, breadth first
systematically explores the edges of G to discover every vertex that is
reachable from s. It computes the distance (smallest number of edges) from s
to each reachable vertex. It also produces a breadth-first tree with root s
that cantains all reachable vertices.
Breadth-first search is so named because it expands the frontier between discovered
and undiscovered vertices uniformly across the breadth of the frontier.
....
...

bfs method takes 2 arguments graph and source.
graph is assumed to be a dictionary where index represents the vertex.
and value is the address of the list which contains vertices adjacent to the vertex.




'''



from graph import Graph
from queue import Queue

def bfs(graph,source):
	color = {}
	distance = {}
	parent = {}
	for vertex in graph:
		color[vertex] = 'white'
		distance[vertex] = 9999999999
		parent[vertex] = None
	color[source] = 'gray'
	distance[source] = 0
	parent[source] = None

	Q = Queue()
	Q.enqueue(source)
	
	while Q.isEmpty() is False:
		u = Q.dequeue()
		for v in graph[u]:
			if color[v.vertex] == 'white':
				color[v.vertex] = 'gray'
				distance[v.vertex] = distance[u]+1
				parent[v.vertex] = u
				Q.enqueue(v.vertex)
		color[u] = 'black'		

	return [parent,color,distance]


def print_path(parent,s,v):
	if v==s:
		print s
	elif parent[v]==None:
		print 'No path'
		
	else:
		print_path(parent,s,parent[v])
		print v


g = Graph()
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(8)
g.add_vertex(9)
g.add_edge(5,6,7)
#g.add_edge(5,8,10)
g.add_edge(6,8,56)
g.add_edge(6,5,7)
g.add_edge(8,9,7)
#g.delete_vertex(5)
#g.delete_edge(6,8)
#ad = g.adjacent(6)

bfstree = bfs(g.graph, 5)
print bfstree
print_path(bfstree[0],5,9)


#for neb in ad :
#	print neb.vertex,neb.weight
