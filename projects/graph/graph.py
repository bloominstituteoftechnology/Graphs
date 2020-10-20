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
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("el zoro")


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        neighbor = self.vertices[vertex_id]
        return neighbor

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # visited = [False] * (len(self.vertices))
        queue = []
        queue.append(starting_vertex)
        # visited[starting_vertex] = True
        visited = set()

        while len(queue) > 0:
            cur_vertex = queue.pop(0)
            # starting_vertex = queue.pop(0)
            

            if cur_vertex not in visited:
                print(cur_vertex)
                visited.add(cur_vertex)

                for i in self.get_neighbors(cur_vertex):
                    queue.append(i)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # visited = [False for i in range(self.vertices)]  
  
        stack = []  
        stack.append(starting_vertex)  
        visited = set()
  
        while len(stack) > 0:
            cur_vertex = stack.pop()

            if cur_vertex not in visited:
                print(cur_vertex)
                visited.add(cur_vertex)
                for n in self.get_neighbors(cur_vertex):
                    stack.append(n)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = None
        if visited is None:
            visited = set()
        visited.add(starting_vertex)

        for next in self.vertices[starting_vertex] - visited:
            self.dft_recursive(next)
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = [ [starting_vertex] ] 
        visited = set()
       
        while len(queue) > 0:
            current_path = queue.pop(0)
            current_vertex = current_path[-1]

            if current_vertex not in visited:
                visited.add(current_vertex)

                if current_vertex == destination_vertex:
                    return current_path
                    
                for neighbor in self.get_neighbors(current_vertex):
                        current_path_copy = list(current_path)
                        current_path_copy.append(neighbor)
                        queue.append(current_path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """  
        stack = [ [starting_vertex] ] 
        visited = set()
       
        while len(stack) > 0:
            current_path = stack.pop(0)
            current_vertex = current_path[-1]

            if current_vertex not in visited:
                visited.add(current_vertex)

                if current_vertex == destination_vertex:
                    return current_path
                    
                for neighbor in self.get_neighbors(current_vertex):
                        current_path_copy = list(current_path)
                        current_path_copy.append(neighbor)
                        stack.append(current_path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        found = False
        if starting_vertex == destination_vertex:
            return True
        if visited is None:
            visited.add(starting_vertex)
        for neighbour in (set(self.vertices[starting_vertex]) - visited):
            if destination_vertex == neighbour:
                return True
            found = self.dfs_recursive(neighbour, destination_vertex)
        return found

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
