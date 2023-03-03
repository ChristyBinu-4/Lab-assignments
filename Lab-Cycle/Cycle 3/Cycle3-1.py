#Question 12: Beam search

def beamSearch(graph, heuristics, start, goal, beam):
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
                heuristicsOfchild = heuristics[(child, goal)]

                opened.append((heuristicsOfchild, child, path))
          
          if i < len(closed) and child in closed[i]:
            break 
        else:
            path = selected_node[2].copy()
            path.append(nameOfselected_node)
            heuristicsOfchild = heuristics[(child, goal)]

            opened.append((heuristicsOfchild, child, path))
           
        opened.sort()

        for i in range(len(opened)):
          if len(opened) > beam : 
            if i >= beam :
              a = opened.pop(i)


        
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
heuristics = {}

print("Beam Search")
print("\ninput graph : ", graph,"\nStarting node : ", start, "\nGoal node : ", goal, "\n")

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

beam = int(input("Enter the beam width : "))

beam_search = beamSearch(graph, heuristics, start, goal, beam)


if beam_search:
  #printing path way
  print("\nGoal node found....", "\npathway :", sep="\n")
  lengthOfpathway = len(beam_search)

  for i in beam_search:
    if i != beam_search[lengthOfpathway - 1 ]:
      print(i, end=' => ')
    else:
      print(i)

  #printing Cost for comparing with other search algorithm
  total_cost = 0
  print("\nCost of Traversal : ")
  for i in range(1, len(beam_search)):
    total_cost += cost[(beam_search[i-1], beam_search[i])]
    
  print(total_cost)

else:
  print("Goal node not found")