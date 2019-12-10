"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.recursiveVisited = set()
        self.recursiveVisited2 = set()
        self.path = list()

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
            raise IndexError("That vertex does not exist")

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
        # Create empty queue and enque the starting vertex ID
        # Create empty set to store visited Vertices
        # while queue is not empty, 
            # Dequeue first vertex
            # if that vertex has not been visited
                #Markt it as vissited, then add all of its 
                # # neighbors to the back of the queue
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for i in self.vertices[v]:
                    q.enqueue(i)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for i in self.vertices[v]:
                    #print("I is ", i)
                    s.push(i)
        

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #visited = set()
        # Visited needs to be outside the function, else it'll be brand new every time its invoked
        if starting_vertex not in self.recursiveVisited:
            print(starting_vertex)
            self.recursiveVisited.add(starting_vertex)
            for i in self.vertices[starting_vertex]:
                self.dft_recursive(i)


    def bfs(self, starting_vertex, destination_vertex):
        """ 
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)
        visited = set()
        while q.size() > 0:
            nextPath = q.dequeue()
            lastNode = nextPath[-1]
            if lastNode not in visited:
                if lastNode == destination_vertex:
                    return nextPath
                visited.add(lastNode)
                
                for i in self.vertices[lastNode]:
                    newPath = list(nextPath)
                    newPath.append(i)
                    q.enqueue(newPath)

        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        path = [starting_vertex]
        s.push(path)
        visited = set()
        while s.size() > 0:
            nextPath = s.pop()
            lastNode = nextPath[-1]
            if lastNode not in visited:
                if lastNode == destination_vertex:
                    #print("dfs path found")
                    return nextPath
                visited.add(lastNode)
                
                for i in self.vertices[lastNode]:
                    newPath = list(nextPath)
                    newPath.append(i)
                    s.push(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        self.recursiveVisited2.add(starting_vertex)
        #print("Visited: ", self.recursiveVisited2)
        self.path.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return
        
        for i in self.vertices[starting_vertex]:
            if i not in self.recursiveVisited2:
                self.dfs_recursive(i, destination_vertex)
                #print("path is: ", self.path)
                #print("i is ", i)
        return self.path
    
    # def DFS(g, v, goal, explored, path_so_far):
    # """ Returns path from v to goal in g as a string (Hack) """
    # explored.add(v)
    # if v == goal: 
    #     return path_so_far + v
    # for w in g[v]:
    #     if w not in explored:
    #         p = DFS(g, w, goal, explored, path_so_far + v)
    #         if p: 
    #             return p
    # return ""
                


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
    print("bft solution: ")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft solution: ")
    graph.dft(1)
    print("dft recursive solution: ")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bfs path is: ")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Normal dfs solution: ")
    print(graph.dfs(1, 6))
    print("dfs recursive solution: ")
    print(graph.dfs_recursive(1, 6))
