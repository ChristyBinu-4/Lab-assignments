def uniformCostSearch(graph, cost, start, goal):
  opened = []    
  path = []
  if goal == start:
    return 'already in goal'
  
  opened.append((0, start, path))

  while(opened) :
    priority, current, path = opened.pop()
    print(current, path)
    if current == goal:
      return path   
    next = graph[current]
    for state in next :
        print(state)
  


# create the graph
cost = {}

# add edge
graph = {
    'S' : [1, 3],
    1 : ['G'],
    2 : [1],
    3 : [1, 'G', 4],
    4 : [2, 5], 
    5 : ['G', 2],
    'G' : [4]
}
# add the cost
cost[('S', 1)] = 2
cost[('S', 3)] = 5
cost[(1, 'G')] = 1
cost[(3, 1)] = 5
cost[(3, 'G')] = 6
cost[(3, 4)] = 2
cost[(2, 1)] = 4
cost[(4, 2)] = 4
cost[(4, 5)] = 3
cost[(5, 2)] = 6
cost[(5, 'G')] = 3
cost[('G', 4)] = 7

print(uniformCostSearch(graph, cost, start='S', goal='G'))