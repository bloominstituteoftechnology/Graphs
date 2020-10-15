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
        # keep track of edges
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndentationError("Nonexixtent vert")

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
        # create queue
        q = Queue()
        # create set of visited
        visited = set()
        # init enqueue and starting node
        q.enqueue(starting_vertex)
        # while loop while queue isnt empty
        while q.size() > 0:
            # deque the first item
            v = q.dequeue()
            # if its hasnt been visited
            if v not in visited:
                # mark as visited
                visited.add(v)
                print(v)
                # add neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # instantiate visited if none
        if visited is None:
            visited = set()
        # check if node has been visited
        if starting_vertex not in visited:
            # if not:
            # add to visited
            visited.add(starting_vertex)
            print(starting_vertex)
            # call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v not in visited:
                if v == destination_vertex:
                    return path

                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    new_path = list(path)  # copy the list
                    new_path.append(next_vert)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack
        s = Stack()
        # push a path to the starting vertex
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop off the first path
            path = s.pop()
            # grab the last vertex from the path
            v = path[-1]
            # check if it's been visited
            # if it hasn't been visited
            if v not in visited:
                # mark it as visited
                visited.add(v)
                # check if it's the targeted vertex
                if v == destination_vertex:
                    # if it is, return the path
                    return path
                # otherwise, push a path to all its neighbors
                # for each neighbor:
                for neighbor in self.get_neighbors(v):
                    # make a copy of current path
                    new_path = path.copy()
                    # add neighbor to the end
                    new_path.append(neighbor)
                    # push the new path
                    s.push(new_path)

    def dfs_recursive(
        self, starting_vertex, destination_vertex, visited=None, path=None
    ):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize visited and/or path if None:
        if visited is None:
            visited = set()
        if path is None:
            path = []
        # check if starting vertx has been visited
        # if it hasn't been visited
        # mark it as visited
        visited.add(starting_vertex)
        # add to path
        path = path + [starting_vertex]
        # check if it's the targeted vertex:
        if starting_vertex == destination_vertex:
            # if it is, return the path - END POINT
            return path
        # otherwise, check neighbors of current vertex
        for next_vertex in self.get_neighbors(starting_vertex):
            # if neighbor not visited:
            if next_vertex not in visited:
                # call dfs_recursive on neighbor w/ updated path
                new_path = self.dfs_recursive(
                    next_vertex, destination_vertex, visited, path
                )
                # get back either None or valid path to destination vertex
                # if valid path, return it back up the chain
                if new_path:
                    return new_path
        # if not target and all neighbors visited, return none END?
        return None


if __name__ == "__main__":
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

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    print(graph.vertices)

    """
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
    """
    graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    graph.dft(1)
    graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
