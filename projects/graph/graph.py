"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """
    Represent a graph as a dictionary of
    vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Invalid vertex')

    def neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        toVisit = Queue()
        toVisit.enqueue(starting_vertex)

        while toVisit.size() > 0:
            node = toVisit.dequeue()
            if node not in visited:
                print(node)
                visited.add(node)
                for neighbor in self.neighbors(node):
                    if neighbor not in visited:
                        toVisit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        toVisit = Stack()
        toVisit.push(starting_vertex)

        while toVisit.size() > 0:
            node = toVisit.pop()
            if node not in visited:
                print(node)
                visited.add(node)
                for neighbor in self.neighbors(node):
                    if neighbor not in visited:
                        toVisit.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def traverse(node):
            if node not in visited:
                print(node)
                visited.add(node)
                for neighbor in self.neighbors(node):
                    if neighbor not in visited:
                        traverse(neighbor)

        traverse(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        toVisit = Queue()
        trail = [starting_vertex]
        toVisit.enqueue(trail)

        while toVisit.size() > 0:
            current = toVisit.dequeue()
            node = current[-1]

            if node == destination_vertex:
                return current

            if node not in visited:
                visited.add(node)
                for neighbor in self.neighbors(node):
                    toVisit.enqueue(current + [neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        toVisit = Stack()
        trail = [starting_vertex]
        toVisit.push(trail)

        while toVisit.size() > 0:
            current = toVisit.pop()
            node = current[-1]

            if node == destination_vertex:
                return current

            if node not in visited:
                visited.add(node)
                for neighbor in self.neighbors(node):
                    toVisit.push(current + [neighbor])

    def dfs_recursive(self, vertex, destination_vertex,
                      trail=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if len(trail) == 0:
            trail.append(vertex)
        # mark node as visited
        visited.add(vertex)
        # check if it's our target node, if so, return
        if vertex == destination_vertex:
            return trail
        for neighbor in self.neighbors(vertex):
            if neighbor not in visited:
                result = self.dfs_recursive(
                    neighbor, destination_vertex, trail + [neighbor], visited
                )
                if result is not None:
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
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
