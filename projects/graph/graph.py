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
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
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
        # create empty queue
        q= Queue()
        #enqueue starting vertex
        q.enqueue(starting_vertex)
        #create empty set to track visisted
        visited = set()
    
        #while queue is not empty:
        while q.size() != 0:
            #get current vertex (dequeeu from queue)
            current = q.dequeue()
            # print current vertex
            if current not in visited:
                print(current)
                visited.add(current)
            else:
                q.dequeue()
            #mark current vertex as visited
                #add vertex to visited_set
            # queue up all current vertex's neighbor
            next_set = self.vertices[current]
            for i in next_set:
                if i not in visited:
                    q.enqueue(i)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack
        s= Stack()
        #enqueue starting vertex
        s.push(starting_vertex)
        #create empty set to track visisted
        visited = set()
    
        #while stack is not empty:
        while s.size() != 0:
            #get current vertex (pop from stack)
            current = s.pop()
            # print current vertex
            if current not in visited:
                print(current)
                visited.add(current)
            else:
                s.pop()
            #mark current vertex as visited
                #add vertex to visited_set
            # push up all current vertex's neighbor
            next_set = self.vertices[current]
            for i in next_set:
                if i not in visited:
                    s.push(i)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        
        if starting_vertex in visited:
            return

        print(starting_vertex)
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            self.dft_recursive(neighbor, visited)
        
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create empty queue
        q= Queue()
        #enqueue PATH to starting vertex

        q.enqueue([starting_vertex])
        # path = q.dequeue()
        #create empty set to track visisted
        visited = set()
        #while queue is not empty:
        while q.size() != 0:
#           #get current vertex PATH
            path = q.dequeue()
            # set current vertex to the LAST element of PATH
            current_vertex = path[-1]

            #check if current vertex has not been visited:
            if current_vertex not in visited:
                #check if current vertex is destination
                #if it is, stop and return
                if current_vertex == destination_vertex:
                    return path
                else:
                    visited.add(current_vertex)
                #mark the current vertex as visited
                #add current vertex to visited
                visited.add(current_vertex)
            #queue up new paths with each neighbor
            neighbors = self.get_neighbors(current_vertex)
            for i in neighbors:
                new_path = list(path)
                # q.enqueue(new_path)
                new_path.append(i)
                q.enqueue(new_path)
                # q.enqueue(new_path)
                #take current path
                #append the neighbor to it
                #queue up new path
                

        return path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # create empty stack
        s= Stack()
        #enqueue PATH to starting vertex

        s.push([starting_vertex])
        # path = q.dequeue()
        #create empty set to track visisted
        visited = set()
        #while queue is not empty:
        while s.size() != 0:
#           #get current vertex PATH
            path = s.pop()
            # set current vertex to the LAST element of PATH
            current_vertex = path[-1]

            #check if current vertex has not been visited:
            if current_vertex not in visited:
                #check if current vertex is destination
                #if it is, stop and return
                if current_vertex == destination_vertex:
                    return path
                else:
                    visited.add(current_vertex)
                #mark the current vertex as visited
                #add current vertex to visited
                visited.add(current_vertex)
            #queue up new paths with each neighbor
            neighbors = self.get_neighbors(current_vertex)
            for i in neighbors:
                new_path = list(path)
                # q.enqueue(new_path)
                new_path.append(i)
                s.push(new_path)
                # q.enqueue(new_path)
                #take current path
                #append the neighbor to it
                #queue up new path

    def dfs_recursive(self, starting_vertex, destination_vertex, visited= None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        
        if path is None:
            path = [starting_vertex]
        
        if starting_vertex in visited:
            return
        
        if path[-1] is destination_vertex:
            return path
        
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            new_path = list(path)
            new_path.append(neighbor)
            returned_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
        
        if returned_path is not None:
            return returned_path
        

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
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
