"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id] if vertex_id in self.vertices else None

    def bft(self, starting_vertex):
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        visited = set()
        stack = Stack()
        stack.push(starting_vertex)
        while stack.size() > 0:
            currNode = stack.pop()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        path += [starting_vertex]
        print(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in path:
                self.dft_recursive(neighbor, path)

    def bfs(self, starting_vertex, destination_vertex):
        visited = set()
        queue = Queue()
        queue.enqueue({'current_vertex': starting_vertex,
        'path': [starting_vertex]})
        while queue.size() > 0:
            currNode = queue.dequeue()
            curr_path = currNode['path']
            curr_vertex = currNode['current_vertex']
            if curr_vertex not in visited:
                if curr_vertex == destination_vertex:
                    return curr_path
                visited.add(curr_vertex)
                for neighbor in self.get_neighbors(curr_vertex):
                    new_path = list(curr_path)
                    new_path.append(neighbor)
                    queue.enqueue({'current_vertex': neighbor, 'path': new_path})

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            currPath = stack.pop()
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.push(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        path += [starting_vertex]
        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in path:
                path = self.dfs_recursive(neighbor, destination_vertex, path)
        return path



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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
