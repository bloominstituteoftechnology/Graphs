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
        # pass  # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That aint there")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        # Create empty queue
        # Create empty set to store visited verticies
        # while the queue is not empty...
            # dequeue the first vertex
            # if that vertex has not been visited...
            # then add all of its neightbors to the back of the queue

        q = Queue()
        q.enqueue(starting_vertex)

        #Create an empty set to store visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        s = Stack()
        s.push(starting_vertex)

        # Create a set to store visited vertices
        visited = set()
        
        # while the stack is not empty...
        while s.size() > 0:
            # pop off the first vertex
            v = s.pop()
            # if that vertex has not been visited...
            if v not in visited:
                # mark it as visited..
                print(v)
                visited.add(v)
                # then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass  # TODO
        if visited is None: 
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO
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
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v not in visited:
                if v == destination_vertex:
                    return path
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)
        return None

    def dfs_recursive(self, starting_vertex, targetValue, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # pass  # TODO
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == targetValue:
            return path
        for child_vert in self.get_neighbors(starting_vertex):
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, targetValue, visited, path)
                if new_path: 
                    return new_path


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
    print(f'Vertices: {graph.vertices}')

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
    print('')

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print('')
    graph.dft_recursive(1)
    print('')

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(f'BTS Path: {graph.bfs(1, 6)}')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(f'DFS Path: {graph.dfs(1, 6)}')
    print(graph.dfs_recursive(1, 6))
