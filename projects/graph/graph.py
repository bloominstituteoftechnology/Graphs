"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
         #Add a vertex to the graph.
        self.vertices[vertex]=set()
        
    def add_edge(self, v1, v2):
        #Add a directed edge to the graph.
        if v1 not in self.vertices:
            self.vertices.add_vertex(v1)
        if v2 not in self.vertices:
            self.vertices.add_vertex(v2)   
        self.vertices[v1].add(v2)
    
    def bft(self, starting_vertex):
        """Print each vertex in breadth-first order
        beginning from starting_vertex.        """
        # Make a queue -  - 
        queue = Queue()
        #Make a visited set
        visited = set()
        # Make a path
        path = []
        #put starting vertex in the queue
        queue.enqueue(starting_vertex)   # []
        # while queue is not empty - dequeue the item, it is our current item
        while queue.size():
            node = queue.dequeue()
            path.append(node)
        # Mark current as visited - for each of the dequeued item's edges
            visited.add(node)
            # for each of the dequeued item's edges.
            for edge in self.vertices[node]:
                if edge not in visited:
                    # Put them in the queue
                    queue.enqueue(edge)
        print("BFT", path)
    
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Make a stack - Make a visited set
        stack = Stack()
        visited = set()
        path= []
        # Put starting vertext in our stack - while the stack isn't empty
        stack.push(starting_vertex)
        # POp off the top of the stack, it is our current item
        while stack.size():
            node = stack.pop()
            path.append(node)
        #Mark it as visited
            visited.add(node)
        #for each of our current item's edges - if not visited
            for edge in self.vertices[node]:
                if edge not in visited:
                    # print(edge)
                    visited.add(edge)  # remember this one
                    stack.push(edge)
        #put them on the stack.
        print("DFT", path)
        
    def dft_recursive(self, node, visited=set()):
        """Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion. """             
        if node in visited:
           print(visited)
           return visited
        else:
           visited.add(node)
           for neighbor in self.vertices[node]:
               return self.dft_recursive(neighbor,visited)

    def bfs(self, starting_vertex, destination_vertex):
        """Return a list containing the shortest path from
           starting_vertex to destination_vertex in
           breath-first order."""
        # Make a queue.
        queue = Queue()
        # Make a visited set.
        visited = set()
        # Enqueue the path to the node.
        queue.enqueue([starting_vertex])
        # While the queue isn't empty:
        while queue.size() > 0:
            ## dequeue and this is our current item
            path = queue.dequeue()   # --> [starting_vertex]  [2]
            ## the last item in the path is our current item            
            node = path[-1]    # --> Starting_vertex 2
            # if the node not visited
            if node not in visited:
                # Check if it is the target item - if yes --> return path
                if node == destination_vertex:
                    return path
                # For each node connections
                else:
                    visited.add(node)
                    for connection in self.vertices[node]:
                        # copy the path
                        copy_path = path[:]
                        copy_path.append(connection)
                        # enqueue the path copy
                        queue.enqueue(copy_path)    
                     
                

        pass  # TODO

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Make a stack
        stack = Stack()
        # Make a visited 
        visited = set()
        # Add starting_vertex to the stack
        stack.push([starting_vertex])
        # while stack is not empty
        while stack.size():
            # pop the top item in the stack
            path = stack.pop()
            # grab the item not the array/list
            node = path[-1]
            # As long as node is not in the visited
            if node is not visited:
                # check it the node is our ending_vertex then return path
                if node == destination_vertex:
                    return path
                else:
                    visited.add(node)
                    # for every connection in the node
                    for connection in self.vertices[node]:
                        # copy the path
                        copy_path = path[:]
                        # push new connection to the copied path
                        copy_path.append(connection)
                        # add this new copied path the stack
                        stack.push(copy_path)

       

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/BloomInstituteOfTechnology/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
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
    graph.dft_recursive(1

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''

    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

