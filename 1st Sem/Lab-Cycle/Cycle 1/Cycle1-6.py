#Question 6: All pair shortes path

import numpy as np


def printGraph(graph):
    for i in graph:
        for j in i:
            if(j == inf):
                print("INF", end="\t")
            else:
                print(j, end="\t")
        print("")
    print("\n") #leaves space after printing graph 



def allPairShortestPathFinder(graph):
    v = len(graph)

#   Formula to find the shortest path for all pair of vertices
    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
    return graph


v = 4 
inf = 99999999999999999999999

graph = [[0, 5, inf, 10],
         [inf, 0, 3, inf],
         [inf, inf, 0, 1],
         [inf, inf, inf, 0]]
graph = np.array(graph)#Converting the normal list to array

print("Input graph : ")
printGraph(graph)

#finding all pair shortest path for input graph
result = allPairShortestPathFinder(graph)
print("Shortest distance between every pair of vertices : ")
printGraph(result)