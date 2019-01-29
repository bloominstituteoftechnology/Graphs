from queue import Queue
"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
        else:
            undefined = []
            if vertex1 not in self.vertices:
                undefined.append(vertex1)
            if vertex2 not in self.vertices:
                undefined.append(vertex2)
            undefined = ", ".join(undefined)
            raise KeyError(f"Vertex not found: {undefined}")

    def breadth_first_traversal(self, starting_node):
        queue = Queue()
        visited = set()
        print(starting_node)
        visited.add(starting_node)
        queue.put(starting_node)
        while not queue.empty():
            node = queue.get()
            for vertex in self.vertices[node]:
                if vertex not in visited:
                    visited.add(vertex)
                    print(vertex)
                    queue.put(vertex)

    def depth_first_traversal(self, starting_node):
        stack = []
        visited = set()
        stack.append(starting_node)
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node)
                for vertex in self.vertices[node]:
                    stack.append(vertex)

    def depth_first_traversal_recursive(self, starting_node, visited=None):
        if visited is None:
            visited = set()
        if starting_node not in visited:
            visited.add(starting_node)
            print(starting_node)
            for vertex in self.vertices[starting_node]:
                if vertex not in visited:
                    self.depth_first_traversal_recursive(vertex, visited)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '4')
graph.add_edge('1', '2')
graph.add_edge('3', '5')
graph.add_edge('6', '4')


# graph.breadth_first_traversal('0')
graph.depth_first_traversal_recursive('0')
