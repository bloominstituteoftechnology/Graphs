"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


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
        if v1 in self.vertices and v2 in self.vertices:
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
        q = Queue()

        q.enqueue(starting_vertex)
        # 1

        visited = set()

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)
                #visited(1, 2)

                for vertex in self.get_neighbors(v):
                    # 2

                    q.enqueue(vertex)
                #q = [3,4]


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
    #   s = [v,neightbor1, neightbor2]
        # LIFO
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:

            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)

                for vertex in self.get_neighbors(v):
                    s.push(vertex)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        """
        if starting_vertex in self.vertices:
            print(starting_vertex)
            visited.add(starting_vertex)

            for vertex in self.get_neighbors(starting_vertex):
                if vertex not in visited:
                    self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
        """
        # keep track of explored nodes
        visited = set()
    # keep track of all the paths to be checked
        q = Queue()
       
        q.enqueue([starting_vertex])

        if starting_vertex == destination_vertex:
            return q[-1]

        while q.size() > 0:

            path = q.dequeue()

            node = path[-1]  # 3,
            [1]

            if node not in visited:
                visited.add(node)
                for vertex in self.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(vertex)
                    print('new_path', new_path)

                    q.enqueue(new_path)
                    q = [[1, 2, 3], [1, 2, 4]]

                    # return path if neighbour is goal
                    if vertex == destination_vertex:
                        return new_path
                        # [1,2]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
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
        1-->2-->3 <---> 5

            2-->4 ---> 6
                4 --->7
    '''
    # print(graph.vertices)

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
    # print(graph.bft(1))

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # print(graph.dft_recursive(1))

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
# path [1]x
# new_path [1]x
# new_path1 [1, 2]x
# path [1, 2]
# new_path [1, 2]x
# new_path1 [1, 2, 3]x
# new_path [1, 2]
# new_path1 [1, 2, 4]
# path [1, 2, 3]
# new_path [1, 2, 3]
# new_path1 [1, 2, 3, 5]
# path [1, 2, 4]
# new_path [1, 2, 4]
# new_path1 [1, 2, 4, 6]
# [1, 2, 4, 6]


# path [1] x
# new_path [1]x
# new_path1 [1, 2]x
# path [1, 2] x
# new_path [1, 2]x
# new_path1 [1, 2, 3]x
# new_path [1, 2, 3]
# new_path1 [1, 2, 3, 4]
# path [1, 2, 3, 4]
# new_path [1, 2, 3, 4]
# new_path1 [1, 2, 3, 4, 6]
# [1, 2, 3, 4, 6]
