from itertools import permutations
from sys import maxsize

def tsp(graph, startNode):
  vertex, path, V = [], [], len(graph)

  for i in range(V):
    if i != startNode:
      vertex.append(i)

  min_path_weight = maxsize
  next_permutation = permutations(vertex)

  for permutation in next_permutation:
    current_path_weight, k = 0, startNode

    for element in permutation :
      current_path_weight += graph[k][element]
      k = element
    current_path_weight += graph[k][startNode]

    if min_path_weight > current_path_weight:
      min_path_weight = current_path_weight
      path.append(permutation)
  return min_path_weight, path


graph = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]
startNode = 2
Output = tsp(graph, startNode)

print(f'Minimum cost for travelling : {Output[0]}')
for i in Output[1]:
  print(f'path => {startNode} {i} {startNode}')
