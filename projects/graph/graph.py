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
        # Checking if the to two vertices exist
        if v1 in self.vertices:
            # if true then add them
            self.vertices[v1].add(v2)
        else:
            self.vertices[v1] = set([v2])
        if v2 not in self.vertices:
            self.vertices[v2] = set()


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
    #Traversal pseudocode:
    # Create a queue/stack as appropriate
        # Put the starting point in that
        # Make a set to keep track of where we’ve been
        # While there is stuff in the queue/stack
        #    Pop the first item
        #    If not visited
        #       DO THE THING!
        #       Add to visited
        #       For each edge in the item
        #           Add that edge to the queue/stack
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # #Step 1 Create an empty queue
        q = Queue()
        # #Create an empty Set to store visited vertices
        visited_nodes = set()
        # add starting vertex
        q.enqueue(starting_vertex)
        # #While the queue is not empty ...
        while q.size() > 0:
            v = q.dequeue()
        # If that vertex has not been visited
            if v in visited_nodes:
                continue
        # mark it as visisted
            print(v)
            visited_nodes.add(v)
        # Then add all of its neighbors to the back of the queue.
            for vertex in self.vertices[v]:
                q.enqueue(vertex)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push starting vertex Id
        s = Stack()
        s.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        #While the stack is not empty.....
        while s.size() > 0:
            #Pop the first vertex
            v = s.pop()
            # If that vertex has been visited...
            if v not in visited:
                #Mark it as visted...
                print(v)
                visited.add(v)
                #Then add all of its nieghbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)




    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create an empty queue and enqueue a PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
                 #Dequeue the first PATH
            #Grab the last vertex from the PATH
            #If that vertex has not been visited...
                #CHECK IF IT'S THE TARGET
                    #IF SO, RETURN PATH
                #Mark it as visited..
                #Then add a PATH TO its neighbors to the back of the queue
                    #COPY THE PATH
                    #APPEND THE NEIGHBOR TO THE BACK
        # recursion with dft since it forces us to use a stack
        if visited is None:

            visited = set()

        print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                # visited.add(vertex)
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex == destination_vertex:
            return [starting_vertex]
        # #Step 1 Create an empty queue and enqueue a PATH TO the starting vertex ID
        q = Queue()
        q.enqueue( [starting_vertex])
        # #Create an empty Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first Path
            path = q.dequeue()
            # Grab the last vertex from the Path
            v = path[-1]
            # if that vertex has not been visited...
            if v not in visited:
                # check to see if It's the target
                if v == destination_vertex:
                # if so return the path
                    return path
                # mark it as visited
                visited.add(v)

                # then add a Path to its neighbors to the back if the qeueue
                for neighbor in self.get_neighbors(v):
                    # Copy path to avoid pass by reference bug
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)




    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        if starting_vertex == destination_vertex:
            return [starting_vertex]

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
            for neighbor in self.get_neighbors(v):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)






    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Init visited
        if visited is None:

            visited = set()
        # Inint path
        if path is None:
            path=[]
        visited.add(starting_vertex)
        # Add vertex to the path
        path = path + [starting_vertex]
        # If we are at  the target value, return the path
        if starting_vertex == target_vertex:
            return path
        # Otherwise, call DFS_recursive on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                # creating a new path
                new_path = self.dfs_recursive(neighbor, target_vertex, visited, path)
                if new_path is not None:
                    return new_path
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

    print("------------")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''

    print("------------")
    graph.dft(1)
    print("-------------")
    print(graph.dft_recursive(1))

    print("------------")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''

    print("------------")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''

    print("------------")
    print(graph.dfs(1, 6))
    print("------------")
    print(graph.dfs_recursive(1, 6))
