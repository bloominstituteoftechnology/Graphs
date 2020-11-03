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
        print('-----------------------------BFT----------------------------------')

        que = Queue()
        que.enqueue(starting_vertex)
        visited = set()
        while que.size() != 0 :
            current = que.dequeue()

            if current not in visited:
                visited.add(current)
                print(current)

                for edge in self.vertices[current]:
                    if edge not in visited:
                        que.enqueue(edge)
                        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print('-----------------------------DFT----------------------------------')
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() != 0 :
            current = stack.pop()

            if current not in visited:
                visited.add(current)
                print(current)

                for edge in self.vertices[current]:
                    if edge not in visited:
                        stack.push(edge)

    def dft_recursive(self, starting_vertex, visited=None, stack = Stack()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            print('------------------------------DFTR---------------------------------')

            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            
            print(starting_vertex)
            for edge in self.vertices[starting_vertex]:
                if edge not in visited:
                    stack.push(edge)

            self.dft_recursive(stack.pop(), visited, stack)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print('------------------------------BFS---------------------------------')

        que = Queue()
        que.enqueue([starting_vertex])
        visited = set()

        while que.size() != 0 :
            path = que.dequeue()
            current = path[-1]

            if current not in visited:
                visited.add(current)

                for edge in self.vertices[current]:
                    new_path = list(path)
                    new_path.append(edge)
                    
                    if new_path[-1] == destination_vertex:
                        return new_path

                    que.enqueue(new_path)
                        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print('----------------------------DFS-----------------------------------')
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size() != 0 :
            path = stack.pop()
            current = path[-1]

            if current not in visited:
                visited.add(current)

                for edge in self.vertices[current]:
                    new_path = list(path)
                    new_path.append(edge)
                    
                    if new_path[-1] == destination_vertex:
                        return new_path

                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex,visited=None, stack = Stack()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if visited == None:
            print('-----------------------------DFSR----------------------------------')
            visited = set()
            stack.push([starting_vertex])

        path = stack.pop()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            
            for edge in self.vertices[starting_vertex]:
                if edge not in visited:
                    new_path = list(path)
                    new_path.append(edge)

                if new_path[-1] == destination_vertex:
                    return new_path
                    

                stack.push(new_path)

            return self.dfs_recursive(new_path[-1], destination_vertex, visited, stack)


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
