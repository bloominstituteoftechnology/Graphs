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

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vert")

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

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

         """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        # q.enqueue(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()
        q.enqueue([starting_vertex])

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()

            # Grab the last vertex from the PATH
            v = path[-1]

            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path

                # Mark it as visited...
                visited.add(v)

                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    # COPY THE PATH
                    new = path.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    new.append(neighbor)
                    q.enqueue(new)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        v = Stack()
        visited = set()
        v.push([starting_vertex])

        while v.size() > 0:
            n = v.pop()
            last_vertex = n[-1]
            if last_vertex not in visited:
                visited.add(last_vertex)
            else:
                continue

            for neighbor in self.get_neighbors(last_vertex):
                new = n.copy()
                new.append(neighbor)
                v.push(new)
                if neighbor == destination_vertex:
                    return new

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex in visited:
            return None
        elif starting_vertex == destination_vertex:
            return [destination_vertex]
        else:
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                neighborSearch = self.dfs_recursive(neighbor, destination_vertex, visited)
                if neighborSearch is not None:
                    return [starting_vertex] + neighborSearch
            return None


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
