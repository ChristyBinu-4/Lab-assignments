#Question 7: Bredth first search


def BFS(graph, startVertex):
  queue, visited, traversalList  = [startVertex], {}, []
  
  for i in graph:
    visited.update({i:False})

  while queue:
    vertex = queue.pop(0)
    visited[vertex] = True
    traversalList.append(vertex)

    for node in graph[vertex]:
      if visited[node] is False and node not in queue:
        queue.append(node)

  return traversalList


graph = { 0:[1, 2, 3], 1:[0, 2], 2:[0, 1, 4], 3:[0], 4:[2]}
print("Input graph : ", graph)
print("Breadth first search :")
for i in BFS(graph,2):
  print(i, end=" ")