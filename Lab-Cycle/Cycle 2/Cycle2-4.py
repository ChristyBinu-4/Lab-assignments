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
  'a' : ['b', 'c'],
  'b' : ['c', 'd'],
  'c' : ['b', 'd', 'e'],
  'd' : ['e'],
  'e' : ['d']
  }
# add the cost
cost = {
  ('a', 'b') : 6,
  ('a', 'c') : 3,
  ('b', 'c') : 1,
  ('c', 'b') : 4,
  ('b', 'd') : 2,
  ('c', 'd') : 8,
  ('c', 'e') : 2,
  ('d', 'e') : 9,
  ('e', 'd') : 7
}

ucs = uniformCostSearch(graph, cost, start='a', goal='d')

if ucs:
  print("Goal node found....", "pathway :", sep="\n")
  print(ucs[0])
  print("Cost of from source to destination = ", ucs[1])