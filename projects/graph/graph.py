"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    
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
        printed = set()
        to_print = Queue()
        to_print.enqueue(starting_vertex)
        while to_print.size() > 0:
            vertex = to_print.dequeue()
            if vertex not in printed:
                print(vertex)
                printed.add(vertex)
            for edge in self.vertices[vertex]:
                if edge not in printed:
                    to_print.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        printed = set()
        to_print = Stack()
        to_print.push(starting_vertex)
        while to_print.size() > 0:
            vertex = to_print.pop()
            if vertex not in printed:
                print(vertex)
                printed.add(vertex)
            for edge in self.vertices[vertex]:
                if edge not in printed:
                    to_print.push(edge)
        

    def dft_recursive(self, starting_vertex, printed=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if printed is None:
            printed = set()
        print(starting_vertex)
        printed.add(starting_vertex)
        for edge in self.vertices[starting_vertex]:
            if edge not in printed:
                self.dft_recursive(edge, printed)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self,
                      starting_vertex,
                      destination_vertex,
                      visited=[],
                      deadend=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = []
        if starting_vertex == destination_vertex:
            return visited + [starting_vertex]
        else:
            visited.append(starting_vertex)
            for edge in self.vertices[starting_vertex]:
                if edge not in visited and edge not in deadend:
                    path = self.dfs_recursive(edge, 
                                              destination_vertex, 
                                              visited)
                    if path is not None:
                        return path
            visited.remove(starting_vertex)
            deadend.append(starting_vertex)

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
    print('BFT')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT')
    graph.dft(1)
    print('DFT recursive')
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
    print('DFS')
    print(graph.dfs(1, 6))
    print('DFS recursive')
    print(graph.dfs_recursive(1, 6))
