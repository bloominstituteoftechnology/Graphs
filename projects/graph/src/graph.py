from collections import OrderedDict, defaultdict

"""
Simple graph implementation
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
        return (len(self.queue))


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
        return (len(self.stack))


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # While the queue is not empty....
        while q.size() > 0:
            # Dequeue the first node from the queue
            v = q.dequeue()
            # If that node has not been visted...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(starting_vertex_id)
        # While the stack is not empty....
        while s.size() > 0:
            # Pop the top node from the stack
            v = s.pop()
            # If that node has not been visted...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dftr(self, starting_vertex_id, cache=set()):
        print(starting_vertex_id)
        cache.add(starting_vertex_id)
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in cache:
                self.dftr(neighbor, cache)

    def dfs(self, starting_vertex_id, target):
        if target == starting_vertex_id:
            print("But that's the same thing")
        s = Stack()
        s.push(starting_vertex_id)
        paths = {starting_vertex_id: [starting_vertex_id]}

        while s.size() > 0:
            v = s.pop()
            if v == target:
                return paths
            for neighbor in self.vertices[v]:
                if neighbor not in paths:
                    paths[neighbor] = list(paths[v])
                    paths[neighbor].append(neighbor)
                    s.push(neighbor)
                    if neighbor == target:
                        print(paths[neighbor])
                        return paths[neighbor]

        print("Are you sure that's in there?")

    def bfs(self, starting_vertex_id, target):
        if target == starting_vertex_id:
                print("but that's the same thing")
        q = Queue()
        q.enqueue(starting_vertex_id)

        paths = {starting_vertex_id: [starting_vertex_id]}

        while q.size() > 0:

        # Add all edges of given vertex to queue
            v = q.dequeue()
            for neighbor in self.vertices[v]:
                if neighbor not in paths:
                # for i in self.vertices[queue[0]]:

                # If vertex has not been visited, cache its path
                # if i not in paths:
                    paths[neighbor] = list(paths[v])
                    paths[neighbor].append(neighbor)
                    q.enqueue(neighbor)

                        # If vertex matches target, return target
                    if neighbor == target:
                        print(paths[neighbor])
                        return paths[neighbor]

        print("Are you sure that's in there?")



graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('5', '3')
graph.add_directed_edge('6', '3')
graph.add_directed_edge('7', '1')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('7', '6')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('3', '5')
graph.add_directed_edge('4', '6')
graph.add_directed_edge('2', '3')
graph.dfs('1', '7')
graph.bfs('1', '7')
