import random
import queue
"""
Simple graph implementation compatible with BokehGraph class.
"""

# lecture solution
"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add an vertex to the graph
        """
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        """
        Add an undirected edge to the graph
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")

    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def dfs(self, starting_node, visited=None):
        # Mark the node as visited
        if visited is None:
            # quese of visited nodes
            visited = []
        visited.append(starting_node)
        # For each child, if that child hasn't been visited, call dft() on that node
        for node in self.vertices[starting_node]:
            if node not in visited:
                self.dfs(node, visited)
        return visited
        # for child in children:
        #    if child not in visited:
        # dft(child, visted)

    def bfs(self, starting_node):
        # create an empty queue
        q = Queue()
        # Put starting vert in the queue
        q.enqueue(starting_node)
        visited = []
        # while q.size() > 0:
        while len(q) > 0:
                    # Remove the first node from the queue...
            new_node = queue.pop()
            # If it has not been visited yet,...
            if new_node not in visited:
                # Mark it as visited....
                visited += new_node
            # Then put all it's children in the back of the queue
            queue.extend(self.vertices[new_node])






class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        """
        Create an empty vertex
        """
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y

    def __repr__(self):
        return f"{self.edges}"


# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges.
#     def __init__(self):
#         self.vertices = {}
#     def add_vertex(self, value):
#         if value not in self.vertices:
#             self.vertices[value] = set()
#         else:
#             print("you already have that vertex in this graph")
#     def add_edge(self, v1, v2):
#         self.vertices[v1].add(v2)
#         self.vertices[v1].add(v2)
