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
        queue = Queue()
        visited = set()

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            vertice = queue.dequeue()

            if vertice not in visited:
                visited.add(vertice)
                print(vertice)

                for next_vertice in self.get_neighbors(vertice):
                    queue.enqueue(next_vertice)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)

        while stack.size() > 0:
            # pop the first item 
            vertice = stack.pop()

            if vertice not in visited:
                visited.add(vertice)
                print(vertice)

                for next_vertice in self.get_neighbors(vertice):
                    stack.push(next_vertice)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def dft_recursive_inner(vertex):
            if vertex in visited:
                return
            else:
                visited.add(vertex)
            
            print(vertex)

            for next_vertice in self.get_neighbors(vertex):
                dft_recursive_inner(next_vertice)

        dft_recursive_inner(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue() 
        visited = set()

        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            path = queue.dequeue()
            last_vertex = path[-1] # grab the last element in the array

            if last_vertex in visited:
                continue
            else:
                visited.add(last_vertex)

            for neighbor in self.get_neighbors(last_vertex):
                next_path = path.copy()
                next_path.append(neighbor)

                if neighbor == destination_vertex:
                    return next_path
                queue.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack() 
        visited = set()

        stack.push([starting_vertex])

        while stack.size() > 0:
            path = stack.pop()
            last_vertex = path[-1] # grab the last element in the array

            if last_vertex in visited:
                continue
            else:
                visited.add(last_vertex)

            for neighbor in self.get_neighbors(last_vertex):
                next_path = path.copy()
                next_path.append(neighbor)

                if neighbor == destination_vertex:
                    return next_path
                stack.push(next_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()

        def dft_inner(vertex_path):
            last_vertex = vertex_path[-1]
            
            if last_vertex in visited:
                return None
            else:
                visited.add(last_vertex)

            if last_vertex == destination_vertex:
                return vertex_path
            
            for neighbor in self.get_neighbors(last_vertex):
                next_path = vertex_path.copy()
                next_path.append(neighbor)
            
                found = dft_inner(next_path)
                if found:
                    return found
            
            return None

        return dft_inner([starting_vertex])

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
    print("graph.dft(1)")
    graph.dft(1)
    print("graph.dft_recursive(1)")
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
