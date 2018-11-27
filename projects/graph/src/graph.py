"""
Simple graph implementation compatible with BokehGraph class.
"""
print('\nNEW FILE RUN: graph.py')

class Vertex:
    """Vertices have a label and a set of edges."""
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = int(label)  # each vertex has a label
        self.edges = set()       # each vertex has a set (unordered dictionary) of edges
    
    def __repr__(self):
        return f'{self.label}'

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # Start here:
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
    
    def bfs(start_node):
        # create a queue:
        q = Queue()
        # create a visited list:
        visited = []
        # put the start node in the queue:
        q.enqueue(start_node)
        # while queue is not empty:
        while q.size() > 0:
            # remove node from queue:
            node = q.dequeue()
            # check if it has been visited:
            if node not in visited:
                # mark node as visited:
                visited.append(node)
                # put all children in queue:
                for child in node.children:
                    q.enqueue(child)

class Queue:
    def enqueue(self, node):
        pass
    def dequeue(self, node_id):
        pass





graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')
graph.add_edge('0', '4')
print(len(graph.vertices))
print(graph.vertices)
