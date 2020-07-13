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
        visited = set()
        queue = Queue()
        queue.enqueue(starting_vertex)
        while queue.size():
            current = queue.dequeue()
            print(current)
            visited.add(current)
            neighbours = self.get_neighbors(current)
            for v in neighbours:
                if v not in visited:
                    queue.enqueue(v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()
        # Look at current vertex
        current = starting_vertex
        # until stack is empty and current has no unvisited neighbours
        stack.push(starting_vertex)
        while stack.size():
            # visit current vertex if it wasn't visited
            if current not in visited:
                print(current)
                visited.add(current)
            # look for unvisited neihgbours
            unvisited_neighbours = [
                v for v in self.get_neighbors(current) if v not in visited]
            if unvisited_neighbours:
                # If it has an unvisited neighbour, push current vertex on stack, make neighbour current
                stack.push(current)
                current = unvisited_neighbours[0]
            else:
                # If it has no unvisited neighbors, pop off stack and set as current
                current = stack.pop()
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for v in self.get_neighbors(starting_vertex):
                self.dft_recursive(v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        paths = Queue()
        paths.enqueue([starting_vertex])
        # store a queue of paths
        while paths.size():
            path = paths.dequeue()
            node = path[-1]
            # if the path ends with destination vertex, that the path we need, bfs ensures it's the shortest
            if node == destination_vertex:
                return path
            # else, look at all the neghbours, and add new paths to the queue
            else:
                for adjacent in self.get_neighbors(node):
                    new_path = path+[adjacent]
                    paths.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        path = []
        visited = set()
        stack = Stack()
        # Look at current vertex
        current = starting_vertex
        # until stack is empty and current has no unvisited neighbours
        stack.push(starting_vertex)
        # if current vertex is destination vertex, we are done, if destination vertex not found, done
        while stack.size() and current is not destination_vertex:
            # visit current vertex if it wasn't visited
            if current not in visited:
                visited.add(current)
            # look for unvisited neihgbours
            unvisited_neighbours = [
                v for v in self.get_neighbors(current) if v not in visited]
            if unvisited_neighbours:
                # If it has an unvisited neighbour, push current vertex on stack, make neighbour current
                stack.push(current)
                current = unvisited_neighbours[0]
            else:
                # If it has no unvisited neighbors, pop off stack and set as current
                current = stack.pop()
        # backtrack and build the path in reverse.
        while stack.size():
            path.append(current)
            current = stack.pop()
        path.reverse()
        return path

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # if this is the vertex we are looking for, return [starting vertex]
        if starting_vertex == destination_vertex:
            visited.add(starting_vertex)
            return [starting_vertex]
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            for v in self.get_neighbors(starting_vertex):
                path = self.dfs_recursive(v, destination_vertex, visited)
                if path:
                    return [starting_vertex] + path

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
