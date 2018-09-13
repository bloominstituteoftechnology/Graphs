"""
Simple graph implementation compatible with BokehGraph class.
"""
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

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    # def add_edge(self, edge):
    #     edge = set(edge)
    #     (vertex1, vertex2) = tuple(edge)
    #     if vertex1 in self.vertices:
    #         self.vertices[vertex1].append(vertex2)
    #     else:
    #         self.vertices[vertex1] = [vertex2]

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            print(f"Cannot create edge between {vertex1} and {vertex2}, vertex does not exist")
            return
        self.vertices[vertex1].add(vertex2)
        self.vertices[vertex2].add(vertex1)

    def breadth_first(self, start_vert_id):
        q = Queue()
        q.enqueue(start_vert_id)
        visited = []
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(self.vertices[v].value)
                visited.append(v)
                for next_vert in self.vertices[v].edges:
                    q.enqueue(next_vert)

graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')