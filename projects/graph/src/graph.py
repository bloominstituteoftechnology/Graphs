"""
Simple graph implementation compatible with BokehGraph class.
"""

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)

class Stack:
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

class Vertex:
    def __init__(self, v_id, value=None):
        self.id = v_id
        self.edges = set()
        self.value = v_id if value is None else value

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex) 
        else:
            raise ValueError(f'Vertex {vertex} already exists')
    
    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices:
            if vertex_2 in self.vertices:
                self.vertices[vertex_1].edges.add(vertex_2)
                self.vertices[vertex_2].edges.add(vertex_1)
            else:
                raise ValueError(f'Edge {vertex_1} already exists with Vertex {vertex_2}')
        else:
            raise ValueError(f'Vertex {vertex_2} does not exist')

    def bfs(self, start, target=None):
        # init queue
        q = Queue()

        # add start value
        q.enqueue(start)

        # init visited
        visited = []

        # loop over queue size
        while q.size() > 0:

            # declare current value
            vertex = q.dequeue()

            # check visited elements
            if vertex not in visited:

                # print value
                print(self.vertices[vertex].value)

                # add to visited
                visited.append(vertex)

                # loop for children nodes
                for next_vertex in self.vertices[vertex].edges:

                    # add next value to queue
                    q.enqueue(next_vertex)

    def dfs(self, start, target=None):
        # init stack
        s = Stack()

        # add start value
        s.push(start)

        # init visited
        visited = []

        # loop over stack size
        while s.size() > 0:

            # declare current value
            vertex = s.pop()

            # check visited elements
            if vertex not in visited:

                # print value
                print(self.vertices[vertex].value)

                # add to visited
                visited.append(vertex)

                # loop for children nodes
                for next_vertex in self.vertices[vertex].edges:
             
                    # add next value to stack
                    s.push(next_vertex)

    def search(self, method, start, target=None):
        if method == 'dfs':
            return self.dfs(start, target)
        else:
            return self.bfs(start, target)

demo_g = Graph()
demo_g.add_vertex('0')
demo_g.add_vertex('1')
demo_g.add_vertex('2')
demo_g.add_vertex('3')
demo_g.add_edge('0', '1')
demo_g.add_edge('0', '3')
demo_g.add_edge('1', '2')
# for vertex in demo_g.vertices:
#     print(f'{vertex}: {demo_g.vertices[vertex].edges}')

# print(demo_g.bfs('0'))
# print(demo_g.bfs('1'))
# print(demo_g.bfs('2'))
# print(demo_g.bfs('3'))
# print(demo_g.dfs('0'))
# print(demo_g.dfs('1'))
# print(demo_g.dfs('2'))
# print(demo_g.dfs('3'))

# print(demo_g.search(method=None, start='0', target='3'))
# print(demo_g.search(method='dfs', start='0', target='3'))
