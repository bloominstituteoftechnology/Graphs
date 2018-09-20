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

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color='white'):
        self.id=int(vertex_id)
        self.x = x
        self.y = y
        self.value=value
        self.color=color
        self.edges=set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id % 3)
        if self.y is None:
            self.y = 2 * (self.id % 3) + self.id / 10 * (self.id // 3)
        if self.value is None:
            self.value = self.id


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise Exception('That vertex does not exist.')
    def add__directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise Exception('That vertex does not exist.')

    # def dft(self, start_vert, visited=[]):
    #     # visited checks if we've visited the node before
    #     visited.append(start_vert)
    #     # touch visited node
    #     print(self.vertices[start_vert].value)
    #     # call DFS on eac child (that has not been visited)
    #     for el in self.vertices[start_vert].edges:
    #         # check if child has been visited
    #         if el not in visited:
    #             # if not, call DFS
    #             self.dft(el)
  
    def dft_stack(self, starting_vertex_id):
        # create empty queue
        stack = Stack()
        # put starting vert in the queue
        stack.push(starting_vertex_id)
        # declare visited list
        visited = []
        # while the queue is not empty
        while stack.size() > 0:
            # remove the first item from the queue
            v = stack.pop()
            # then if it has nit been visited
            if v not in visited:
                # print it's value
                print(self.vertices[v].value)
                visited.append(v) # mark as visited
                # then put its child into the queue
                for next_el in self.vertices[v].edges:
                    stack.push(next_el)

    def bft(self, starting_vertex_id):
        # create empty queue
        q = Queue()
        # put starting vert in the queue
        q.enqueue(starting_vertex_id)
        # declare visited list
        visited = []
        # while the queue is not empty
        while q.size() > 0:
            # remove the first item from the queue
            v = q.dequeue()
            # then if it has nit been visited
            if v not in visited:
                # print it's value
                print(self.vertices[v].value)
                visited.append(v) # mark as visited
                # then put its child into the queue
                for next_el in self.vertices[v].edges:
                    q.enqueue(next_el)


    def dfs(self, start_vert, target_value, visited=[]):
        visited.append(start_vert)
        if self.vertices[start_vert].value == target_value:
            return True
        for child_vert in self.vertices[start_vert].edges:
            if child_vert not in visited:
                if self.dfs(child_vert, target_value, visited):
                    return True
        return False
    


    def bfs(self, starting_vertex_id, target_value):
        q = Queue()
        q.enqueue(starting_vertex_id)
        visited = []
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                if self.vertices[v].value == target_value:
                    return True
                # print(self.vertices[v].value)
                visited.append(v)
                for next_el in self.vertices[v].edges:
                    q.enqueue(next_el)
        return False

