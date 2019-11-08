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
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print('Breadth First Traversal')
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an emptySset to store visited vertices 
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex had not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of it's neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        print('\n')

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print('Depth First Traversal')
        # Create an empty stack and enqueue the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create an emptySset to store visited vertices 
        visited = set()
        # While the stck is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex had not been visited...
            if v not in visited:
                # Mark it as 
                print(v)
                visited.add(v)
                # Then add all of it's neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        print('\n')

    
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if not visited:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for v in self.vertices[starting_vertex]:
                self.dft_recursive(v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        initial_path = [starting_vertex]
        q.enqueue(initial_path)
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited...
            if last_vert not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                  # IF SO, RETURN PATH
                  return path
                # Mark it as visited...
                visited.add(last_vert)
                # Then add A PATH TO its neighbors to the back of the 
                for v in self.vertices[last_vert]:
                  # COPY THE PATH
                  path_copy = path[:]
                  # APPEND THE NEIGHOR TO THE BACK
                  path_copy.append(v)
                  q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        initial_path = [starting_vertex]
        s.push(initial_path)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Dequeue the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited...
            if last_vert not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                  # IF SO, RETURN PATH
                  return path
                # Mark it as visited...
                visited.add(last_vert)
                # Then add A PATH TO its neighbors to the back of the 
                for v in self.vertices[last_vert]:
                  # COPY THE PATH
                  path_copy = path[:]
                  # APPEND THE NEIGHOR TO THE BACK
                  path_copy.append(v)
                  s.push(path_copy)





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
    print('Depth First Traversal Recursion')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('Breadth First Search')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('Depth First Search')
    print(graph.dfs(1, 6))
