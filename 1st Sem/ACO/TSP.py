from itertools import permutations
from sys import maxsize
from numpy import array

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
    
    print('Minimum cost of Path', permutation, 'is', current_path_weight)

    if min_path_weight > current_path_weight:
      path.clear()#clear the path if minimum weight is found which less than current minimum 
      min_path_weight = current_path_weight
      path.append(permutation)
    elif min_path_weight == current_path_weight:
      path.append(permutation)
      
  return min_path_weight, path

#creating graph and inputing cities and its cost of travelling
graph = []
numberOfNodes = int(input("How many cities have to be traversed ?"))

for i in range(numberOfNodes):
  for j in range(numberOfNodes):
    cost = 0
    if i == j:
      graph.append(0)
      continue
    cost = int(input(f'Cost of travelling between city {i} to {j} => '))
    graph.append(cost)
graph = array(graph)
graph = graph.reshape(numberOfNodes, numberOfNodes)

#performing the travelling salesmann problem
startNode = 2
Output = tsp(graph, startNode)

#printing the output of the program
print(f'\nMinimum cost for travelling : {Output[0]}')
print("\npaths with minimum cost :")
for i in Output[1]:
  print(f'{startNode} {i} {startNode}')
