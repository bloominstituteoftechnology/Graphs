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
        else:
            self.vertices[v1].add(v2)

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
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass  # TODO
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        #Edge case: Start node is destination, return start node.

        queue = self.queue
        vertices = self.vertices
        if starting_vertex is destination_vertex:
            return [starting_vertex] # singleton list?

        checked = []
        route = []
        queue.enqueue(starting_vertex)
        checked.append(starting_vertex) #Edge case: This/a graph may have cycles to the starting vert.
        location = starting_vertex
        # checked.append(location)
        route.append(location)
        i = 1
        while queue.size():
            # we have to dequeue somewhere to meet our base case and end the loop!
            # if none of a verts edges touch the destination vert, we can add that vert to the route,
            # because there's no way to get to the destination without traversing it!
            for v in vertices[location]:  # yikes, I think this line might be O(n^2).
                if v not in checked and v is destination_vertex:
                    route.append(location)
                    route.append(v)
                    # return route
                else:
                    queue.enqueue(v)
                    checked.append(v)
            location = checked[i]
            route.append(location)
            i += 1
        return route
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





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
    # graph.dft_recursive(1)
    #
    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print(graph.bfs(1, 6))
    #
    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
