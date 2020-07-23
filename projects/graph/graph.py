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
        # make queue
        q = Queue()
        # enqueue our start node
        q.enqueue(starting_vertex)
        # make a set to track visited nodes
        visited = set()
        # whilie queue still has things in it
        while q.size():
            # dequeue from front of the line, this is the current node
            curr_node = q.dequeue()
            # check if we visited, if not:
            if curr_node not in visited:
                # mark it as visited
                visited.add(curr_node)
                print(curr_node)
            # get it's neighbors (add neighbors to "neighbors stack")
                neighbors = self.get_neighbors(curr_node)
            # iterate over neighbors
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # make a stack
        s = Stack()
        # push our starting node onto the stack
        s.push(starting_vertex)
        # make a set to track the nodes we've visited
        visited = set()
        # as long as our stack isn't empty
        while s.size():
            # pop off the top, this is our current node
            current_node = s.pop()
        # check if we have visited this before and if not:
            if current_node not in visited:
                # mark it as visited
                visited.add(current_node)
                print(current_node)
        # get it's neighbors (add neighbors to "neighbors stack")
                neighbors = self.get_neighbors(current_node)
        # iterate over neighbors
                for neighbor in neighbors:
                    # aand add them to our stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)

            for neighbor in neighbors:
                self.dft_recursive(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        q = Queue()

        q.enqueue(starting_vertex)

        visited = set()

        shortest_path = []
        found = False

        while q.size() and not found:

            curr_node = q.dequeue()

            while q.size() > 0 and curr_node != destination_vertex:
                curr_node = q.dequeue()

            if curr_node not in visited:

                visited.add(curr_node)
                shortest_path.append(curr_node)

                neighbors = self.get_neighbors(curr_node)

                for neighbor in neighbors:

                    q.enqueue(neighbor)

            if curr_node == destination_vertex:
                found = True

        return shortest_path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push(starting_vertex)

        visited = set()

        shortest_path = []
        found = False

        while s.size() and not found:

            curr_node = s.pop()

            # while s.size() > 0 and curr_node != destination_vertex:
            #     curr_node = s.pop()

            if curr_node not in visited:

                visited.add(curr_node)
                shortest_path.append(curr_node)

                neighbors = self.get_neighbors(curr_node)

                for neighbor in neighbors:

                    s.push(neighbor)

            if curr_node == destination_vertex:
                found = True

        return shortest_path

    def dfs_recursive(self, starting_vertex, destination_vertex,  path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        path.append(starting_vertex)

        if starting_vertex not in visited and (starting_vertex != destination_vertex):
            print("new_visited |", visited)
            neighbors = self.get_neighbors(starting_vertex)

            for neighbor in neighbors:
                path.append(self.dfs_recursive(
                    neighbor, destination_vertex, path))

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
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
