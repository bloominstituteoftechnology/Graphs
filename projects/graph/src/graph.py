 
"""
Simple graph implementation
"""
class Queue
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size())> 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex):
        if vertex not in self.vertices.keys():
            self.vertices[vertex]= Vertex(vertex_id)


    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add[v2]
            self.vertices[v2].edges.add[v1]
        else:
            raise IndexError('That vertex does not exist')

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)        
        else:
            raise IndexError('That vertex does not exist')
    
    def breadth(self, starting, search_value):
        q = Queue()

        visited = set()

        q.enqueue(starting)

        while q.size()> 0:
            node = q.dequeue
        
        if node not in visited:
            print(node)
            visited.add(node)

        for child in self.vertices[node].edges:
            q.enqueue(child)
        
        


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('2', '1')
graph.add_edge('1', '2')
graph.add_edge('3', '2') 

print(graph.vertices)
print('breadth below')
graph.breadth(0, 5)