"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import pdb


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels
    to edges.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Incorrect Index Passed')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create empty set
        vertices = set()
        # Create empty Queue
        queue = Queue()

        queue.enqueue(starting_vertex)

        # Iterate each level and get the next level vertices
        while queue.size() > 0:
            vertex = queue.dequeue()

            # Check and update the set
            if vertex not in vertices:
                print(vertex)
                vertices.add(vertex)

                # Get the next layer vertices
                for next_vertex in self.vertices[vertex]:
                    if next_vertex not in vertices:
                        queue.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create empty set
        vertices = set()
        # Create empty Stack
        stack = Stack()

        stack.push(starting_vertex)

        # Iterate all the levels and identify the vertices
        while stack.size() > 0:
            vertex = stack.pop()

            # Check if node visited
            if vertex not in vertices:
                print(vertex)
                vertices.add(vertex)

                for next_vertex in self.vertices[vertex]:
                    if next_vertex not in vertices:
                        stack.push(next_vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        vertices = set()

        def recursive_call(starting_vertex):
            """
            Handles the recursive call
            """
            nonlocal vertices

            # Base case
            if starting_vertex in vertices:
                return

            print(starting_vertex)
            vertices.add(starting_vertex)

            # Iterate thorough the neighbouring vertices
            for vertex in self.vertices[starting_vertex]:
                if vertex not in vertices:
                    recursive_call(vertex)

        recursive_call(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pdb.set_trace()
        # Create an empty set
        vertices = set()
        # Create and empty Queue
        queue = Queue()

        # Create initial path and push to queue
        initial_path = [starting_vertex]
        queue.enqueue(initial_path)

        while queue.size() > 0:
            # Get the path and new vertex information from queue.
            path = queue.dequeue()
            vertex = path[-1]

            # If current vertex is same as destination vertex, return path
            if vertex == destination_vertex:
                return path

            if vertex not in vertices:
                vertices.add(vertex)

                for next_vertex in self.vertices[vertex]:
                    if next_vertex not in vertices:
                        # Here copy is important else the initial
                        # path shall be updated incorrectly
                        new_path = path.copy()
                        new_path.append(next_vertex)
                        queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty set
        vertices = set()
        # Create an empty Stack
        stack = Stack()

        # Add the starting path to Stack
        initial_path = [starting_vertex]
        stack.push(initial_path)

        while stack.size() > 0:

            path = stack.pop()
            vertex = path[-1]

            # If vertex matches the destination vertex
            # return path
            if vertex == destination_vertex:
                return path

            if vertex not in vertices:
                vertices.add(vertex)

                # Find new paths and push to stack.
                for next_vertex in self.vertices[vertex]:
                    if next_vertex not in vertices:
                        new_path = path.copy()
                        new_path.append(next_vertex)

                        stack.push(new_path)


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
    print("Graph Creation")
    valid_str = '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(valid_str)
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\nDepth First Search")
    valid_str = '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(valid_str)
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
    print("\nBreadth First Search")
    valid_str = '''
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
    print(valid_str)
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('\n Depth First Search Recursive')
    valid_str = '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(valid_str)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\nBreadth First Search")
    valid_str = '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(valid_str)
    print(graph.bfs(1, 6))
    print(graph.bfs(7, 3))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("\n Depth First Search")
    valid_str = '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(valid_str)
    print(graph.dfs(1, 6))
    print(graph.dfs(1, 3))
