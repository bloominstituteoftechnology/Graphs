"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.vertices.add_vertex(v1)
        if v2 not in self.vertices:
            self.vertices.add_vertex(v2)
        self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        queue = Queue()
        visited = set()
        path = []
        queue.enqueue(starting_vertex)
        while queue.size():
            node = queue.dequeue()
            path.append(node)
            visited.add(node)
            for edge in self.vertices[node]:
                if edge not in visited:
                    queue.enqueue(edge)
        print("BFT:", path)

    def dft(self, starting_vertex):
        stack = Stack()
        visited = set()
        path = []
        stack.push(starting_vertex)
        while stack.size():
            node = stack.pop()
            path.append(node)
            visited.add(node)
            for edge in self.vertices[node]:
                if edge not in visited:
                    visited.add(edge)
                    stack.push(edge)
        print("DFT:", path)

    def dft_recursive(self, node, visited=set()):
        if node in visited:
            # print(visited)
            return visited
        else:
            visited.add(node)
            for neighbor in self.vertices[node]:
                return self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            node = path[-1]
            if node not in visited:
                if node == destination_vertex:
                    return path
                else:
                    visited.add(node)
                    for connection in self.vertices[node]:
                        copy_path = path[:]
                        copy_path.append(connection)
                        queue.enqueue(copy_path)    

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        while stack.size():
            path = stack.pop()
            node = path[-1]
            if node is not visited:
                if node == destination_vertex:
                    return path
                else:
                    visited.add(node)
                    for connection in self.vertices[node]:
                        copy_path = path[:]
                        copy_path.append(connection)
                        stack.push(copy_path)



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft_recursive(1)
    print("DFT Recursive:", graph.dft_recursive(1))


    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS:", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS:", graph.dfs(1, 6))
