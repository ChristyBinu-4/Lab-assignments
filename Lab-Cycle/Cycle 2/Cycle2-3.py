#Question 9: Iterative deepening depth first search


def DFS(graph, currentNode, depth):
    print(currentNode, end="->")
    if depth > 0:
        for node in graph[currentNode]:
            if DFS(graph, node, depth - 1):
                return True
    else:
        return False


def IDDFS(graph, currentNode, depth):
    for i in range(depth):
        if DFS(graph, currentNode, i):
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
IDDFS(graph, 'A', 4)
