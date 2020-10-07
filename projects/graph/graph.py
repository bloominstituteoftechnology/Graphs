"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import copy


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
        else:
            raise IndexError("nonexistent vertex")

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
        # Create an empty queue
        q = Queue()

        # Add starting vertex
        q.enqueue(starting_vertex)

        # Create set for visited vertices
        visited = set()

        # While queue is not empty
        while q.size() > 0:

            # Dequeue a vertex
            v = q.dequeue()

            # If not visited
            if v not in visited:

                # Visit it!
                print(v)

                # Mark as visited
                visited.add(v)

                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Add starting vertex
        s.push(starting_vertex)

        # Create list for visited vertices
        visited = set()

        # While stack is not empty
        while(s.size()):

            # Pop a vertex from stack
            v = s.pop()

            # If not visited
            if v not in visited:

                # Visit it!
                print(v)

                # Mark as visited
                visited.add(v)

                # Add all neighbors to the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        # print current vertex
        print(starting_vertex)

        # add vertex to visited set
        visited.add(starting_vertex)

        # For each nonvisted neighbor, recursively call dft_recursive
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty stack
        q = Queue()

        # add A PATH TO the starting vertex ID
        path = [starting_vertex]
        q.enqueue(path)

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while q.size() > 0:

            # Remove the last PATH
            p = q.dequeue()

            # Grab the last vertex from the PATH
            last = p[-1]

            # If that vertex has not been visited...
            if last not in visited:

                # CHECK IF IT'S THE TARGET
                # IF SO, RETURN PATH
                if last == destination_vertex:
                    return p

                # Mark it as visited...
                visited.add(last)

                # Then add A PATH TO its neighbors to the top of the stack
                for neighbor in self.get_neighbors(last):
                    # SHALLOW COPY THE PATH
                    path = copy.copy(p)

                    # APPEND THE NEIGHOR TO THE BACK
                    path.append(neighbor)

                    q.enqueue(path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        s = Stack()

        # add A PATH TO the starting vertex ID
        path = [starting_vertex]
        s.push(path)

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size() > 0:

            # Remove the last PATH
            p = s.pop()

            # Grab the last vertex from the PATH
            last = p[-1]

            # If that vertex has not been visited...
            if last not in visited:

                # CHECK IF IT'S THE TARGET
                # IF SO, RETURN PATH
                if last == destination_vertex:
                    return p

                # Mark it as visited...
                visited.add(last)

                # Then add A PATH TO its neighbors to the top of the stack
                for neighbor in self.get_neighbors(last):
                    # SHALLOW COPY THE PATH
                    path = copy.copy(p)

                    # APPEND THE NEIGHOR TO THE BACK
                    path.append(neighbor)

                    s.push(path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = [starting_vertex]

        print(starting_vertex)
        visited.add(starting_vertex)
        # path += [starting_vertex]

        # if starting_vertex == destination_vertex:
        #     return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == destination_vertex:
                    return new_path
                dfs_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path)
                if dfs_path is not None:
                    return dfs_path
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
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
