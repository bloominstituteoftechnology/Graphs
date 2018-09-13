"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.edges = set()
        if self.x is None:
            # self.x = 3 * (self.id // 3)
            self.x = 2 * (self.id // 3) + self.id / 10 
        if self.y is None:
            # self.y = 4 * (self.id % 3)
            self.y = 2 * (self.id % 3) + self.id / 10 + (self.id // 4)
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def add_edge(self, vertex, edge):
        self.vertices[vertex].edges.add(edge)
        self.vertices[edge].edges.add(vertex)

    def connectedBFT(self,index):
        connected = []
        queue = [self.vertices[str(index)]]

        while queue:
            node = queue.pop(0)
            if node not in connected:
                connected.append(node)
                for next_node in node.edges:
                    queue.append(self.vertices[next_node])
        
        nuconnected = []
        for i in connected:
            nuconnected.append(i.id)

        return nuconnected

    def dft(self, index):
        stack = []
        stack.append(self.vertices[str(index)])
        visited = []

        while len(stack) > 0:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                for next_node in node.edges:
                    stack.append(self.vertices[next_node])
        
        nuconnected = []
        for i in visited:
            nuconnected.append(i.id)

        return nuconnected
    

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_vertex('9')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '4')
graph.add_edge('4', '7')
graph.add_edge('4', '9')

print(graph.dft(0))  
