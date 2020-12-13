import sys 
import numpy as np
import networkx.generators.random_graphs as nx
import networkx.convert_matrix as nm
import networkx.convert as nc
import timeit

from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]

# Function For Implementing Best First Search
# Gives output path having lowest cost


def best_first_search(source, target, n):
	visited = [0] * n
	visited[source] = True
	pq = PriorityQueue()
	pq.put((0, source))
	while pq.empty() == False:
		u = pq.get()[1]
		# Displaying the path having lowest cost
		print(u, end=" ")
		if u == target:
			break

		for v, c in graph[u]:
			if visited[v] == False:
				visited[v] = True
				pq.put((c, v))


def addedge(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))


lst = [10, 50, 100, 500, 1000, 5000, 10000]

for i in lst:

    print(i)
    graph = [[] for j in range(i)]
    a = nx.fast_gnp_random_graph(10, 0.5)
    b = nc.to_edgelist(a)

    for x,y,z in b:
        addedge(x,y,1)
    
    start = timeit.default_timer()
    best_first_search(0, i, i)
    stop = timeit.default_timer()
    print('Time: ', stop - start, "\n")

# Initially, Contributed by Neelam Yadav 
# Later On, Edited by Himanshu Garg 
