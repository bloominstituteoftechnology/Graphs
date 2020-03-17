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
        # pass  # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ImportError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)

                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  # TODO
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                visited.add(v)
                print(v)

                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass  # TODO
        visited.add(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)

        if len(neighbors) == 0:
            return
        else:
            for neighbor in neighbors:
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            first_path = q.dequeue()
            last_vertex = first_path[-1]
            if last_vertex == destination_vertex:
                return first_path
            else:
                if last_vertex not in visited:
                    visited.add(last_vertex)
                    neighbors = self.get_neighbors(last_vertex)

                    for neighbor in neighbors:
                        copy_path = list(first_path)
                        copy_path.append(neighbor)
                        q.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            first_path = s.pop()
            last_vertex = first_path[-1]
            if last_vertex == destination_vertex:
                return first_path
            else:
                if last_vertex not in visited:
                    visited.add(last_vertex)
                    neighbors = self.get_neighbors(last_vertex)

                    for neighbor in neighbors:
                        copy_path = list(first_path)
                        copy_path.append(neighbor)
                        s.push(copy_path)

    def dfs_recursive(self, starting_vertex, target_value, visited=set(), path=[]):
        # def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # pass  # TODO
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        neighbors = self.vertices[starting_vertex]

        if starting_vertex == target_value:
            return path
        if len(neighbors) == 0:
            return
        else:
            for neighbor in neighbors:
                if neighbor not in visited:
                    # self.dft_recursive(neighbor, visited)
                    new_path = self.dfs_recursive(
                        neighbor, target_value, visited, path)
                    if new_path:
                        return new_path
            # return None
        # if visited is None:
        #     visited = set()
        # if path is None:
        #     path = []
        # visited.add(starting_vertex)
        # path = path + [starting_vertex]
        # if starting_vertex == target_value:
        #     return path
        # for neighbor in self.vertices[starting_vertex]:
        #     if neighbor not in visited:
        #         # self.dft_recursive(neighbor, visited)
        #         new_path = self.dfs_recursive(
        #             neighbor, target_value, visited, path)
        #         if new_path:
        #             return new_path
        # return None


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
