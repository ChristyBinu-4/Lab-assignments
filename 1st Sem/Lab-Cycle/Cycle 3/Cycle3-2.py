#Question 13: A* search algorithm


def a_star(graph, cost, heuristics, start, goal):
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

      return pathWayOfnode
    
    closed.append(selected_node)
    new_nodes = graph[nameOfselected_node]

    if new_nodes:
    
      for child in new_nodes:
        costToChild = cost[(nameOfselected_node, child)]
        costValue = costToChild + costOfselected_node
  
        for i in range(len(opened)):
          if child in opened[i] :
              if costValue < opened[i][0]:
                opened.pop(i)

                path = selected_node[2].copy()
                path.append(nameOfselected_node)
                heuristicsOfchild = heuristics[(child, goal)]

                functionValue = heuristicsOfchild + costValue

                opened.append((functionValue, child, path))
          
          if i < len(closed) and child in closed[i]:
            break 
        else:
            path = selected_node[2].copy()
            path.append(nameOfselected_node)
            heuristicsOfchild = heuristics[(child, goal)]

            functionValue = heuristicsOfchild + costValue

            opened.append((functionValue, child, path))
        

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
heuristics = {}
start = 0
goal = 6

print("A* search Algorithm")

print("\nInput graph and cost : ", graph)
print("\ncost : ")
for i in cost.keys():
  print(i[0], " => ", i[1], " : ",  cost[i])


#getting heuristics from user
for i in graph.keys():
  if i is not goal:
    heuristicValue = int(input(f"Enter the heuristics from {i} to Goal : "))
    heuristics[(i, goal)] = heuristicValue
  else:
    heuristicValue = 0
    heuristics[(i, goal)] = heuristicValue



astar = a_star(graph, cost, heuristics,start, goal)

if astar:

  #printing path way
  print("\nGoal node found....", "\npathway :", sep="\n")
  for i in astar:
    if i != astar[len(astar) - 1 ]:
      print(i, end=' => ')
    else:
      print(i)

  #printing Cost for comparing with other search algorithm
  total_cost = 0
  print("\nCost of Traversal : ")
  for i in range(1, len(astar)):
    total_cost += cost[(astar[i-1], astar[i])]
    
  print(total_cost)
else:
  print("Goal node not found")