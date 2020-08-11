"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

#to keep track of visitied outside of recursive (so doesn't refresh to empty)
visit = set()
stack = Stack()

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
                #visit it! (print)
                #Move to visited
                #Add neighbors to the queue
        que = Queue()
        que.enqueue(starting_vertex)
        visit = set()
        while que.size() > 0:
            vert = que.dequeue()
            if vert not in visit:
                print(vert)
                visit.add(vert)
                for neighbor in self.get_neighbors(vert):
                    que.enqueue(neighbor)

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
                #visit it! (print)
                #Move to visited
                #Add neighbors to the Stack
        stack = Stack()
        stack.push(starting_vertex)
        visit = set()
        while stack.size() > 0:
            vert = stack.pop()
            if vert not in visit:
                print(vert)
                visit.add(vert)
                for neighbor in self.get_neighbors(vert):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visit=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #set visit as param, default to None to doesn't change test
        #if it is None, (is at beginning), reassign to empty set
        #add starting variable to visit
        #print( so it prints the order)
        #for every neightbor, check if neighbor is in visit already
            #if not, recurse with neighbor as starting_vert and current visit
        if visit is None:
            visit = set()
        visit.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visit:
                self.dft_recursive(neighbor, visit)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and add A PATH TO the starting vertex ID
            # Create a Set to store visited vertices
            # While the queue is not empty...
                # remove the first PATH
                # Grab the last vertex from the PATH
                # If that vertex has not been visited...
                    # CHECK IF IT'S THE TARGET
                        # IF SO, RETURN PATH
                    # Mark it as visited...
                    # Then add A PATH TO its neighbors to the back of the queue
                        # COPY THE PATH
                        # APPEND THE NEIGHOR TO THE BACK
        que = Queue()
        visit = set()
        que.enqueue([starting_vertex])
        while que.size() > 0:
            path = que.dequeue()
            vert = path[-1]
            if vert not in visit:
                if vert == destination_vertex:
                        return path
                visit.add(vert)
                for neighbor in self.get_neighbors(vert):
                    newpath = list(path) + [neighbor]
                    que.enqueue(newpath)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
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
        stack = Stack()
        visit = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vert = path[-1]
            if vert not in visit:
                if vert == destination_vertex:
                        return path
                visit.add(vert)
                for neighbor in self.get_neighbors(vert):
                    newpath = list(path) + [neighbor]
                    stack.push(newpath)
         
    def dfs_recursive(self, starting_vertex, destination_vertex, visit=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #set visit and path to params, defualt to None, then reassign
        #add current vertex to visit
        #make a copy of path and reassign it with current vert at end
        #base case
        #if current vert is the destination, return the path
        #if not, check every neighbor
            #if hasn't been visited yet,
                #visit it by recursion--new path is recursion with neighbor as starting vertex
                #return newpath is not None (found something other than None if didn't find the first time)
        # otherwise if can't find desination, return None
        if visit is None:
            visit = set()
        if path is None:
            path = []
        visit.add(starting_vertex)
        path = list(path) #makes a copy
        path.append(starting_vertex) #reassigns
        if starting_vertex == destination_vertex:
            return path
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visit:
                newpath = self.dfs_recursive(neighbor, destination_vertex, visit, path)
                if newpath is not None:
                    return newpath
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
    # print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print(graph.dft(1))
    # print(graph.dft_recursive(1))

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
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))