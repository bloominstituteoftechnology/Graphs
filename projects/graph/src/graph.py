"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError('Vertex does not exist')

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist')

    def bft(self, starting_vertex_id):
        #1: empty queue
        q = Queue()
        #2: add starting to queue
        q.enqueue(starting_vertex_id)
        #3: empty set for visited vertices
        visited = set()

        #4: while loop for when queue has items
        while q.size() > 0:
            #5: dequeue first node
            v = q.dequeue()
            if v not in visited:
                #6: add unvisited into visited set
                print(v)
                visited.add(v)

                #7: add all children into queue
                for next_vert in self.vertices[v]:
                    q.enqueue(next_vert)

    def dft(self, starting_vertex_id):
        #1: empty stack
        s = Stack()
        #2: add starting to stack
        s.push(starting_vertex_id)
        #3: empty set for visited vertices
        visited = set()
        #4: while loop for when stack has items
        while s.size() > 0:
            #5: pop off last node
            v = s.pop()
            if v not in visited:
                #6: add unvisited into visited set
                print(v)
                visited.add(v)

                #7: add all children into stack
                for next_vert in self.vertices[v]:
                    s.push(next_vert)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
