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
            self.vertices[v1].add(v2)
        else:
            raise IndexError("noneexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO
        # return the neighbor after sorted by dictionary
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        # create the empty Queue 
        q = Queue()
        # create the visited dictionary
        visited = set()
        # add all the starting_vertex into the queue
        q.enqueue(starting_vertex)
        # loop through the queuse size if the size bigger than 0 then
        while q.size() > 0:
            # set the variable for vertex to delete or remove from queue
            vertex = q.dequeue()
            # if vertex is not in visited yet 
            if vertex not in visited:
                print(vertex)
                # add the vertex in to visited as already visit
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)
        
           
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        s = Stack()
        visited = set()

        s.push(starting_vertex)
        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass  # TODO
        # return self.dft(starting_vertex)
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
       


       
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        # enqueue A PATH TO the starting vertex ID
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            vertex = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = vertex[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return vertex
                visited.add(last_vertex)
                for neighbor in self.get_neighbors(last_vertex):
                    # next path is the list of new path
                    # COPY THE PATH
                    # next_path = vertex[:] 
                    # # add the neighbor to the new path
                    # next_path.append(neighbor)
                    next_path = vertex + [neighbor]
                    # add the next path to the queue
                    # APPEND THE NEIGHOR TO THE BACK
                    q.enqueue(next_path)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
        # Create an empty Stack and push A PATH TO the starting vertex ID
        s = Stack()
        # push A PATH TO the starting vertex ID
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # while the Stack is not empty
        while s.size() > 0:
            # pop the first path of the stack
            vertex = s.pop()
            # Grab the last vertex from the Path
            last_vertex = vertex[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # check if the vertex is equlal to target
                if last_vertex == destination_vertex:
                    #is yes return the path
                    return vertex
                # mark the vertex as visited.
                visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the back of the queue
				  # COPY THE PATH
				  # APPEND THE NEIGHOR TO THE # Then add A PATH TO its neighbors to the back of the queue
				  # COPY THE PATH
				  # APPEND THE NEIGHOR TO THE BACK
                for neighbor in self.get_neighbors(last_vertex):
                    next_path = vertex[:]
                    next_path.append(neighbor)
                    s.push(next_path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # pass  # TODO
        # check if the starting vertes if not visited yet
        if starting_vertex not in visited:
            # add the starting vertex into visited dicitonary. as visisted.
            visited.add(starting_vertex)
        # check if the starting vertex is in the path ?
        if starting_vertex not in path:
            # if if still empty we store that starting to path as list
            path = [starting_vertex]
        # loop thourgh all neighbor of starting vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # check if not visit that neighbor yet add the visiting neighbor to visited
            if neighbor not in visited:
                # copy the new path of neighbor
                new_path = path +[neighbor]
                # if neighbor equal to desination or target return that new path
                if neighbor == destination_vertex:
                    # return the new path
                    return new_path
                # other wise create the variable that store call back frunction and then
                dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                # check if that the dfs path is not none then we return the the dfs path
                if dfs_path is not None:
                    return dfs_path
        return None
        # return self.dfs(starting_vertex, destination_vertex)
        
       
                
        

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
