"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            print(' Can not add edges to vertices that do not exist')
        else:
            self.vertices[v1].add(v2)
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        queue = deque()
        queue.append(starting_vertex)
        visited = set()

        while len(queue):
            current_vertex = queue.popleft()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)

    
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = deque()
        stack.append(starting_vertex)
        visited = set()

        while len(stack):
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        # create a visited
        # if start isnt in visited add it
        # print start
        # call recursive funciton for neighbors of vertix using neighbor and visited

        if not visited:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = deque()
        visited = set()
        queue.append([starting_vertex])

        while len(queue):
            current_path = queue.popleft()
            current_vertex = current_path[-1]

            if current_vertex == destination_vertex:
                return current_path

            if current_vertex not in visited:
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        queue = deque()
        visited = set()
        queue.append([starting_vertex])

        while len(queue):
            current_path = queue.pop()
            current_vertex = current_path[-1]

            if current_vertex == destination_vertex:
                return current_path

            if current_vertex not in visited:
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create a path
        # path starts with starting vertex
        # if starting vertex not in visited add to visited
        # print vertex
        # grab the neighbors of the vertex

        if not visited:
            visited = set()
        if not path:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                res = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if res:
                    return res
        return []


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/BloomInstituteOfTechnology/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
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
