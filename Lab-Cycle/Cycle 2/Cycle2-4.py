#Question 10: Uniform cost search

def uniformCostSearch(graph, cost, start, goal):
  opened = []
  closed = []
  costToChild = 0
  opened.append((0, start, []))
  
  while opened:

    opened.sort(reverse=True)
    selected_node = opened.pop()

    nameOfselected_node = selected_node[1]
    costOfselected_node = selected_node[0]
    pathWayOfnode = selected_node[2]

    if nameOfselected_node == goal:
      pathWayOfnode.append(nameOfselected_node)

      return pathWayOfnode, costOfselected_node
    
    closed.append(selected_node)
    new_nodes = graph[nameOfselected_node]

    if new_nodes:
    
      for child in new_nodes:
        costToChild = cost[(nameOfselected_node, child)]
  
        for i in range(len(opened)):
          if child in opened[i] :
              if costToChild + costOfselected_node < opened[i][0]:
                opened.pop(i)

                path = selected_node[2].copy()
                path.append(nameOfselected_node)

                opened.append((costToChild + costOfselected_node, child, path))
          
          if i < len(closed) and child in closed[i]:
            break 
        else:
            path = selected_node[2].copy()
            path.append(nameOfselected_node)

            opened.append((costToChild + costOfselected_node, child, path))
        

# create the graph

# add edge
graph = {
  0 : [1, 3],
  1 : [6],
  2 : [1], 
  3 : [1, 4, 6],
  4 : [2, 4],
  5 : [2, 6],
  6 : [4]
  }
# add the cost
cost = {
    (0, 1) : 2,
    (0, 3) : 5,
    (1, 6) : 1,
    (3, 1) : 5,
    (3, 6) : 6,
    (3, 4) : 2,
    (2, 1) : 4,
    (4, 2) : 4,
    (4, 5) : 3,
    (5, 2) : 6,
    (5, 6) : 3,
    (6, 4) : 7
}
start = 0
goal = 6
ucs = uniformCostSearch(graph, cost, start, goal)

print("\nInput graph and cost : ", graph)
print("\ncost : ")

for i in cost.keys():
  print(i[0], " => ", i[1], " : ",  cost[i])


if ucs:
  print("\nGoal node found....", "pathway :", sep="\n\n")
  lengthOfpathway = len(ucs[0]) - 1

  for i in ucs[0]:
    if i != ucs[0][lengthOfpathway]:  
      print(i, end=" => ")
    else:
      print(i)
  print(f"\nMinimum Cost of traversal from {start} to {goal} = ", ucs[1])