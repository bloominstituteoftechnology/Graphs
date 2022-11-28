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
        if vertex_id not in self.vertices: #may not even need this line
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
        queue = Queue() #start an empty queue
        queue.enqueue(starting_vertex) #enqueue the starting vertex
        visited = set() #create an empty set to keep track of visited vertices
        while queue.size() > 0:
            #while queue is not empty add vertices to the queue
            current = queue.dequeue()
            if current not in visited:
                print(current)
                visited.add(current)
                for el in self.get_neighbors(current):
                    queue.enqueue(el)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stck = Stack()
        stck.push(starting_vertex)
        visited = set()
        while stck.size() > 0:
            current = stck.pop()
            if current not in visited:
                print(current)
                visited.add(current)
                
                for el in self.get_neighbors(current):
                    stck.push(el)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)
        edges = self.get_neighbors(starting_vertex)

        if len(edges) <= 0:
            return
        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the PATH TO starting_vertex
        q = Queue()
        q.enqueue([starting_vertex])

        # Create an empty set to track visited verticies
        visited = set()
        # while the queue is not empty:
        while q.size() > 0:
            # get current vertex PATH (dequeue from queue)
            current_path = q.dequeue()
            # set the current vertex to the LAST element of the PATH
            current_vertex = current_path[-1]
            # CHECK IF THE CURRENT VERTEX IS DESTINATION
            if current_vertex is destination_vertex:
                # IF IT IS, STOP AND RETURN
                return current_path
            # Check if the current vertex has not been visited:
            if current_vertex not in visited:
                visited.add(current_vertex)

                edges = self.get_neighbors(current_vertex)

                for edge in edges:
                    clone = list(current_path)
                    clone.append(edge)
                    q.enqueue(clone)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            current_path = s.pop()

            current_vertex = current_path[-1]

            if current_vertex is destination_vertex:
                return current_path

            if current_vertex not in visited:
                visited.add(current_vertex)

                edges = self.get_neighbors(current_vertex)

                for edge in edges:
                    clone = list(current_path)
                    clone.append(edge)
                    s.push(clone)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if path is None:
            path = []

        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path

        for edge in self.get_neighbors(starting_vertex):
            if edge not in visited:
                new_path = self.dfs_recursive(
                    edge, destination_vertex, path, visited)
                if new_path:
                    return new_path
            else:
                return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/BloomInstituteOfTechnology/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
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
