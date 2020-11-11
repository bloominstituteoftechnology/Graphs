"""
Simple graph implementation
"""
from collections import deque  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            print("Error: 1 or both vertices not found")
            return
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        if vertex_id not in self.vertices:
            print(f"Error: id {vertex_id} not found")
            return
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        if starting_vertex not in self.vertices:
            print(f"Error: {starting_vertex} not found")
            return
        discovered = set()
        queue = deque()

        queue.append(starting_vertex)
        while len(queue) > 0:
            curr_node = queue.popleft()
            if curr_node not in discovered:
                discovered.add(curr_node)
                print(curr_node)
                for neighbor in self.vertices[curr_node]:
                    queue.append(neighbor)



    def dft(self, starting_vertex):
        if starting_vertex not in self.vertices:
            print(f"Error: {starting_vertex} not found")
            return
        discovered = set()
        stack = []

        stack.append(starting_vertex)
        while len(stack) > 0:
            curr_node = stack.pop()
            if curr_node not in discovered:
                discovered.add(curr_node)
                print(curr_node)
                for neighbor in self.vertices[curr_node]:
                    stack.append(neighbor)
        

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
        pass  # TODO

    def dfs(self, starting_vertex, goal_vertex):
        stack = []
        visited = set()
        # push the current path you're on onto the stack, instead of just a single vertex
        stack.append([starting_vertex])

        while len(stack) > 0:
            currPath = stack.pop()
            currNode = currPath[-1] # the current node you're on is the last node in the path
            if currNode == goal_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath) # make copy of current path
                    newPath.append(neighbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
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
    print("breadth first traversal")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("depth first traversal")
    graph.dft(1)
    print("depth first traversal - recursive")
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
