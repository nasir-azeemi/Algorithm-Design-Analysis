# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

# Library for INT_MAX 
import sys 
import numpy as np
import networkx.generators.random_graphs as nx
import networkx.convert_matrix as nm 
import timeit

class Graph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] 
					for row in range(vertices)] 

	def printSolution(self, dist): 
		print ("Vertex tDistance from Source") 
		for node in range(self.V): 
			print (node, "t", dist[node]) 

	# A utility function to find the vertex with 
	# minimum distance value, from the set of vertices 
	# not yet included in shortest path tree 
	def minDistance(self, dist, sptSet): 

		# Initilaize minimum distance for next node 
		min = sys.maxsize 

		# Search not nearest vertex not in the 
		# shortest path tree 
		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 

		return min_index 

	# Funtion that implements Dijkstra's single source 
	# shortest path algorithm for a graph represented 
	# using adjacency matrix representation 
	def dijkstra(self, src): 

		dist = [sys.maxsize] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 

		for cout in range(self.V): 

			# Pick the minimum distance vertex from 
			# the set of vertices not yet processed. 
			# u is always equal to src in first iteration 
			u = self.minDistance(dist, sptSet) 

			# Put the minimum distance vertex in the 
			# shotest path tree 
			sptSet[u] = True

			# Update dist value of the adjacent vertices 
			# of the picked vertex only if the current 
			# distance is greater than new distance and 
			# the vertex in not in the shotest path tree 
			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
				    dist[v] = dist[u] + self.graph[u][v] 

		# self.printSolution(dist) 

# Driver program

lst = [10, 50, 100, 500, 1000, 5000, 10000]

for i in lst:

    print(i)

    a = nx.fast_gnp_random_graph(i, 0.5)
    a = nm.to_numpy_array(a)

    g = Graph(i)
    g.graph = a.tolist()
    start = timeit.default_timer()
    g.dijkstra(0)
    stop = timeit.default_timer()
    print('Time: ', stop - start, "\n")
# This code is contributed by Divyanshu Mehta 
