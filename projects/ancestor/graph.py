"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            raise Exception('Vertex not found')
        self.vertices[v1] = {*self.vertices[v1], v2}
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        qq = Queue()
        visited = set()
        qq.enqueue(starting_vertex)
        while qq.size() > 0:
            vertex = qq.dequeue()
            visited.add(vertex)
            print(vertex)
            for edge in self.vertices[vertex]:
                if edge not in visited:
                    qq.enqueue(edge)
            
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stk = Stack()
        visited = {starting_vertex}
        stk.push(starting_vertex)
        while stk.size() > 0:
            vertex = stk.pop()
            print(vertex)
            for edge in self.vertices[vertex]:
                if edge not in visited:
                    stk.push(edge)
                    visited.add(edge)


    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if starting_vertex in visited:
            pass #Base case
        else:
            visited.add(starting_vertex)
            print(starting_vertex)
            for edge in self.vertices[starting_vertex]:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        qq = Queue()
        path = []
        visited = set()
        qq.enqueue([starting_vertex])
        while qq.size() > 0:
            path = qq.dequeue()
            visited.add(path[-1])
            for edge in self.vertices[path[-1]]:
                if edge == destination_vertex:  
                    path.append(edge)
                    return path
                if edge not in visited:
                    qq.enqueue(list([*path, edge]))


    def bfs_longest_route(self, starting_vertex):
        """
        Returns the vertex furthest from the starting vertex
        """

        qq = Queue()
        path = []
        greatest_distance = [0,0]
        qq.enqueue([starting_vertex])
        while qq.size() > 0:
            path = qq.dequeue()
            for edge in self.vertices[path[-1]]:
                qq.enqueue(list([*path, edge]))
            if self.vertices[path[-1]] == set():
                if len(path) ==  greatest_distance[0]: 
                    if path[-1] < greatest_distance[1]: #this check will allow us to return the lowest value node on a tie
                        greatest_distance[1] = path[-1]
                if len(path) > greatest_distance[0]:
                    greatest_distance[0] = len(path)
                    greatest_distance[1] = path[-1]
        return greatest_distance[1]



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stk = Stack()
        path = []
        visited = {starting_vertex}
        stk.push(starting_vertex)
        while stk.size() > 0:
            vertex = stk.pop()
            path.append(vertex)
            for edge in self.vertices[vertex]:
                if edge not in visited:
                    stk.push(edge)
                    visited.add(edge)
                    if edge == destination_vertex:
                        path.append(edge)
                        return path





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
