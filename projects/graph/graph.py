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
        # pass  # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1]. add(v2)
        else:
            raise IndexError('Vertex is non-existent')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        for_visited = Queue() # created a visited queue and added to the starting vertex
        for_visited.enqueue(starting_vertex)
        visited_vertices = set() # created a set for visiting verticies
        while for_visited.size() > 0: # visited is not empty
            current_vertex = for_visited.dequeue() # dequeue the first vertex on the queue
            if current_vertex not in visited_vertices: # if it has not been visited
                print(current_vertex) 
                visited_vertices.add(current_vertex) # mark a visited then added to visited_vertices
                for neighbor in self.get_neighbors(current_vertex): # added all unvisited neighbors to the queue
                    if neighbor not in visited_vertices:
                        for_visited.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        for_visited = Stack() # created a visited stack and added to the starting vertex 
        for_visited.push(starting_vertex)
        visited_vertices = set() # created a set for visiting verticies
        while for_visited.size() > 0: # visited not empty 
            current_vertex = for_visited.pop() # pop the first vertex on for_visited 
            if current_vertex not in visited_vertices: # if it has not been visited 
                print(current_vertex)
                visited_vertices.add(current_vertex) # mark as visited then added to visited_vertices
                for neighbor in self.get_neighbors(current_vertex): # added all unvisited neighbors to the stack 
                    if neighbor not in visited_vertices:
                        for_visited.push(neighbor)

    def dft_recursive(self, starting_vertex, visited_vertices=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass  # TODO
        if visited_vertices is None:# check if visited is none
            visited_vertices = set()# if visited vertices is none change to set
        visited_vertices.add(starting_vertex)# added starting vertex to visited vertices
        print(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)# get the neighbors from the starting vertex
        while len(neighbors) > 0:# check if there are neighbors in the neighbors var
            for neighbor in neighbors:# for each of the neighbors
                if neighbor not in visited_vertices: # if the neighbor is not in the visited vertices 
                    self.dft_recursive(neighbor, visited_vertices)# run the dft_recur function again/ this time with neighbor as the starting vertex, and visited_vertices as the visited 
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO
        path = Queue() # created and empty queue and enqueue a path to the starting vertex
        path.enqueue([starting_vertex])
        visited_vertices = set() # created a set for visited vertices
        while path.size() > 0: # queue is not empty
            current_path = path.dequeue()# dequeue the first Path
            current_path_prev_vertex = current_path[-1]
            if current_path_prev_vertex not in visited_vertices:# if it has not been visited
                if current_path_prev_vertex == destination_vertex:# check if its the target
                    return current_path# return the path if it is
                else:# mark it as visited if it is not
                    visited_vertices.add(current_path_prev_vertex)
                    neighbors = self.get_neighbors(current_path_prev_vertex)
                    for neighbor in neighbors:  # make new versions of the the current path with each neighbor added to them
                        current_path_copy = current_path[:]# duplicate the path
                        current_path_copy.append(neighbor)# add the neighbor
                        path.enqueue(current_path_copy)# add the new path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
        path = Stack()#created empty stack
        path.push([starting_vertex])#path to start vertex
        visited_vertices = set()#set for visited vetices
        while path.size() > 0:#path is not empty
            current_path = path.pop()#pop the first path
            current_path_prev_vertex = current_path[-1]#take last vertex in path
            if current_path_prev_vertex not in visited_vertices:#if we have not been there yet
                if current_path_prev_vertex == destination_vertex:#check if the current is in the destination 
                    return current_path#return the path if it is
                else:#mark as visited if it is not 
                    visited_vertices.add(current_path_prev_vertex)#get the neighbors and make a new path
                    neighbors = self.get_neighbors(current_path_prev_vertex)
                    for neighbor in neighbors:#duplicate the path
                        current_path_copy = current_path[:]# add the neighbor
                        current_path_copy.append(neighbor)# add the new path
                        path.push(current_path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=Stack(), visited_vertices=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # pass  # TODO
        visited_vertices = set()#create a set for visited_vertices
        current_path = path.pop()#create a path to begin search 
        if current_path == None:
            current_path = [starting_vertex]#making sure the current path included the starting vertex
        if current_path[-1] not in visited_vertices:#checking if the last item in stack is not in the visited vertices
            visited_vertices.add(current_path[-1])# added the last item to visited vertices
            for neighbor in self.get_neighbors(current_path[-1]):# getting neighbors for the last item
                if neighbor == destination_vertex:#if neighbor is the desitination vertex end this 
                    current_path.append(neighbor)#append neighbor to path
                    return current_path#return the current path
                current_path_copy = current_path.copy()#create a copy of the current path to make a new path
                current_path_copy.append(neighbor)#adding neighbor to new path
                path.push(current_path_copy)#push the new path to the master path
            return self.dfs_recursive(starting_vertex, destination_vertex, path, visited_vertices)# re run the function

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
