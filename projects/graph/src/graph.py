"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = int(vertex_id)
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)
    def add_edge(self, vertex, edge):
        self.vertices[vertex].edges.add(edge)
        self.vertices[edge].edges.add(vertex)

    def connectBFS(self,index):
        connected = []
        queue = [self.vertices[str(index)]]
        while queue:
            node = queue.pop(0)
            if node not in connected:
                connected.append(node)
                for next_node in node.edges:
                    queue.append(self.vertices[next_node])

        newconnected = []
        for i in connected:
            newconnected.append(i.id)
        return newconnected

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')

graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '1')
graph.add_edge('3', '2')

print(graph.connectBFS(1))