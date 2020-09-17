"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque
from queue import Queue 
from queue import LifoQueue 

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # this is the vertices dictionary

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # add the vertex to the dictionary and the value will be a set 
        # that at the start is empty
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # to add an edge we will get the vertex out of the dictionary
        # we will then check put the neighbor in the set of the vertex
        # need to check that both of the vertices are in the dictionary
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception("At least one of the vertices has not been added to the graph")
        else:
            self.vertices[v1].add(v2)



    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        This function will return a set
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id] # this will return a set
        else:
            return set()

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        
        # This will implement a queue (like a line)
        # will first put the starting vertex into the queue
        myQueue = Queue()
        visited = set() # This will contain the 
        # first will check to see if the starting vertex is in the graph
        if starting_vertex in self.vertices:
            myQueue.put(starting_vertex)
        else:
            raise Exception("The following vertex is not in the graph")
        # will now go through the breadth first traversal
        # first will deque from the queue
        while myQueue.qsize() >= 1: # While there is something to get out of the queue
            node = myQueue.get()
            # printing the node when visiting it
            # if the node dequeued is not in the visited set then will print it and then put it 
            # in the visited set and then will add all the neighbors of the node it not been visited
            if node not in visited:
                print(node)
                visited.add(node)
                for val in self.get_neighbors(node): # looping through the neighbors
                    myQueue.put(val)
            
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        # this means that we will go down the depth of the 
        # graph 
        # will implement a stack instead of a queue
        myStack = LifoQueue()
        # making the set that shows what has been visited
        visited = set()
        # checking to see if the starting vertex is in the graph
        if starting_vertex not in self.vertices:
            raise Exception("Vertex not found in the graph")
        else:
            # will put the staring vertex into the stack
            myStack.put(starting_vertex)
        # now doing the while loop
        while myStack.qsize() >= 1: # will go if there is something to pop from the stack
            # popping from the stack
            node = myStack.get()
            if node not in visited:
                # now we need to print it and then add it to the visited set and then
                # add its neighbors to the stack
                print(node)
                visited.add(node)
                for val in self.get_neighbors(node):
                    myStack.put(val)




        
    def dft_recur_inner(self, visited, node):

        if node == None or node in visited:
            return
        else:
            # will print the node
            # will add the node to the visited list 
            # will then loop through the neighbors of the node recursively
            print(node)
            visited.add(node)
            for val in self.get_neighbors(node):
                self.dft_recur_inner(visited, val)
            return




    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        # will cause this to call an inner function called dft_recur_inner 
        # setting up the set 
        visited = set()
        self.dft_recur_inner(visited, starting_vertex)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #print("ding bfs") just used to show when the method was called
        # will have the elements in the stack be the current path ie a list

        myQueue = Queue()
        visited = set()
        newPath = None

        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            raise Exception("This vertex is not in the graph")
        # adding the first begining path
        myQueue.put([starting_vertex])

        # now doing the loopig and dequeing of the queue and then will go further  along 
        # a path
        while myQueue.qsize() >= 1:
            # will pop the path off of the queue
            path = myQueue.get()
            curNode = path[-1]
            # checking to see if the curent not is the one that we need to end on
            if curNode == destination_vertex:
                return path
            # need to check to see if the last element has not been visited
            if curNode not in visited:
                # will put it in the visited 
                # get all of its neighbors and make new lists (paths ) and then append the neighbor
                visited.add(curNode)

                for val in self.get_neighbors(curNode):
                    newPath = path[:]
                    newPath.append(val)
                    # will put the path back into the queueu
                    myQueue.put(newPath)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        #print("doing dfs") # used to show when the method was called
        # doing te dfs means that we will keep going down a path till we hit the end of the path
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            raise Exception("One of the verices is not in the graph")
        # implementing the stack
        myStack = LifoQueue()
        visited = set()
        newPath = None
        # putting the path that begings with the starting destination into the stack
        myStack.put([starting_vertex])

        # will now go and do the looping in the while loop
        while myStack.qsize() >= 1:
            # popping off of the stack
            path = myStack.get()
            # now getting the last element of the path
            curNode = path[-1]
            # will check to see if the curNode is in the visited set
            if curNode not in visited:
                
                # check to see if the curNode is the destination
                if curNode == destination_vertex:
                    return path
                # adding the curNode to the visited set
                visited.add(curNode)
                # adding each of the neighbors to the path
                for val in self.get_neighbors(curNode):
                    newPath = path[:]
                    newPath.append(val)
                    # putting each path into the stack
                    myStack.put(newPath)


    def dfs_recurs_inner(self, visited, path, curNode, destination_vertex):
        # base case
        if curNode == destination_vertex:
            return path
        # need to check if the curNode is in the visited set
        if curNode in visited:
            return None
        # need to put the curNode in the set visited
        visited.add(curNode)
        newPath = None
        # doing the looping of the neighbors of the curNode
        for val in self.get_neighbors(curNode):
            newPath = path[:]
            newPath.append(val)
            # making a recursive call
            returnVal = self.dfs_recurs_inner(visited, newPath, val, destination_vertex) 
            if returnVal:
                return returnVal   
        return []


        
    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #print("doing dfs_recurs")
        # checking to see if the starting vertex or the destination vertex are in the graph
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            raise Exception("One of the vertices is not in the graph")
        # This is the wrappeer function to the inner recursive funtion
        visited = set()
        path = [] # This is what will be returned from this function
        # addig the first node to the path
        path.append(starting_vertex)

        return self.dfs_recurs_inner(visited , path, starting_vertex, destination_vertex)



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
