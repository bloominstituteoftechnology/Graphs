#add graph class to access graphs
class Graph:
   """Represent a graph as a dictionary of vertices mapping labels to edges."""
   def __init__(self):
      self.vertices = {}

   def add_vertex(self, vertex):
      """
      Add a vertex to the graph.
      """
      self.vertices[vertex] = set()
   def add_edge(self, v1, v2):
      """
      Add a directed edge to the graph.
      """
      if v1 not in self.vertices:
         self.add_vertex(v1)
      if v2 not in self.vertices:
         self.add_vertex(v2)

      self.vertices[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
   #create graph
   graph = Graph()

   #loop through ancestors array and change it to a list
   #add vertex and edges to graph
   for group in ancestors:
      l = list(group)
      graph.add_edge(l[1], l[0])

   #create queue, visited and path
   #highest node holds highest nodes
   #initiate queue and visited with starting node
   q = []
   path = []
   highest = []
   visited = set()

   q.append(starting_node)
   highest.append(starting_node)
   visited.add(starting_node)

   index = len(highest)
   count = len(highest)

   #travese using bft to check nodes by level
   while True:
      node = q.pop(0)
      path.append(node)
   
   #find highest parent
   # add parents to highest
      highest += list(graph.vertices[node])
   #if q is empty and the node has no parents break
      if not len(q) and not graph.vertices[node]:
         break
   #subtract 1 from count
      count -= 1
   #if count is 0
      if not count:
         highest = highest[index:]
         count = len(highest)
         index = len(highest)
      
   #loop through graph vertices and add parents
      for parent in graph.vertices[node]:
         if parent not in visited:
            q.append(parent)
            visited.add(parent)

   #return -1 if no highest parent is found
   #return the minimum if multiple highest parents are found
   if highest[0] == starting_node:
      return -1
   else:
      return min(highest)