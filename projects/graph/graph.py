"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('Invalid Vertex')

    def bft(self, starting_vertex):
        q = Queue()
        v = set()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            x = q.dequeue()

            if x not in v:
                print("BFT", v)
                v.add(x)
                for n in self.vertices[x]:
                    q.enqueue(n)

    def dft(self, starting_vertex):
        s = Stack()
        v = set()
        s.push(starting_vertex)

        while s.size() > 0:
            x = s.pop()
            if x not in v:
                print("DFT", x)
                v.add(x)
                for n in self.vertices[x]:
                    s.push(n)

    def dft_recursive(self, starting_vertex, v=None):
        if v is None:
            v = set()
        print('DFT_R', starting_vertex)
        v.add(starting_vertex)

        for x in self.vertices[starting_vertex]:
            if x not in v:
                self.dft_recursive(x, v)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        v = set()
        q.enqueue([starting_vertex])
        while q.size() > 0:
            path = q.dequeue()
            node = path[-1]
            if node == destination_vertex:
                return path
            for x in self.vertices[node]:
                new_path = path.copy()
                new_path.append(x)
                q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push((starting_vertex, [starting_vertex]))

        while s.size() > 0:
            v = s.pop()
            for x in self.vertices[v[0]]:
                if x == destination_vertex:
                    return v[1] + [x]
                else:
                    s.push((x, v[1] + [x]))


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
    print("verticles", graph.vertices)

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
    print("BFS", graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS", graph.dfs(1, 6))
