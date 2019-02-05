"""
Simple graph implementation
"""


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        return None

    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        # includes all vertices
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    # adding/creating an edge to a graph between vertices i and j
    def add_edge(self, i, j):
        # check if vertices are connected
        if i not in self.vertices or j not in self.vertices:
            raise Exception(
                'Cannot create edges on vertices that do not exist')
        if not (i in self.vertices[j]):
            # makes sure that i is included in the list of vertices that connect to j
            self.vertices[j].add(i)
            # viseversa makes sure that j is included in the list of vertices that connect to i
            self.vertices[i].add(j)

    def bft(self, target):
        queue = Queue()
        visited = []
        queue.enqueue(target)
        while queue.size():
            vertex = queue.dequeue()
            if vertex not in visited:
                visited.append(vertex)
                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        queue.enqueue(neighbor)
        return visited

    def dft(self, start_vertex):
        stack = Stack()
        visited = []
        stack.push(start_vertex)
        while stack.size():
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    stack.push(neighbor)
        return visited

    def dft_recursive(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        print(start_node)
        for child_node in self.vertices[start_node]:
            if child_node not in visited:
                self.dft_recursive(child_node, visited)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_edge('0', '1')
graph.add_edge('1', '2')
graph.add_edge('1', '4')
# graph.add_edge('5', '7')

# graph.add_edge(1, 3)
# graph.add_edge(2, 3)
# graph.add_edge(2, 4)
# graph.add_edge(2, 1)
print(graph.vertices)
# print(graph.bft('1'))
# print(graph.dft('1'))
# print(graph.dft_recursive('1'))
