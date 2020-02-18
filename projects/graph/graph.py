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
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex doesn't exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        create an empty queue
        add starting vertex id to queue
        create empty set to store visited nodes
        while queue is not empty
            dequeue first vert
            check if visited
            if not
                mark as visited
                add all neighbors to queue
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visted = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visted:
                print(v)
                visted.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        create an empty stack
        push starting vertex id to stack
        create empty set to store visited nodes
        while stack is not empty
            pop first vert
            check if visited
            if not
                mark as visited
                add all neighbors to stack
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        check if node is visited
        if not
            mark as visited
            (print)
            call dft recurse on each child
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)#, visited)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        create an empty queue
        add a PATH to the starting vert to the queue
        create an empty set to store visited
        while the queue is not empty
            dequeue the first path
            grab last vertex from path
            check if it's the target
                if so, return path
            check if visited
            if not visited
                mark as visited
                add path to all neighbors
                    (make a copy of the path before adding)
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            vert = path[-1]
            if vert == destination_vertex:
                return path
            if vert not in visited:
                visited.add(vert)
                for neighbor in self.get_neighbors(vert):
                    newPath = path.copy()
                    newPath.append(neighbor)
                    q.enqueue(newPath)
        return None

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
            path = s.pop()
            vert = path[-1]
            if vert == destination_vertex:
                return path
            if vert not in visited:
                visited.add(vert)
                for neighbor in self.get_neighbors(vert):
                    newPath = path.copy()
                    newPath.append(neighbor)
                    s.push(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex in visited:
            return None
        elif starting_vertex == destination_vertex:
            return [destination_vertex]
        else:
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                neighborSearch = self.dfs_recursive(neighbor, destination_vertex, visited)
                if neighborSearch is not None:
                    return [starting_vertex] + neighborSearch
            return None

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
    print("all vertices")
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
    print("breadth first traverse")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("depth first traverse")
    graph.dft(1)
    print("depth first traverse - recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("breadth first search")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("depth first search")
    print(graph.dfs(1, 6))
    print("depth first search - recursive")
    print(graph.dfs_recursive(1, 6))
