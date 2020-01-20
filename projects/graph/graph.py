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
        pass  # TODO

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
        if visited is None:
            visited = set([starting_vertex])

        print(starting_vertex)

        for vertex in self.vertices[starting_vertex]:
            if vertex not in visited:
                visited.add(vertex)
                self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        pass



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    # print(graph.dfs_recursive(1, 6))
