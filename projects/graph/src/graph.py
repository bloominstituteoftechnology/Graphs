#!/usr/bin/python
import random
"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
  def __init__(self, label, component=-1):
    self.label= str(label)
    self.component= component

  def __repr__(self):
    return 'Vertex:' + self.label

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
      self.vertices = {}
      self.components = 0

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
      if vertex in self.vertices:
        raise Exception('Error: adding vertex that already exists')
      # if not set(edges).issubset(self,vertices):
      #   raise Exception('Error: cannot have edge to nonexistant vertices')
      # if exists don't do anything, if not intilize it
      self.vertices[vertex] = set(edges)

    # def bfs(self, start, target:None):
        # random_color = '#' + \
        # ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        # queue = start
        # found = set()
        # # queue.append(start)
        # found.append(start)

        # start.color = random_color

        # while queue:
        #     current = queue.pop(0)
        #     if current == target:
        #       break
        #     visited.add(current)
        #     # Add possible (unvisited) vertices to queue 
        #     queue.extend(self.vertices[current]- visited)
        # return visited

    # def dfs(self, start, target:None):
        # random_color = '#' + \
        # ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        # stack = start
        # found = set()
        # queue.append(start)
        # found.append(start)

        # start.color = random_color

        # while stack:
        #     current = stack.pop()
        #     if current == target:
        #       break
        #     visited.add(current)
        #     # Add possible (unvisited) vertices to queue 
        #     stack.extend(self.vertices[current]- visited)
        # return visited
    def search(self, start, target=None, method='dfs'):
        """Search the graph using BFS or DFS."""
        quack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            quack.extend(self.vertices[current] - visited)

        return visited
    # def search(self,start, target:None, method = 'dfs'):
    #    quack = [start]
    #    pop_index= 0 if method == 'bfs' else -1
    #    while quack:
    #         current = stack.pop(pop_index)
    #         if current == target:
    #           break
    #         visited.add(current)
    #         # Add possible (unvisited) vertices to queue 
    #         quack.extend(self.vertices[current]- visited)
    #    return visited

    # Get the connected components
    def find_components(self):
        # Connected Components
        # Go to the next unfound vertex in graph vertices and call BFS on it
        # Go to step 1 until we get to the end of the array(loop)

        visited= set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.search(vertex)
                for otherVertex in reachable:
                  otherVertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
