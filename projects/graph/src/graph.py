"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        vertex = Vertex(vertex)
        self.vertices[vertex.vertex] = vertex.edge

    def add_edge(self, vertex_one, vertex_two):
        self.vertices[vertex_one].add(vertex_two)
        self.vertices[vertex_two].add(vertex_one)

    def breadth_first_traversal(self, starting_vertex):
        queue = Queue() # new queue
        traversal_path = [] # new list for reporting traversal history; only str, not Vertexes
        traversal_path.append(starting_vertex) # adds input to keep track
        queue.add(self.vertices[starting_vertex]) # adds input as starting member
        for item in self.vertices[starting_vertex]:
            if item in traversal_path:
                pass
            else:
                traversal_path.append(item)
                queue.add(self.vertices[item]) # the item's children
        queue.pop()

        while queue.size() > 0:
            for item in queue.pop():
                if item in traversal_path:
                    pass
                else:
                    traversal_path.append(item)
                    queue.add(self.vertices[item])
            # queue.pop()

        print(f"traversal_path: {traversal_path}")

class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.edge = set()

    def __repr__(self):
        return f"{self.vertex} : {self.edge} \n"

class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def __repr__(self):
        pretty_print = "" # actually conventionally a separator character
        return pretty_print.join(str(self.queue))


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)

graph.breadth_first_traversal('2')
graph.breadth_first_traversal('0')
graph.breadth_first_traversal('1')
graph.breadth_first_traversal('3')
