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
        self.vertices[vertex_id]= set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add( v1)
        else:
            raise IndexError("thar vertex doesnot exist")

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
        queue = Queue()
        queue.enqueue(starting_vertex)
        # create set to store vertices
        visited = set()
        # while que isn't empty,
        while queue.size() > 0:
            dequeued = queue.dequeue()
            # if vertex not visitied, mark it as visitied then add neighbors
            if dequeued not in visited:
                visited.add(dequeued)
                for i in self.vertices[dequeued]:
                    queue.enqueue(i)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
         s = Stack()
        s.push(starting_vertex)
        # create set to store vertices
        visited = set()
        # while stack isn't empty,
        while s.size() > 0:
            popping = s.pop()
            #if vertex not visited, mark it as visited then add neighbors
            if popping not in visited:
                visited.add(popping)
                for i in self.vertices[popping]:
                    s.push(i)
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set() 
        visited.add(starting_vertex)
        for neighbor_vert in self.get_neighbors(starting_vertex):
            if neighbor_vert not in visited:
                self.dft_recursive(neighbor_vert, visited)

  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        starting = [starting_vertex]
        queue.enqueue(starting)
        # create set to store vertices
        visited = set()
        # while que isn't empty,
        while queue.size() > 0:
            path = queue.dequeue()
            vert = path[-1]
            # if vertex not visitied, mark it as visitied then add neighbors
            if vert not in visited:
                # check for destination target
                if vert == destination_vertex:
                  return path
                visited.add(vert)
                for neighbor_vert in self.vertices[vert]:
                  copy = path[:]
                  copy.append(neighbor_vert)
                  queue.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        starting = [starting_vertex]
        s.push(starting)
        # create set to store vertices
        visited = set()
        while s.size() > 0:
            path = s.pop()
            vert = path[-1]
            #if vertex not visited, mark it as visited then add neighbors
            if vert not in visited:
                # check for destination target
                if vert == destination_vertex:
                  return path
                visited.add(vert)
                for neighbor_vert in self.vertices[vert]:
                  copy = path[:]
                  copy.append(neighbor_vert)
                  s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
            if visited is None:
                    visited = set()
                if path is None:
                    path = []
                visited.add(starting_vertex)
                path = path + [starting_vertex]
                if starting_vertex == destination_vertex:
                    return path
                for neighbor_vert in self.get_neighbors(starting_vertex):
                    if neighbor_vert not in visited:
                        new = self.dfs_recursive(neighbor_vert, destination_vertex, visited, path)
                        if new is not None:
                            return new
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
