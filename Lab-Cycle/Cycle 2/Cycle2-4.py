def uniformCostSearch(graph, cost, start, goal):
  opened = []
  closed = []
  path = []
  costToChild = 0
  opened.append((0, start))
  
  while opened:

    opened.sort(reverse=True)
    selected_node = opened.pop()

    nameOfselected_node = selected_node[1]
    costOfselected_node = selected_node[0]

    path.append(nameOfselected_node)

    if nameOfselected_node == goal:
      return path
    
    closed.append(selected_node)
    new_nodes = graph[nameOfselected_node]

    if new_nodes:
  
      for child in new_nodes:
        costToChild = cost[(nameOfselected_node, child)]

        if child not in (opened and closed):
          opened.append((costToChild + costOfselected_node, child))
        
        elif child in opened:
          for i in range(len(opened)):
            if child == opened[i]:
              opened.append((costToChild, child))

   
    

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

ucs = uniformCostSearch(graph, cost, start='S', goal='G')

if ucs:
  print("Goal node found....", "pathway :", sep="\n")
  for i in ucs:
    print(i, end=" ")