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
        else:
            print("Warning, vertex already exists")

    def add_edge(self, source_vertex, destination_vertex):
        """
        Add a directed edge to the graph.
        """
        if source_vertex in self.vertices and destination_vertex in self.vertices:
            self.vertices[source_vertex].add(destination_vertex)
        else:
            print("Can not add edge between non-existant vertices")
        
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        q.enqueue(starting_vertex)
        found = [starting_vertex]
        while q.size() > 0:
            for vertex in self.vertices[q.queue[0]]:
                if vertex not in found:
                    q.enqueue(vertex)
                    found.append(vertex)
            q.dequeue()
        
        print(found)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        s.push(starting_vertex)
        found = []

        while s.size() > 0:
            v = s.pop()

            if v not in found:
                found.append(v)
                
                for next_vert in self.vertices[v]:
                    s.push(next_vert)

        print(found)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        def helper(graph, starting_vertex, visited):
            if starting_vertex not in visited:
                visited.append(starting_vertex)

                for vertex in graph.vertices[starting_vertex]:
                    helper(graph, vertex, visited)

        visited = []

        helper(self, starting_vertex, visited)

        print(visited)

        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #attempting with dictionary of traversal arrays

        path_from_start = {}
        q = Queue()
        q.enqueue(starting_vertex)
        path_from_start[starting_vertex] = [starting_vertex]
        visited = [starting_vertex]

        while q.size() > 0:
            for vertex in self.vertices[q.queue[0]]:
                if vertex not in visited:
                    q.enqueue(vertex)
                    # We get to any node by going from its "parent" to itself
                    # So we just add a node to it's parent's path
                    path_from_start[vertex] = path_from_start[q.queue[0]] + [vertex]
                    visited.append(vertex)
                if vertex == destination_vertex:
                    return path_from_start[vertex]
            q.dequeue()

        return None

        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push(starting_vertex)
        found = []

        while s.size() > 0:
            v = s.pop()

            if v not in found:
                found.append(v)
                
                for next_vert in self.vertices[v]:
                    s.push(next_vert)
            if v == destination_vertex:
                break

        return found




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
