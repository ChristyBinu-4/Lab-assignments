def uniformCostSearch(graph, cost, start, goal):
  opened = []
  closed = []

  opened.append((0, start))
  
  while opened:
    opened.sort(reverse=True)
    selected_node = opened.pop()
    
    if selected_node[1] == goal:
      return selected_node[1]
    closed.append(selected_node)
    new_nodes = graph[selected_node[1]]

    if new_nodes:

      for child in new_nodes:
        costToChild = cost[(selected_node, child)]

        if child not in (opened and closed):
          opened.append((costToChild, child))
        
        # elif child in opened:
        #   if child == opened[0][1]:
        #     opened.append((costToChild, child))

   
    

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