#Question 8: Depth first search


def DFS(graph, currentNode):

    print(currentNode, end=" ")
    for node in graph[currentNode]:
        if DFS(graph, node):
            return True
    return False


graph = {
  'A' : ['B', 'C'],
  'B' : ['D', 'E'],
  'C' : ['G'],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : []
}

DFS(graph,'A')