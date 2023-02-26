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
  
        for i in range(len(opened)):
          if child in opened[i] :
              if costToChild < opened[i][0]:
                print("fuck it")
                opened.pop(i)
                opened.append((costToChild, child))
          if child in closed[i]:
            break
        else:
            opened.append((costToChild + costOfselected_node, child))
        

# create the graph

# add edge
graph = {
    'V1' : ['V2', 'V3'],
    'V2':  ['V3', 'V4', 'V5'],
    'V3' : ['V4', 'V5'],
    'V4' : ['V5', 'V6'],
    'V5' : ['V6'], 
    'V6' : []
}
# add the cost
cost = {
  ('V1', 'V2') : 9,
  ('V1', 'V3') : 4,
  ('V2', 'V3') : 2,
  ('V2', 'V4') : 7,
  ('V2', 'V5') : 3,
  ('V3', 'V4') : 1,
  ('V3', 'V5') : 6,
  ('V4', 'V5') : 4,
  ('V4', 'V6') : 8,
  ('V5', 'V6') : 2,
}

ucs = uniformCostSearch(graph, cost, start='V1', goal='V6')

if ucs:
  print("Goal node found....", "pathway :", sep="\n")
  for i in ucs:
    print(i, end=" ")