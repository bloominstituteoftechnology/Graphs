"""
Simple graph implementation
"""
from collections import deque

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if (self.size()) > 0:
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

    def add_edge(self, vertex_a, vertex_b):
        if vertex_a in self.vertices.keys() and vertex_b in self.vertices.keys():
            self.vertices[vertex_a].add(vertex_b)
            self.vertices[vertex_b].add(vertex_a)
        else:
            print("Cannot find all vertices")

    def bft(self, starting_node):
        # # create a queue
        # q = Queue()
        # # markt he first node as visited
        # # enqeue starting node
        # q.enqueue(starting_node)
        # visited = []

        # while q.size() > 0:
        #     dequeued = q.dequeue()
        #     visited.append(dequeued)
        #     print(visited)
        #     # enqueue connected nodes
        #     for edge in self.vertices[dequeued].edges:
        #         if edge not in visited:
        #             q.enqueue(edge)
        # return visited
        # # remove first node from queue
        # # if it h asnt been visited
                #create queue - using built in library deque
        q = deque()
        # Enqueue starting vertex
        q.append(starting_node)
        visited = []

        #while the queue is not empty, 
        while q:
            #dequeue a vertex from the queue 
            current_v = q.popleft()
            #...and mark it as visited 
            if current_v not in visited:
                visited.append(current_v)
                #enqueue all of it's children that have not been visited 
                for edge in self.vertices[current_v]:
                    q.append(edge)

        print(visited)

    def dft(self, starting_node):
        # s = Stack()

        # visited = []

        # s.push(starting_node)

        # while s:
        #     # dequeue node from stack
        #     dequeued = s.pop()
        #     # mark it as visited
        #     if dequeued not in visited:
        #         visited.append(dequeued)
        #         print(dequeued)
        #     for vert in self.vertices[dequeued]:
        #         if vert not in visited:
        #             s.push(vert)
        #     return visited
                #create stack
        s = deque()
        #push starting vertex
        s.append(starting_node)
        visited = []
        #while the stack is not empty, 
        while s:
            #pop a vertex from the stack
            current_v = s.pop()
            #mark it as visited 
            if current_v not in visited:
                visited.append(current_v)
            #push all of it's children that have not been visited 
                for edge in self.vertices[current_v]:
                    s.append(edge)

        print(visited)

    def dft_r(self, starting_node, visited=None):
        # mark node as visited
        if visited is None:
            visited = []
        if starting_node not in visited:
            visited.append(starting_node)
            print(starting_node)
        # call dft_r on all children
        for vert in self.vertices[starting_node]:
            if vert not in visited:
                self.dft_r(vert, visited)

    def bfs(self, starting_node, target_node):
        q = Queue()
        visited = []
        # put start in the queue
        q.enqueue(starting_node)
        while q:
            dequeued = q.dequeue()
            if dequeued == target_node:
                return True
            if dequeued not in visited:
                visited.append(dequeued)
            for vert in self.vertices[dequeued]:
                if vert not in visited:
                    q.enqueue(vert)

        return False

    def dfs(self, starting_node, target_node):
        s = deque()
        #push starting vertex
        s.append(starting_node)
        visited = []
        #while the stack is not empty, 
        while s:
            #pop a vertex from the stack
            current_v = s.pop()
            #mark it as visited 
            if current_v == target_node:
                return True
            if current_v not in visited:
                visited.append(current_v)
            #push all of it's children that have not been visited 
                for edge in self.vertices[current_v]:
                    s.append(edge)

        print(visited)


graph = Graph()  # my graph instance
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
graph.add_edge('1', '3')
graph.add_edge('9', '2')
graph.add_edge('2', '3')
graph.add_edge('4', '5')
graph.add_edge('3', '4')
graph.add_edge('5', '9')
graph.add_edge('6', '7')
graph.add_edge('7', '9')
graph.add_edge('2', '8')

print(graph.vertices)

graph.bft('2')
