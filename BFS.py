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
	# print()

# Function for adding edges to graph


def addedge(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))


# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
# addedge(0, 1, 3)
# addedge(0, 2, 6)
# addedge(0, 3, 5)
# addedge(1, 4, 9)
# addedge(1, 5, 8)
# addedge(2, 6, 12)
# addedge(2, 7, 14)
# addedge(3, 8, 7)
# addedge(8, 9, 5)
# addedge(8, 10, 6)
# addedge(9, 11, 1)
# addedge(9, 12, 10)
# addedge(9, 13, 2)

# source = 0
# target = 9
# print(graph)
# best_first_search(source, target, v)

# This code is contributed by Jyotheeswar Ganne


lst = [10]

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
