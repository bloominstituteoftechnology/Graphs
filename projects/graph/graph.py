"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        # Add a vertex to the graph.
        self.vertices[vertex] = set()
        #Vertices will have set inside like dictionary
        
    def add_edge(self, v1, v2):
        # Add a directed edge to the graph.
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex doesn't exist!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create empty set
        vertices = set()
        
        #create empty queue
        queue = Queue()
        
        queue.enqueue(starting_vertex)
        
        #we iterate each level and grab the next level of vertices
        while queue.size() > 0:
            vertex = queue.dequeue()
            
            #check and update the set
            if vertex not in vertices:
                print(vertex)
                vertices.add(vertex)
                
                #now get the next vertices
                for next_vertex in self.vertices[vertex]:
                    if next_vertex not in vertices:
                        queue.enqueue(next_vertex)
        
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create empty set
        vertices = set()
        # Create empty Stack
        stack = Stack()

        stack.push(starting_vertex)

        # Iterate all the levels and identify the vertices
        while stack.size() > 0:
            vertex = stack.pop()

            # Check if node visited
            if vertex not in vertices:
                print(vertex)
                vertices.add(vertex)

                for next_vertex in self.vertices[vertex]:
                    if next_vertex not in vertices:
                        stack.push(next_vertex)
        
        
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        vertices = set()
        
        def recursive_call(starting_vertex):
            """
            Handles the recursive call
            """
            nonlocal vertices

            # Base case
            if starting_vertex in vertices:
                return

            print(starting_vertex)
            vertices.add(starting_vertex)

            # Iterate thorough the neighbouring vertices
            for vertex in self.vertices[starting_vertex]:
                if vertex not in vertices:
                    recursive_call(vertex)

        recursive_call(starting_vertex)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
         # create an empty queue, add the starting vertex
        if starting_vertex is destination_vertex:
            print("Lol that's funny")
            return starting_vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        print(visited)
        while queue.size() > 0:
            # dequeue the first path
            path = queue.dequeue()
            print(path)
            # we need to grab the last vertex of the path (hint, path is an array)
            vertex = path[-1]
            if vertex == destination_vertex:
                return path
            
            if vertex not in visited:
                visited.add(vertex)
                
            for neighbor in self.vertices[vertex]:
                # create a copy path for each of those neighbors, and then append neighbor to that copy
                path_copy = path.copy()
                path_copy.append(neighbor)
                if neighbor == destination_vertex:

                    return path_copy
                queue.enqueue(path_copy)
                
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty queue, add the starting vertex
        if starting_vertex is destination_vertex:
            print("Lol that's funny")
            return starting_vertex
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        print(visited)
        while stack.size() > 0:
            # dequeue the first path
            path = stack.pop()
            print(path)
            # we need to grab the last vertex of the path (hint, path is an array)
            vertex = path[-1]
            if vertex == destination_vertex:
                return path
            if vertex not in visited:
                visited.add(vertex)
            for neighbor in self.vertices[vertex]:

                # create a copy path for each of those neighbors, and then append neighbor to that copy
                path_copy = path.copy()
                path_copy.append(neighbor)
                if neighbor == destination_vertex:

                    return path_copy
                stack.push(path_copy)





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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
