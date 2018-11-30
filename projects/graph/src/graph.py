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
        queue = Queue()
        traversal_path = []
        queue.add(self.vertices[starting_vertex])
        while queue.size() > 0:
            traversal_path.append(queue.queue[0])
            checking_children = list(queue.queue[0].edge)
            for i in range(0, len(queue.queue[0].edge) - 1):
                # print(f"count: {traversal_path.count(checking_children[i])}")
                if traversal_path.count(self.vertices[str(checking_children[i])]) == 0:
                    print(f"child being checked: {self.vertices[checking_children[i]]}")
                    queue.add(self.vertices[str(checking_children[i])])
                    # print(f"size of queue: {queue.size()}")
            queue.pop()
            # print(f"size: {queue.size()}")

        print(f"Starting vertex: {starting_vertex}")
        for item in traversal_path:
            print(item)

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


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
# 
# graph.breadth_first_traversal('2')
# graph.breadth_first_traversal('0')
# graph.breadth_first_traversal('1')
# graph.breadth_first_traversal('3')
