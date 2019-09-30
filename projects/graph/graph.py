"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from typing import Optional, NoReturn, List
from collections import defaultdict

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.adj_matrix = [[0 for _ in self.vertices]
                           for _ in self.vertices]

    def vert_not_exists_error(self, v: int) -> Optional[NoReturn]:
        """
        show an error to the screen if vertex does not exist
        """
        try:
            assert v in self.vertices.keys()
        except AssertionError:
            raise Exception(f"Vertex {v} does not exist")
        else:
            return None

    @property
    def adj_matrix_(self):
        """

        """
        return self.adj_matrix

    @adj_matrix_.setter
    def adj_matrix_(self):
        """ should run every time a new vert is added"""
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * len(self.adj_matrix)+1)
        pass

    def add_vertex(self, vertex: int):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        pass

    def add_edge(self, v1: int, v2: int):
        """
        Add a directed edge to the graph.
        """
        self.vert_not_exists_error(v1)
        self.vert_not_exists_error(v2)

        self.vertices[v1].add(v2)
        pass

    def add_undirected_edge(self, v1: int, v2: int):
        """
        add an undirected edge
        """
        self.vert_not_exists_error(v1)
        self.vert_not_exists_error(v2)

        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)
        pass

    def bft(self, starting_vertex: int) -> List[int]:
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        """
        # initialize all to "unvisited"
        #colors = dict()
        #for v in self.vertices:
        #    colors[v] = 'white'
        colors = defaultdict(lambda: 'white')

        # mark starting vertex as "visited"
        colors[starting_vertex] = 'blue'

        q = Queue()
        q.enqueue(starting_vertex)

        order = [starting_vertex]
        while q.queue:
            u = q.queue[0]
            for v in self.vertices[u]:
                if colors[v] == 'white':
                    colors[v] = 'blue'
                    order.append(v)
                    q.enqueue(v)

            q.dequeue()
            colors[u] = 'black'

        return order

    def dft(self, starting_vertex: int) -> List[int]:
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        implemented from this https://github.com/quinn-dougherty/Graphs/tree/master/objectives/depth-first-search#pseudocode-for-dfs
        """
        order = list()
        colors = defaultdict(lambda: 'white')
        parents = defaultdict()

        def dft_visit(v: int) -> None:
            colors[v] = 'blue'
            order.append(v)
            for neighbor in self.vertices[v]:
                if colors[neighbor]=='white':
                    parents[neighbor] = v

                    dft_visit(neighbor)
            pass

        for v in self.vertices:
            if colors[v]=='white':
                dft_visit(v)

        return order


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass  # TODO

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
    print(graph.dft(1))

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
    print(graph.bft(1))

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
