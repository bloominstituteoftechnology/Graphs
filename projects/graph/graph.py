"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import sys
sys.setrecursionlimit(1000000)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            KeyError('Error')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()

        queue.enqueue(starting_vertex)
        visited_path = set()

        while queue.size() > 0:
            dequeued = queue.dequeue()
            if dequeued not in visited_path:
                visited_path.add(dequeued)
                # print(dequeued)
                for items in self.vertices[dequeued]:
                    queue.enqueue(items)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        s.push(starting_vertex)
        visited_path = set()

        while s.size() > 0:
            depoped = s.pop()
            if depoped not in visited_path:
                # print(depoped)
                visited_path.add(depoped)

                for items in self.vertices[depoped]:
                    s.push(items)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(starting_vertex)
        visited.add(starting_vertex)
        for vertice in self.vertices[starting_vertex]:
            if vertice not in visited:
                self.dft_recursive(vertice, visited)

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
            vert = path[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    return path

                visited.add(vert)
            for next_vert in self.vertices[vert]:
                new_path = list(path)
                new_path.append(next_vert)
                queue.enqueue(new_path)

        return None

    def dfs(self, starting_vertex, destination_vertex, visited=set()):
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
            vert = path[-1]
            if vert not in visited:
                if vert == destination_vertex:
                    return path

                visited.add(vert)
            for next_vert in self.vertices[vert]:
                new_path = list(path)
                new_path.append(next_vert)
                stack.push(new_path)

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
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.bft(1)

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