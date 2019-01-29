"""
Simple graph implementation
"""


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None


class Stack:
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()
        else:
            return None


class Vertex:
    def __init__(self, value):
        self.value = value
        self.color = 'white'
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of
    vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = []

    def add_vertex(self, value):
        node = Vertex(value)
        self.vertices.append(node)

    def add_edge(self, first_value, sec_value):
        vertex = None
        edge = None
        for v in self.vertices:
            if v.value == first_value:
                vertex = v
            elif v.value == sec_value:
                edge = v

        vertex.edges.add(edge)

    def bft(self, starting_node):
        print('Breadth First Traversal')
        q = Queue()
        start_vertex = None
        for vertex in self.vertices:
            if vertex.value == starting_node:
                start_vertex = vertex

        for v in self.vertices:
            v.color = 'white'

        start_vertex.color = 'gray'
        q.enqueue(start_vertex)
        while len(q.storage) > 0:
            u = q.storage[0]

            for v in u.edges:
                if v.color == 'white':
                    v.color = 'gray'
                    q.enqueue(v)

            q.dequeue()
            u.color = 'black'
            print(u.value)

        print('--------')


graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_edge('1', '2')
graph.add_edge('2', '3')
graph.add_edge('2', '4')
graph.add_edge('3', '5')
graph.add_edge('4', '6')
graph.add_edge('4', '7')
graph.add_edge('5', '3')
graph.add_edge('6', '3')
graph.add_edge('7', '6')
graph.add_edge('7', '1')

# graph.add_edge('0', '20')
# for v in graph.vertices:
#     print(v.edges)
# graph.bft('2')
graph.bft('1')

# graph.dft('1')

# graph.dft_r('1')

# print(graph.dfs('3', '4'))
