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
        #If they are both in the graph
        # print(v1)
        # print(v2)
        # print(self.vertices)
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in graph')

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
        q = Queue()
        q.enqueue(starting_vertex)

        #Keep track of the visiting nodes
        visited = set()

        #Keep going until the queue is empty
        while q.size() > 0:
            #Dequeue first vert
            #print(q.queue)
            v = q.dequeue()

            #If it's not visited
            if v not in visited:
                print(v)
            #Mark visited
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #dft uses stack
        #Starting at first vertex, 
        s = Stack()
        visited = set()
        #First ask if the vertex has neighbors
        s.push(starting_vertex)
        #Start traversing the graph using a while loop
        while s.size() > 0:
            #Pop the first vertex
            #print(visited)
            v = s.pop()
        #if v is not visited, print v
            if v not in visited:
                print(v)
                visited.add(v)
                
        #if v is visited, place in the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #If visited is none, we're going initialize it to equal set
        if visited is None:
            visited = set()
        #If the vertex has not been visited, print vertex and add to visited
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
        #For each neighbor, we want to pass the neighbor into dft_recursive
            sv = starting_vertex
            for next_vert in self.get_neighbors(sv):
                self.dft_recursive(next_vert, visited)
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
       
        #Keep track of the visiting nodes
        visited = set()

        #Keep going until the queue is empty
        while q.size() > 0:
            #Dequeue first vert
            #print(q.queue)
            path = q.dequeue()
            v = path[-1]
            #If it's not visited
            if v not in visited:
                
            #Mark visited
                visited.add(v)
                if v == destination_vertex:
                    return path
                for next_vert in self.get_neighbors(v):
                    new_path = path.copy()
                    new_path.append(next_vert)
                    q.enqueue(new_path)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #dft uses stack
        #Starting at first vertex,
        s = Stack()
        visited = set()
        #First ask if the vertex has neighbors
        s.push([starting_vertex])
        #Start traversing the graph using a while loop
        while s.size() > 0:
            #Pop the first vertex
            #print(visited)
            path = s.pop()
            v = path[-1]
        #if v is not visited, print v
            if v not in visited:
                visited.add(v)
                if v == destination_vertex:
                    return path
                for next_vert in self.get_neighbors(v):
                    new_path = path.copy()
                    new_path.append(next_vert)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #If visited is none, we're going initialize it to equal set
        if visited is None:
            visited = set()
        if path is None:
            path = []
        path = path + [starting_vertex]
        #If the vertex has not been visited, print vertex and add to visited
        if starting_vertex not in visited:
            
            visited.add(starting_vertex)
        #For each neighbor, we want to pass the neighbor into dft_recursive
            sv = starting_vertex
            if sv == destination_vertex:
                return path

            for next_vert in self.get_neighbors(sv):
                new_path = self.dfs_recursive(
                    next_vert, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
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
