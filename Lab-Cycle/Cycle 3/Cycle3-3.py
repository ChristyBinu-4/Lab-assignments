#Question 14: Best first search

def bestFirstSearch(graph, heuristics, start, goal):
  opened = []
  closed = []
  heuristicsToGoal = 0
  opened.append((heuristicsToGoal, start, []))
  
  while opened:

    opened.sort(reverse=True)
    selected_node = opened.pop()

    nameOfselected_node = selected_node[1]
    heuristicsOfselected_node = selected_node[0]
    pathWayOfnode = selected_node[2]

    if nameOfselected_node == goal:
      pathWayOfnode.append(nameOfselected_node)

      return pathWayOfnode
    
    closed.append(selected_node)
    new_nodes = graph[nameOfselected_node]

    if new_nodes:
    
      for child in new_nodes:
        heuristicsToGoal = heuristics[(nameOfselected_node, goal)]
  
        for i in range(len(opened)):
          if child in opened[i] :
              if heuristicsToGoal < opened[i][0]:
                opened.pop(i)

                path = selected_node[2].copy()
                path.append(nameOfselected_node)

                opened.append((heuristicsToGoal, child, path))
          
          if i < len(closed) and child in closed[i]:
            break 
        else:
            path = selected_node[2].copy()
            path.append(nameOfselected_node)

            opened.append((heuristicsToGoal, child, path))
        
# create the graph

# add edge
graph = {
  0 : [1, 2],
  1 : [3, 4],
  2 : [5, 6],
  3 : [],
  4 : [],
  5 : [7],
  6 : [8, 9],
  7 : [],
  8 : [],
  9 : []
  }

goal = 9
heuristics = {}

#getting heuristics from user
for i in graph.keys():
  if i is not goal:
    heuristicValue = int(input(f"Enter the heuristics from {i} to Goal : "))
    heuristics[(i, goal)] = heuristicValue
  else:
    heuristicValue = 0
    heuristics[(i, goal)] = heuristicValue



best_first_search = bestFirstSearch(graph, heuristics, 0, goal)

#printing path way
if best_first_search:
  print("Goal node found....", "pathway :", sep="\n")
  for i in best_first_search:
    print(i)
else:
  print("Goal node not found")