#Question 8: Depth first search


def DFS(graph, startVertex):
  queue, visited, traversalList = [startVertex], {}, []
  
  for i in graph:
    visited.update({i:False})

  while queue:
    vertex = queue.pop(0)
    visited[vertex] = True
    traversalList.append(vertex)
    nodeIndex = 0 # It is used to avoid reversing of nodes in graph[vertex]

    for node in graph[vertex]:
      if visited[f"{node}"] is False and node not in queue: 
        queue.insert(nodeIndex,node)
        nodeIndex += 1

  return traversalList


graph = {
  'A' : ['B', 'C'],
  'B' : ['D', 'E'],
  'C' : ['G'],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : []
}
print(DFS(graph,'A'))