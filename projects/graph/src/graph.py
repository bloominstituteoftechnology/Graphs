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

    # def dft_recursion(self, starting_vertex, path=[]):
    #     path += [starting_vertex]
    #     print(path)
    #     for neighbor in self.vertices[starting_vertex]:
    #         if neighbor not in path:
    #             path = self.dft_recursion(neighbor, path)
    #     return path
    def dft_r(self, starting_vertex_id, visited=None):
        if visited is None:
            visited = set()
        # Mark the starting node as visited
        visited.add(starting_vertex_id)
        # Then call dft_r() on each unvisited neighbor
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_r(neighbor, visited)

    # def bfs(self, start, end):
    #     verts = self.vertices
    #     # maintain a queue of paths
    #     queue = []
    #     # push the first path into the queue
    #     queue.append([start])
    #     while len(queue) > 0:
    #         # get the first path from the queue
    #         path = queue.pop(0)
    #         # get the last node from the path
    #         node = path[-1]
    #         # path found
    #         if node == end:
    #             return print(path)
    #         # enumerate all adjacent nodes, construct a new path and push it into the queue
    #         for adjacent in verts.get(node, []):
    #             new_path = list(path)
    #             new_path.append(adjacent)
    #             queue.append(new_path)
    def bfs(self, starting_vertex_id, target_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited verts
        visited = set()
        # Put the path to the starting vert in our queue
        q.enqueue([starting_vertex_id])
        # while the queue is not empty...
        while q.size() > 0:
            # Dequeue the first path from the queue
            path = q.dequeue()
            # Get the current node from the last element in the path
            print(path)
            v = path[-1]
            # if the node has not been visited...
            if v not in visited:
                # Mark it as visited
                return path
            for neighbor in self.vertices[v]:
                # copy the path into a new instance
                new_path = list(path)
                # append the neighbor to the end of the path
                new_path.append(neighbor)
                # enqueue
                q.enqueue(new_path)

    def dfs(self, start, end):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(start)
        # While the value passed as "end" is not in the visit array....
        while end not in visited:
            # Pop the top node from the stack
            v = s.pop()
            # If that node has not been visted...
            if v not in visited:
                    # Mark it as visited
                print(v)
                visited.add(v)
                # Then, put all of it's children into the stack
                if v is not None:
                    for neighbor in self.vertices[v]:
                        s.push(neighbor)
                else:
                    return print("they don't connect")


graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('5', '3')  # 1
graph.add_directed_edge('6', '3')  # 2
graph.add_directed_edge('7', '1')  # 3
graph.add_directed_edge('4', '7')  # 4
graph.add_directed_edge('1', '2')  # 5
graph.add_directed_edge('7', '6')  # 6
graph.add_directed_edge('2', '4')  # 7
graph.add_directed_edge('3', '5')  # 8
graph.add_directed_edge('2', '3')  # 9
graph.add_directed_edge('4', '6')  # 10
# print(graph.vertices)

graph.bfs('4', '6')
