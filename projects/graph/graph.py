"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].add(v2)
            
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    
    def bft(self, starting_vertex):
        q= Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            current_node = q.dequeue()
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            current_node = s.pop()
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = set()):
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            for i in neighbors:
                self.dft_recursive(i, visited)
            
    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        visited = []
        current_node = starting_vertex
        while current_node != destination_vertex:
            if current_node not in visited:
                visited.append(current_node)
                neighbors = self.get_neighbors(current_node)
                for i in neighbors:
                    if i == destination_vertex:
                        visited.append(i)
                        return visited
                    if i not in visited:
                        current_node = i
                    
    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push(starting_vertex)
        visited = []
        current_node = s.pop()
        while current_node != destination_vertex:
            if current_node not in visited:
                visited.append(current_node)
                neighbors = self.get_neighbors(current_node)
                for i in neighbors:
                    if i == destination_vertex:
                        visited.append(i)
                        return visited
                    if i not in visited:
                        current_node = i

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = []):
        if starting_vertex == destination_vertex:
            visited.append(starting_vertex)
            print(visited)
            return visited
        if starting_vertex not in visited:
            print(visited)
            visited.append(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            for i in neighbors:
                if destination_vertex in neighbors:
                    print(visited, 'v')
                if i not in visited:
                    self.dfs_recursive(i, destination_vertex, visited)
                                        

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
