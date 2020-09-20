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
        # check if vertex in dict:
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        else:
            print('Duplicate! Vertex not updated!')

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if v1 in graph
        if v1 in self.vertices:
            # check if v2 in graph
            if v2 in self.vertices:
                self.vertices[v1].add(v2)      
        else:
            return 'One or more vertices not found!'       
        
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # check if vertex in graph
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return set()

    # default function to use in traversals 
    def print_path(vertex):
        print(str(vertex))

    # adding func to allow for variation in operation application
    def bft(self, starting_vertex, func = print_path):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = Queue()

        # check if starting vertex in graph and add to begin traversal
        if starting_vertex in self.vertices:
            queue.enqueue(starting_vertex)
        else:
            return 'Starting vertex not found!'

        while queue.size() > 0:
            vertex = queue.dequeue()
            
            # check if current vertex has been visited
            if vertex not in visited:

                # get all vertices to be visted next added to queue
                for neighbor in self.get_neighbors(vertex):
                    queue.enqueue(neighbor)
                
                # perform function operation on current vertex
                func(vertex)

            # add current vertex to visited set avoid collisions with neighboring edges
            visited.add(vertex)
            

    
    # adding func to allow for variation in operation application
    def dft(self, starting_vertex, func = print_path):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()

        # check if starting vertex in graph and add to begin traversal
        if starting_vertex in self.vertices:
            stack.push(starting_vertex)
        else:
            return 'Starting vertex not found!'

        while stack.size() > 0:
            vertex = stack.pop()
            
            # check if current vertex has been visited
            if vertex not in visited:

                # get all vertices to be visted next added to queue
                for neighbor in self.get_neighbors(vertex):
                    stack.push(neighbor)
                
                # perform function operation on current vertex
                func(vertex)

            # add current vertex to visited set avoid collisions with neighboring edges
            visited.add(vertex)
        

    # adding func to allow for variation in operation application
    def dft_recursive(self, starting_vertex, func = print_path, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check starting vertex is valid
        if starting_vertex not in self.vertices:
            return f'Staring vertex {starting_vertex} not found!'

        # perform func on starting vertex if first pass
        if len(visited) < 1:
            func(starting_vertex)
            
        # add current vetex to visited each recursion
        visited.add(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                func(neighbor)
                self.dft_recursive(neighbor, visited= visited)

        
    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = Queue()

        # add current vertex to queue
        if starting_vertex in self.vertices:
            queue.enqueue([starting_vertex])

        while queue.size() > 0:
            curr_path = queue.dequeue()
            curr_vert = curr_path[-1]

            # check if found
            if curr_vert == destination_vertex:
                return curr_path

            # traverse unvisited neighbors
            for neighbor in self.get_neighbors(curr_vert):
                if neighbor not in visited:
                    new_path = list(curr_path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

            visited.add(curr_vert)

        return None



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = Stack()

        # add current vertex to stack
        if starting_vertex in self.vertices:
            stack.push([starting_vertex])

        while stack.size() > 0:
            curr_path = stack.pop()
            curr_vert = curr_path[-1]

            # check if found
            if curr_vert == destination_vertex:
                return curr_path

            # traverse unvisited neighbors
            for neighbor in self.get_neighbors(curr_vert):
                if neighbor not in visited:
                    new_path = list(curr_path)
                    new_path.append(neighbor)
                    stack.push(new_path)

            visited.add(curr_vert)


        return None
        

    def dfs_recursive(self, starting_vertex, destination_vertex,
                    curr_path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # check if in graph
        if starting_vertex not in self.vertices:
            return None

        # if first run, add starting vertex to path
        if len(curr_path) < 1: 
            curr_path.append(starting_vertex)

        # add current vert to visited
        visited.add(starting_vertex)
        
        # base case is vertex found:
        if starting_vertex == destination_vertex:
            return curr_path 

        # use recusrive stack to traverse
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = list(curr_path)
                new_path.append(neighbor)
                res = self.dfs_recursive(neighbor, destination_vertex,
                                        new_path, visited)
                if len(res) > 0:
                    return res
        return []

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
