#Question 8: Depth first search


def DFS(graph, startVertex):
  queue, visited, traversalList = [startVertex], {}, []
  
  for i in range(len(graph)):
    visited.update({i:False})

  while queue:
    vertex = queue.pop(0)
    visited[vertex] = True
    traversalList.append(vertex)
    nodeIndex = 0 # It is used to avoid reversing of nodes in graph[vertex]

    for node in graph[vertex]:
      if visited[node] is False and node not in queue: 
        queue.insert(nodeIndex,node)
        nodeIndex += 1

  return traversalList


graph = { 0:[1, 2, 3], 1:[0, 2], 2:[0, 1, 4], 3:[0], 4:[2]}
print(DFS(graph,2))