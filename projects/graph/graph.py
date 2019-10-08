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
        if self.vertices.get(vertex, None) is None:
            self.vertices[vertex] = set()
        else:
            print("Vertex already exists")


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That Vertex does not exist!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty set to store visited nodes
        visited = set()
        res = []
        q = Queue()
        q.enqueue(starting_vertex)
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            vertex = q.dequeue()
            # If vertex not visited
            if vertex not in visited:
                # Mark as visited
                visited.add(vertex)
                res.append(vertex)
                # Add all of its neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    q.enqueue(neighbor)
        print(res)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        res = []
        # Create an empty stack and push the starting vertex
        s = Stack()
        s.push(starting_vertex)

        while s.size() > 0:
            vertex = s.pop()
            #
            if vertex not in visited:
                visited.add(vertex)
                res.append(vertex)
                for neighbor in self.vertices[vertex]:
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        res = []

        def visit(vertex, visited=set()):
            nonlocal res
            if vertex not in visited:
                res.append(vertex)
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    visit(neighbor, visited)

        visit(starting_vertex)
        print(res)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        # Queue will hold a tuple (currentVertex, path)
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            # Split queue into vertex and path
            path = q.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                visited.add(vertex)
                if vertex == destination_vertex:
                    return path
                for neighbor in self.vertices[vertex]:
                    q.enqueue(path + [neighbor])

        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        s = Stack()
        s.push([starting_vertex])

        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path

                visited.add(vertex)

                for neighbor in self.vertices[vertex]:
                    s.push(path + [neighbor])





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
