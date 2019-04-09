"""
Simple graph implementation
"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, num):
        if num not in self.vertices:
            self.vertices[num] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)


    def addDoubleEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v2].add(v1)
            self.vertices[v1].add(v2)

    def bft(self, node):
        q = Queue()
        visited = []
        q.enqueue(node)

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.append(v)
                for nextVertice in self.vertices[v]:
                    q.enqueue(nextVertice)
        return visited

    def bfs(self, root, searching):
        # Queue is an array of paths
        q = Queue()
        visited = []
        q.enqueue([root])

        while q.size() > 0:
            path = q.dequeue()
            node = path[-1]

            if node not in visited:
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    nextPath = list(path)
                    nextPath.append(neighbor)
                    q.enqueue(nextPath)
                    if neighbor == searching:
                        return nextPath
                visited.append(node)
        return None

    def dft(self, node):
        s = Stack()
        visited = []
        s.push(node)

        while not s.isEmpty():
            v = s.pop()
            if v not in visited:
                visited.append(v)
                for nextVertice in self.vertices[v]:
                    s.push(nextVertice)
        return visited

    def dfs(self, root, searching):
        # Queue is an array of paths
        s = Stack()
        visited = []
        s.push([root])

        while s.size() > 0:
            path = s.pop()
            node = path[-1]

            if node not in visited:
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    nextPath = list(path)
                    nextPath.append(neighbor)
                    s.push(nextPath)
                    if neighbor == searching:
                        return nextPath
                visited.append(node)
        return None



graph = Graph()
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')

graph.add_directed_edge('1', '2')
graph.add_directed_edge('1', '3')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('3', '4')
graph.add_directed_edge('3', '5')
graph.add_directed_edge('3', '1')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('5', '6')
graph.add_directed_edge('5', '7')
graph.add_directed_edge('7', '2')

print(f'Graph is: {graph.vertices})')
#print(graph.bft('1'))
#print(graph.dft('1'))

#print(graph.bfs('1', '7'))
print(graph.dfs('1', '2 '))




