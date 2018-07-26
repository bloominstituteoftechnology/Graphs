#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """Represent a vertex with a label and possible connected component."""

    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.components = 0

    def add_vertex(self, vertex, edges=()):
        """Add a new vertex, optionally with edges to other vertices."""
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        """Add a edge (default bidirectional) between two vertices."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

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

    def find_components(self):
        """Identify components and update vertex component ids."""
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

# import random


# class Vertex:
#     def __init__(self, label, color="gray", **pos):
#         self.label = label
#         self.color = color
#         self.pos = pos
#         self.edges = set()

#     '''
#     def __repr__(self):
#         return str(self.label)
#     '''

#     # Use the str method instead
#     def __str__(self):
#         if not self.pos:
#             pos = dict(x=None, y=None)
#         else:
#             pos = self.pos
#         return "Vartex is {}, position at ({}, {}), color is {} and has edges  {}".format(self.label, pos['x'], pos['y'], self.color, self.edges)


# class Graph:
#     def __init__(self):
#         self.vertices = {}

#     # we can see what properties are on the Graph
#     def __str__(self):
#         return str(self.vertices)

#     def add_edge(self, start, end, bidirectional=True):
#         """ And an edge (default bidirectional) between two vertices"""

#         # Change this so that if not in vertices, just add it
#         '''
#         if start not in self.vertices or end not in self.vertices:
#             raise Exception("Vertices to connect not in graph!")
#         self.vertices[start].add(end)
#         '''
#         # using the key, if we are passed an object just get the key

#         if isinstance(start, Vertex):
#             start = start.label

#         if isinstance(end, Vertex):
#             end = end.label

#         # add start if not in vertices
#         if start not in list(self.vertices.keys()):
#             self.add_vertex(Vertex(start))

#         # add end if not in vertices
#         if end not in list(self.vertices.keys()):
#             self.add_vertex(Vertex(end))

#         self.vertices[start].edges.add(self.vertices[end])
#         if bidirectional:
#             self.vertices[end].edges.add(self.vertices[start])

#     def add_vertex(self, vertex):

#         if not isinstance(vertex, Vertex):
#             vertex = Vertex(vertex)

#         if vertex.label in self.vertices:
#             return False  # ignores it

#         self.vertices[vertex.label] = vertex
#         return True  # added

#     # Create a random graph
#     def create_vertices_and_edges(self, n_verts):
#         # create verts and put them in a grid
#         grid = []
#         for i in range(n_verts):
#             grid.append(Vertex(str(i)))

#         # randomly loop through verts and randomly connect it to the next one, passing in the random bidirection
#         for i in range(n_verts - 1):
#             if (random.randrange(n_verts) < n_verts // 2):
#                 if(random.randrange(n_verts) < n_verts // 2):
#                     self.add_edge(grid[i].label, grid[i+1].label, False)
#                 self.add_edge(grid[i].label, grid[i+1].label)

#         for vert in grid:
#             self.add_vertex(vert)

    

#     def bfs(self, start):
#         random_color = '#' + \
#             ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
#         queue = []
#         found = []
#         queue.append(start)
#         found.append(start)

#         start.color = random_color

#         while (len(queue) > 0):
#             v = queue[0]
#             for edge in v.edges:
#                 if edge not in found:
#                     found.append(edge)
#                     queue.append(edge)
#                     edge.color = random_color

#             queue.pop(0)  # TODo look at collections.dequeue
#         return found

#     # Get the connected components
#     def get_connected_components(self):
#         # Connected Components
#         # Go to the next unfound vertex in graph vertices and call BFS on it
#         # Go to step 1 until we get to the end of the array(loop)

#         searched = []

#         for index, vertex in self.vertices.items():
#             if vertex not in searched:
#                 searched.append(self.bfs(vertex))

#         return searched


# import random

# class Vertex:
#     """Object representation of Vertex"""
#     def __init__(self, label ):
#         self.label = label
#         self.edges = set()
#         self.pos = pos
#         self.color = color

# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex, edges=()):
#         """Add anew vertex, optionally with edges to other vehicles."""
#         if vertex in self.vertices:
#             raise Exception('Error: adding vertex that already exists')
#         if not set(edges).issubset(self.vertices):
#             raise Exception('Error: cannot have edge to nonexistent vertices')
#         self.vertices[vertex] = set(edges)

#     def add_edge(self, start, end, bidirectional = True):
#         """Add a edge (default bidrectional) between two vertices."""
#         if start not in self.vertices or end not in self.vertices:
#             raise Exception('Vertices to connect not in graph!')    
#         self.vertices[start].add(end)
#         if bidirectional:
#             self.vertices[end].add(start)

#     def bfs(self, start):
#         #he making thats hexadecimal
#         random_color = '#' + \
#             ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
#         start.color = random_color
#         queue = [start]
#         found = set()
    
#         while queue:
#             current_vertex = queue.pop(0)
#             found.add(current_vertex)
#             for edge in current_vertex .edges:
#                 if edge not in found:
#                     found.append(edge)
#                     queue.append(edge)
#                     edge.color = random

        
#         return found
            
#     def get_connected_components(self):
        
#         searched = []

#         for index, vertex in self.vertices.items():
#             if vertex not in searched:
#                 searched.append(self.bfs(vertex))

#             return searched
        

# def main(): #instantiate your graph
#     graph = Graph()
#     graph.add_vertex('0')
#     graph.add_vertex('1')
#     graph.add_vertex('2')
#     graph.add_vertex('3')
#     graph.add_edge('0', '1')
#     graph.add_edge('0', '3')
#     print(graph.vertices)

#     if __name__ == '_main_':
#         main()
