"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from functools import reduce

class MazeGraph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = {}
            return self.vertices[vertex_id]
        else:
            return None

    def add_edge(self, direction, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices:
            self.vertices[v1][direction] = v2
        else:
            self.vertices[v1] = {}
            self.vertices[v1][direction] = v2

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return {} 

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set() 

        while q.size() > 0:
            vertex = q.dequeue()
            print(vertex)
            visited.add(vertex)

            for next_vert in self.get_neighbors(vertex).values():
                if next_vert not in visited:
                    q.enqueue(next_vert)
                    # It hasn't been visited yet, but it will be in the near future.
                    visited.add(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            vertex = s.pop()
            # if vertex not in visited:
            print(vertex)
            visited.add(vertex)

            for next_vert in self.get_neighbors(vertex).values():
                if next_vert not in visited:
                    s.push(next_vert)
                    visited.add(next_vert)
     

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        def traverse(vertex, visited):
            neighbors = self.get_neighbors(vertex).values()
            if vertex not in visited:
                print(vertex)
                visited.append(vertex)
            
                for next_vert in neighbors:
                    traverse(next_vert, visited)

        return traverse(starting_vertex, [])
                 

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            cur_path = q.dequeue()
            if cur_path[-1] == destination_vertex:
                return cur_path
            else:
                for vertex in self.get_neighbors(cur_path[-1]).values():
                    if vertex not in visited:
                        visited.add(vertex)
                        q.enqueue(cur_path + [vertex])
        return [] 

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
            cur_path = s.pop()
            if cur_path[-1] == destination_vertex:
                return cur_path
            else:
                for vertex in self.get_neighbors(cur_path[-1]).values():
                    if vertex not in visited:
                        visited.add(vertex)
                        s.push(cur_path + [vertex])

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def find_shortest_path(path, visited):
            if path[-1] == destination_vertex:
                return path
            else:
                visited.append(path[-1])
                for vertex in self.get_neighbors(path[-1]).values():
                    if vertex not in visited:
                        shortest_path = find_shortest_path(path + [vertex], visited)
                        if shortest_path is not None:
                            return shortest_path
                return None       

        return find_shortest_path([starting_vertex], [])
        


if __name__ == '__main__':
    graph = MazeGraph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge("n", 5, 3)
    graph.add_edge("s", 6, 3)
    graph.add_edge("e", 7, 1)
    graph.add_edge("w", 4, 7)
    graph.add_edge("e", 1, 2)
    graph.add_edge("e", 7, 6)
    graph.add_edge("w", 2, 4)
    graph.add_edge("s", 3, 5)
    graph.add_edge("n", 2, 3)
    graph.add_edge("n", 4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

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
