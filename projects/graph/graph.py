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
            print("Error: vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        q = Queue()
        # enqueue the starting index
        q.enqueue(starting_vertex)
        # create a set to store visited verticies
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first index
            i = q.dequeue()
            # check if its been visited
            # if it hasnt been visited
            if i not in visited:
                print(i)
                visited.add(i)
                # mark it as visited
                # enques all its neighbors
                for neighbor in self.get_neighbors(i):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        s = Stack()
        # push the starting index
        s.push(starting_vertex)
        # create a set to store visited verticies
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first index
            v = s.pop()
            # check if its been visited
            # if it hasnt been visited
            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)
                # push all its neighbors
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex,visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            # call dft recursive on all the neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor,visited)
        

    def bfs(self, starting_vertex, target):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
       # Create a queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue( [starting_vertex] )
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == target:
                    # IF SO, RETURN THE PATH
                    return path
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # ENQUEUE THE COPY
                    q.enqueue(path_copy)

                

                
            

    def dfs(self, starting_vertex, target):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        s = Stack()
        # Push A PATH TO the starting vertex
        s.push( [starting_vertex] )
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == target:
                    # IF SO, RETURN THE PATH
                    return path
                # Enqueue A PATH TO all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # MAKE A COPY OF THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # PUSH THE COPY
                    s.push(path_copy)

    def dfs_recursive(self,starting_vertex,target,visited = None,path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        '''if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(starting_vertex)
        copy = path.copy
        copy.append(starting_vertex)
        if starting_vertex == target:
            return copy
        if starting_vertex not in visited
        for neighbor in self.get_neighbors(starting_vertex):
            new_path = self.dft_recursive(neighbor,target,visited = visited,path = path)
            '''

        if visited is None:
            visited = set()
        if path is None:
            path = []
        # add starting_vertex to visited set
        visited.add(starting_vertex)
        path += [starting_vertex]
        # path =  path + [starting_vertex]
        # if starting vertex == target_vertex:
        # return path
        if starting_vertex == target:
            # print(path)
            return path
         
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor,target,visited = visited,path = path)
                if new_path:
                    return new_path
        # for neighbor in neighbors(starting_vertex):
            # if neighbor not in visited:
                # make a copy of the path
                # new_path = dfs_recursive(neighbor, target_vertex, visited, path)
                # if new_path return new_path
        #return None

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
    #print(graph.vertices)

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
    print("BFT")
    graph.bft(1)
    print()

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT")
    graph.dft(1)
    print()
    print("DFT recursive")
    print(graph.dft_recursive(1))
    

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS")
    print(graph.dfs(1, 6))
    print()
    print("DFS recursive")
    print(graph.dfs_recursive(1, 6))
