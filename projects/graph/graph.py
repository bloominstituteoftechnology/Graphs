"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.queue = Queue()
        self.stack = Stack()
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            self.add_vertex(v1)
        elif v1 in self.vertices:
            self.vertices[v1].add(v2)

        # ****** Undirected
    def add_bi_edge(self, v1, v2):
        vertices = self.vertices
        if v1 and v2 in vertices:
            self.add_edge(v1, v2)
            self.add_edge(v2, v1)
        elif v1 and v2 not in vertices:
            self.add_vertex(v1)
            self.add_vertex(v2)
            self.add_bi_edge(v1, v2)
        # self.add_vertex(v1)
        # self.add_vertex(v2)
        # self.vertices[v1].add(v2)
        # self.vertices[v2].add(v1)


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        visited = []
        vertices = self.vertices
        queue = self.queue
        queue.enqueue(starting_vertex)
        while queue.size():
            cur_ver = queue.dequeue()
            if cur_ver not in visited:
                visited.append(cur_ver)
                for v in vertices[cur_ver]:
                    queue.enqueue(v)
        self.queue = Queue()
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = self.stack
        vertices = self.vertices
        visited = []
        stack.push(starting_vertex)
        while stack.size():
            cur_ver = stack.pop()
            if cur_ver not in visited:
                visited.append(cur_ver)
                for v in vertices[cur_ver]:
                    stack.push(v)
        self.stack = Stack()
        return visited
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # stack = self.stack
        # vertices = self.vertices
        # visited = []
        # stack.push(starting_vertex)
        # while stack.size():
        #     cur_ver = stack.pop()
        #     if cur_ver not in visited:
        #         visited.append(cur_ver)
        #         for v in vertices[cur_ver] or v not in visited:
        #             self.dft_recursive(v)
        # return visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)
        else:
            print(visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = self.queue
        vertices = self.vertices
        checked = []
        route = set()
        queue.enqueue(starting_vertex)
        checked.append(starting_vertex)
        location = starting_vertex
        route.add(location)
        i = 0
        if starting_vertex is destination_vertex:
            return [starting_vertex]
        while queue.size():
            for v in vertices[location]:
                if v is destination_vertex:
                    route.add(location)
                    route.add(v)
                    return route
                elif v is not destination_vertex:
                    queue.enqueue(v)
                    checked.append(v)
                if destination_vertex in vertices[v]:
                    route.add(location)
            location = checked[i]
            i += 1
        self.queue = Queue()





    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = self.stack
        visited = []
        route = set()
        vertices = self.vertices
        location = starting_vertex
        stack.push(starting_vertex)
        visited.append(starting_vertex)
        if starting_vertex is destination_vertex:
            return [starting_vertex]
        while stack.size():
            print('Placeholder')
            for v in vertices[location]:
                if v is destination_vertex:
                    print('Placeholder')
                elif v is not destination_vertex:
                    print('Placeholder')
                if destination_vertex in vertices[v]:
                    print('Placeholder')
        self.stack = Stack()




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


# print(graph.vertices)
    # '''
    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    #
    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
# print('dft:', graph.dft(1))
    #
    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)
    #
    # '''
    # Valid DFT recursive paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    graph.dft_recursive(1)
    #
    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))
    #
    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
