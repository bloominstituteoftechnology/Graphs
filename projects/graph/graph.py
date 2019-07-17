"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            self.vertices[v1] = set(v2)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = [False] * (len(self.vertices) + 1)
        queue = []
        queue.append(starting_vertex)
        visited[starting_vertex] = True
        # print("BFT visited", starting_vertex)

        while queue:
            starting_vertex = queue.pop(0)
            for i in self.vertices[starting_vertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        if visited is None:
            visited = [False]*(len(self.vertices) + 1)

        visited[starting_vertex] = True
        # print("DFT visited", starting_vertex)

        for i in self.vertices[starting_vertex]:
            if visited[i] is False:
                self.dft(i, visited)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if len(visited) == len(self.vertices):
            print()
            return

         if starting_vertex not in visited:
            visited.append(starting_vertex)
            print(starting_vertex, end=", ")

             for edge in self.vertices[starting_vertex]:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        visited = [False] * (len(self.vertices) + 1)
        queue = []
        queue.append(starting_vertex)
        visited[starting_vertex] = True

        match = None

        while queue and match is None:
            starting_vertex = queue.pop(0)
            if starting_vertex == destination_vertex:
                match = starting_vertex
            for i in self.vertices[starting_vertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return match


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        
        s.push([starting_vertex])
        while s.size():
            path = s.pop()
            vertex = path[-1]
            if vertex == destination_vertex:
                return path
            elif vertex not in visited:
                for next in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next)
                    s.push(new_path)
                visited.add(vertex)
        if vertex != destination_vertex:
            return f"path from {starting_vertex} to {destination_vertex} not found"
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
