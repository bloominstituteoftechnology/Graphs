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
        if vertex_id not in self.vertices: # check if vertex exists
            self.vertices[vertex_id] = set() # add vertex

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v2 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) # add v1 neighbor -> v2
        else:
            raise IndexError("Vertex does not exist")

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
        # create an empty queue
        q = Queue()
        # add starting vertex ID
        q.enqueue(starting_vertex)
        # create set for visited verts
        visited = set()
        # while queue is not empty
        while q.size() > 0:
            # dequeue a vert
            v = q.dequeue()
            
            # if not visited
            if v not in visited:
                # visit it!
                print(v)
                # mark as visited
                visited.add(v)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # creat an empty stack
        s = Stack()
        # add starting vertex id
        s.push(starting_vertex)
        # create set for visited verts
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop a vert
            v = s.pop()

            # if not visited
            if v not in visited:
                # visit it
                print(v)
                # mark as visited
                visited.add(v)
                # add all neighbors to the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        v = starting_vertex
        # if visited is None, init with set
        if visited is None:
            visited = set()
        
        # if vert has not been visited
        if v not in visited:
            # print it
            print(v)
            # mark as visited
            visited.add(v)

            # get vert neighbors
            neighbors = self.get_neighbors(v)

            # iterate through the neighbors
            for neighbor in neighbors:
                # and recurse for neighbors
                if neighbor not in visited:
                    self.dft_recursive(neighbor,visited)
        else:
            return # all verts have been visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # init visited as set
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited
            if last_vert not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                else:
                    # Mark as visited
                    visited.add(last_vert)
                    # Then add A PATH TO its neighbors to the back of the queue
                    for edge in self.get_neighbors(last_vert):
                        # copy path
                        path_copy = list(path)
                        # append neighbor to th back
                        path_copy.append(edge)
                        q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited
            if last_vert not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                else:
                    # Mark as visited
                    visited.add(last_vert)
                    # Then add A PATH TO its neighbors to the back of the stack
                    for edge in self.get_neighbors(last_vert):
                        # COPY THE PATH
                        path_copy = list(path)
                        # APPEND THE NEIGHOR TO THE BACK
                        path_copy.append(edge)
                        s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = []
        temp_path = path.copy()
        temp_path.append(starting_vertex)
        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            if starting_vertex == destination_vertex:
                return temp_path
            else:
                for neighbor in self.get_neighbors(starting_vertex):
                    next_path = self.dfs_recursive(
                        neighbor, destination_vertex, visited)
                    if next_path is not None:
                        return next_path

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
