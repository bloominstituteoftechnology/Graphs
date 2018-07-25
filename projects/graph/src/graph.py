#!/usr/bin/python
import random
"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
  def __init__(self, label, color='green', **pos):
    self.label= label
    self.color= color
    self.pos = pos
    self.edge = set()

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
      self.vertices = {}

    def add_edge(self, start, end, bidirectional= True):
      if start not in self.vertices or end not in self.vertices:
        raise Exception ('Error vertices not in graph')
      # start.edges.add(end)
      self.vertices[start].add(end)
      if bidirectional:
        self.vertices[end].add(start)
        # end.edges.add(start)
        # the start exists? or end exists  raise error 
        #  if exists access the start vertex, the add(SET) if Bidrect 
        #  self.ver[start]. add 

    def add_vertex(self, vertex, edges=()):
      # if not set(edges).issubset(self,vertices):
        # raise Exception('Error: cannot have edge to nonexistant vertices')
      if vertex in self.vertices:
        raise Exception('Error: adding vertex that already exists')
      # if exists don't do anything, if not intilize it
      self.vertices[vertex] = set(edges)
    
    def bfs(self, start):
        random_color = '#' + \
        ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        queue = []
        found = []
        queue.append(start)
        found.append(start)

        start.color = random_color

        while (len(queue) > 0):
            v = queue[0]
            for edge in v.edges:
                if edge not in found:
                    found.append(edge)
                    queue.append(edge)
                    edge.color = random_color

            queue.pop(0)  # TODo look at collections.dequeue
        return found

    # Get the connected components
    def get_connected_components(self):
        # Connected Components
        # Go to the next unfound vertex in graph vertices and call BFS on it
        # Go to step 1 until we get to the end of the array(loop)

        searched = []

        for index, vertex in self.vertices.items():
            if vertex not in searched:
                searched.append(self.bfs(vertex))

        return searched

  #   def dfs(start, reset = true):
  #     component = []
  #     stack = []
  #     if reset:
  #       for v in vertexes:
  #         v.color = 'white'
  #     stack.append(start)
  #     while stack.length > 0:
  #       u = stack.pop(0)
  #       if u.color == 'white':
  #         u.color = 'gray'
  #       for e in u.edges:
  #         stack.append(e.destination)
  #     stack.[:0]
  #     u.color = 'black'
  #     component.append(u)
  #     return component;


  # /**
  #  * Get the connected components
  #  */
  #   def getConnectedComponents(self):
  #     componentsList = []
  #     needReset = true
  #     for v in  vertexes:
  #       if needReset || v.color =='white':
  #         component = self.dfs(v, needReset)
  #         needReset = false
  #       componentsList.append(component)
  #     return componentsList

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# # print(graph.vertices)

# # graph.add_edge('0', '4')
# bg = BokehGraph(graph)
# bg.show()
