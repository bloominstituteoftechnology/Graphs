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
        self.vertices[v1].add(v2)

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
        #Create a Queue
        #Add starting node to search
        #Create set of Visited nodes
        #While Queue is not empty:
            #remove that node
            #check if it's been visited
            #If not:
                #Move to visited
                #Add neighbors to the queue
        #return
        que = Queue()
        que.enqueue(starting_vertex)
        visit = set()
        while que.size() > 0:
            vert = que.dequeue()
            if vert not in visit:
                visit.add(vert)
                for neighbor in self.get_neighbors(vert):
                    que.enqueue(neighbor)
        return visit

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #Create a Stack
        #Add starting node to search
        #Create set of Visited nodes
        #While Stack is not empty:
            #remove that node
            #check if it's been visited
            #If not:
                #Move to visited
                #Add neighbors to the Stack
        #return
        stack = Stack()
        stack.push(starting_vertex)
        visit = set()
        while stack.size() > 0:
            vert = stack.pop()
            if vert not in visit:
                visit.add(vert)
                for neighbor in self.get_neighbors(vert):
                    stack.push(neighbor)
        return visit

    #to keep track of visitied outside of recursive (so doesn't refresh to empty)
    visited = set()
    stack = Stack()
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #if starting vertex not in visited:
        if starting_vertex not in visited:
            #add to visited
            visited.add(starting_vertex)
            #add to stack so not empty
            stack.push(starting_vertex)
        #while visit not empty:
        while stack.size() > 0:
            #assign vert to remove from stack
            vert = stack.pop()
            #if vert not in visit:
            if vert not in visited:
                #add to visit
                visit.add(vert)
                #add neighbors to visit
                for neighbor in self.get_neighbors(vert):
                    stack.push(neighbor)
            #recurse visited and index 0
            dft_recursive(stack.index(0))
        #return visit
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                  # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to the back of the queue
                  # COPY THE PATH
                  # APPEND THE NEIGHOR TO THE BACK
            #return

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO
        # Create an empty stack and add A PATH TO the starting vertex ID
            # Create a Set to store visited vertices
            # While the stack is not empty...
                # remove the first PATH
                # Grab the last vertex from the PATH
                # If that vertex has not been visited...
                    # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN PATH
                    # Mark it as visited...
                    # Then add A PATH TO its neighbors to the back of the stack
                    # COPY THE PATH
                    # APPEND THE NEIGHOR TO THE BACK
            #return

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
    print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft(1))
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))