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
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        return set()

    def bft(self, start):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = []
        visited = set()
        queue.append(start)
        while queue:
            curr_node = queue.pop(0)
            if curr_node not in visited:
                visited.add(curr_node)
                print(curr_node)
                for edge in self.get_neighbors(curr_node):
                    queue.append(edge)

    def dft(self, start):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = []
        stack.append(start)
        visited = set()
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                print(curr)
                for edge in self.get_neighbors(curr):
                    stack.append(edge)

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if vertex in visited:
            return
        visited.add(vertex)
        print(vertex)
        for edge in self.get_neighbors(vertex):
            self.dft_recursive(edge, visited)

    def bfs(self, start, end):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = []
        visited = set()
        queue.append([start])
        while queue:
            curr_path = queue.pop(0)
            curr_node = curr_path[-1]
            if curr_node == end:
                return curr_path
            if curr_node not in visited:
                visited.add(curr_node)
                for edge in self.get_neighbors(curr_node):
                    new_path = list(curr_path)
                    new_path.append(edge)
                    queue.append(new_path)

    def dfs(self, start, end):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = []
        stack.append([start])
        visited = set()
        while stack:
            curr_path = stack.pop() # [1,2,3]
            curr_node = curr_path[-1] #
            if curr_node == end:
                return curr_path
            if curr_node not in visited:
                visited.add(curr_node)
                print(curr_path)
                for edge in self.get_neighbors(curr_node):
                    # creates new arr with current path
                    new_path = list(curr_path)
                    # add edges into 
                    new_path.append(edge)
                    stack.append(new_path)

    def dfs_recursive(self, start, end):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        
        def recurse(vertex, end, visited=set()):
            curr_node = vertex[-1]
            if curr_node in visited:
                return 
            if curr_node == end:
                return vertex
            visited.add(curr_node)
            for edge in self.get_neighbors(curr_node):
                new_path = list(vertex)
                new_path.append(edge)
                res = recurse(new_path, end, visited)
                if res:
                    return res
        return recurse([start], end)


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
