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

        # Add starting vertex ID
        q.enqueue(starting_vertex)

        # Create set for visited verts
        visited = set()

        # While queue is not empty
        while q.size() > 0:

            # Dequeue a vert
            v = q.dequeue()

            # If not visited
            if v not in visited:

                # Visit it!
                print(v)

                # Marked as visited
                visited.add(v)

                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a new stack
        s = Stack()

        # Push stores a value in a stack
        s.push(starting_vertex)

        # Create a set for visited verts
        visited = set()

        # While the stack isn't empty
        while s.size() > 0:

            # pop off whatever is on top, this is the current vert
            v = s.pop()

            # if not visited
            if v not in visited:

                # visit it
                print(v)

                # Mark as visited
                visited.add(v)

                # Push the neighbor to the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
            

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # If the vertex we visited is None
        if visited is None:
            # We can make a set
            visited = set()
        
        # Add it to our visited list
        visited.add(starting_vertex)
        
        # Print it out
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
        # Create an empty queue
        q = Queue()

        # Add starting vertex ID
        q.enqueue([starting_vertex])

        # Create a set for visited verts
        visited = set()

        # While the queue isn't empty
        while q.size() > 0:
            
            # We have to dequeue the first path
            v = q.dequeue()

            # This grabs the last vertex from the path
            n = v[-1]

            # If the last vertex has not been visited then execute this
            if n not in visited:
                # if the last vertex is equal to our destination vertex
                if n == destination_vertex:
                    # Return the path
                    return v
                
                # Mark it as visited
                visited.add(n)

                # Add a path to it's neighbors to the back of the queue
                for neighbor in self.vertices[n]:
                    # Make a copy of the path
                    new = v.copy()
                    # Append the neighbor to theb back
                    new.append(neighbor)
                    q.enqueue(new)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a new stack
        s = Stack()

        # Push stores a value in a stack
        s.push(starting_vertex)

        # Create a set for visited verts
        visited = set()

        # While the stack isn't empty
        while s.size() > 0:

            # pop off whatever is on top, this is the current vert
            v = s.pop()

            # Mark as visited
            visited.add(v)

            # Push the neighbor to the stack
            for neighbor in self.get_neighbors(v):
                if neighbor not in visited:
                    s.push(neighbor)
                if neighbor is destination_vertex:
                    visited.add(neighbor)
                    return list(visited)


    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Mark our vertex as visited
        visited.add(starting_vertex)

        # if the length of our path is equal to 0
        if len(path) == 0:
            # we append our vertex
            path.append(starting_vertex)

        # If the vertex is the target vertex, then we return it
        if starting_vertex == destination_vertex:
            return path

        # We'll check if each neighbor has been visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:

                # If it hasn't, then we'll perform recursion with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)

                # if the recursion returns a path
                if result is not None:
                    
                    # We return it
                    return result

        

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
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
