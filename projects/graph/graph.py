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
        unvisited = {v for v in self.vertices.keys() if v != starting_vertex}
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() != 0:
            vertex_id = queue.dequeue()
            neighbors = self.vertices[vertex_id]

            for neighbor_id in neighbors:
                if neighbor_id in unvisited:
                    unvisited.remove(neighbor_id)
                    queue.enqueue(neighbor_id)
            print(vertex_id)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        unvisited = {v for v in self.vertices.keys() if v != starting_vertex}
        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() != 0:
            vertex_id = stack.pop()
            neighbors = self.vertices[vertex_id]

            for neighbor_id in neighbors:
                if neighbor_id in unvisited:
                    unvisited.remove(neighbor_id)
                    stack.push(neighbor_id)
            print(vertex_id)

    def dft_recursive(self, starting_vertex, unvisited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if unvisited is None:
            unvisited = {
                v for v in self.vertices.keys() if v != starting_vertex
            }
        for neighbor_id in self.vertices[starting_vertex]:
            if neighbor_id in unvisited:
                unvisited.remove(neighbor_id)
                self.dft_recursive(neighbor_id, unvisited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        unvisited = {v for v in self.vertices.keys() if v != starting_vertex}
        queue = Queue()
        queue.enqueue([starting_vertex])

        while queue.size() != 0:
            path = queue.dequeue()
            vertex_id = path[-1]

            if vertex_id == destination_vertex:
                return path

            neighbors = self.vertices[vertex_id]
            for neighbor_id in neighbors:
                if neighbor_id in unvisited:
                    unvisited.remove(neighbor_id)
                    new_path = path.copy()
                    new_path.append(neighbor_id)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        unvisited = {v for v in self.vertices.keys() if v != starting_vertex}
        stack = Stack()
        stack.push([starting_vertex])

        while stack.size() != 0:
            path = stack.pop()
            vertex_id = path[-1]

            if vertex_id == destination_vertex:
                return path

            neighbors = self.vertices[vertex_id]
            for neighbor_id in neighbors:
                if neighbor_id in unvisited:
                    unvisited.remove(neighbor_id)
                    new_path = path.copy()
                    new_path.append(neighbor_id)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def find_path(destination, unvisited, path):
            vertex = path[-1]
            if vertex == destination_vertex:
                return path

            for neighbor_id in self.vertices[vertex]:
                if neighbor_id in unvisited:
                    unvisited.remove(neighbor_id)
                    new_path = path.copy()
                    new_path.append(neighbor_id)
                    found_path = find_path(destination, unvisited, new_path)
                    if len(found_path) != 0:
                        return found_path
            return []

        path = [starting_vertex]
        unvisited = {v for v in self.vertices.keys() if v != starting_vertex}
        path = find_path(destination_vertex, unvisited, path)
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
    print("graph vertices:")
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
    print("\nbft:")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\ndft:")
    graph.dft(1)
    print("\ndft recursive:")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\nbfs:")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("\ndfs:")
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
