graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B'],
         'F': ['C'],
         'G': ['C']}

def bfs(graph, start, goal):
  #keep track of explored nodes (check this list when you pop a node to make sure you have not already visited)
  explored = []

  #initialize a queue to hold the nodes in a data structure as you search the graph
  queue = []
  queue.append(start) #adds the start node to the queue
  explored.append(start) #adds the start node to nodes that have already been explored

  while queue:#iterates through the queue
    current = queue.pop(0)
    for valueList in graph.values(): #grabs the list of nodes connected to the current node

        for value in valueList: #iterates through the list of nodes

            if value not in explored: #if the node has not been explored yet...
                explored.append(value) #add it to explored
                queue.append(graph[value]) #add the node to the queue so its children can be explored

                if value == goal: #check if we've reached the goal node
                    return explored #return the explored path if the goal is reached

print("BFS: ", bfs(graph, 'B', 'F')) #print the returned path

#change BFS to DFS by changing the queue to a stack
exploredDFS = [] #initialize the explored list
def dfs(graph, explored, node, goal):
    if node not in explored: #if the node has not been visited...
        if node == goal: #check if it is the goal node
            exploredDFS.append(node) #if it is, add it to the path
            print("Recursive DFS: ", exploredDFS) #print the path
            quit() #and quit the program
        else: #otherwise...
            explored.append(node) #add it to the explored list
        for child in graph[node]: #look for it's child
            dfs(graph, explored, child, goal) #call the function recursively

dfs(graph, exploredDFS, 'B', 'F')

