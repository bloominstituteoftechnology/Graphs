"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """Represent a vertex with a label and possible connected component."""
    # pylint: disable=too-few-public-methods
    # Using class so it's hashable, even though it doesn't have public methods
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
        visited = set([start])

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            quack.extend(self.vertices[current] - visited)
            visited.update(self.vertices[current])

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



















# """
# Simple graph implementation compatible with BokehGraph class.
# """
# import random
# from queue import PriorityQueue

# class Vertex:
#     def __init__(self, data, x=None, y=None, component=-1):
#         self.id = data
#         self.edges = set()
#         self.color = 'white'
#         self.component = component
#         if x is None:
#             self.x = random.random() * 10 - 5
#         else:
#             self.x = x
#         if y is None:
#             self.y = random.random() * 10 - 5
#         else:
#             self.y = y
#     def __repr__(self):
#         return f"{self.edges}"

# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex):
#         node = Vertex(vertex)
#         self.vertices[vertex] = node

#     def add_edge(self, src, dest):
#         if src in self.vertices and dest in self.vertices:
#             self.vertices[src].edges.add(dest)
#             self.vertices[dest].edges.add(src)

#     def num_nodes(self):
#         num_nodes = 0
#         for _ in self.vertices:
#             num_nodes += 1
#         return num_nodes
    
#     def list_nodes(self):
#         node_list = []
#         for node in self.vertices:
#             node_list.append(node)
#         return node_list
    
#     def BFT(self, startVert):
#         q = PriorityQueue()
#         visited = []
#         for v in self.vertices:
#             self.vertices[v].color = 'white'
        
#         # print('****', self.vertices[startVert].color)
#         self.vertices[startVert].color = 'pink'
#         q.put(startVert)

#         while not q.empty():
#             u = q.queue[0]
#             visited.append(self.vertices[u])
#             # print("edges", self.vertices[u].edges)
#             for v in self.vertices[u].edges:
#                 if self.vertices[v].color == 'white':
#                     self.vertices[v].color = 'pink'
#                     if v not in visited:
#                         q.put(v)
#             q.get()
#             self.vertices[u].color = 'purple'
#         return visited

#     def connected_components(self):
        
#         connected_components = set()
#         for v in self.vertices:
#             print(v)
#             self.vertices[v].color = 'white'
#             if self.vertices[v] not in connected_components:
#                 connected_components.update(self.BFT(self.vertices[v].id))
#             if self.vertices[v].color == 'white':
#                 self.vertices[v].color = 'pink'
#         print("CC" , connected_components)
#         return connected_components


# if __name__ == "__main__":
#     graph = Graph()
#     graph.add_vertex(0)
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)

#     graph.add_edge(0, 1)
#     graph.add_edge(0, 3)

#     # graph.print_graph()
#     print(graph.vertices)

#     for key in graph.vertices.keys():
#         print(graph.vertices[key].edges)










