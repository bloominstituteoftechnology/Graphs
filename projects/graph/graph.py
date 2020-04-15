"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # adjesancy list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph. from v1 to v2 
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("Vertex not found!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        qq = Queue()
        qq.enqueue(starting_vertex)
        
        visited = set()
        while qq.size() > 0:
            v = qq.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    qq.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for n in self.get_neighbors(v):
                    stack.push(n)

    def dft_recursive(self, starting_vertex,visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for n in self.get_neighbors(starting_vertex):
                visited = self.dft_recursive(n, visited)
        return visited
            

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create a queue
        q = Queue()
        # enqueue the path to starting vertex
        q.enqueue([starting_vertex])
        # set for visited
        visited = set()
        # as long as not empty dequeue the first path
        while q.size() > 0:
            path = q.dequeue()
            if path[-1] not in visited:
                visited.add(path[-1])
                if path[-1] == destination_vertex:
                    return path
                for n in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(n)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #create a queue
        stack = Stack()
        # enqueue the path to starting vertex
        stack.push([starting_vertex])
        # set for visited
        visited = set()
        # as long as not empty dequeue the first path
        while stack.size() > 0:
            path = stack.pop()
            if path[-1] not in visited:
                visited.add(path[-1])
                if path[-1] == destination_vertex:
                    return path
                for n in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(n)
                    stack.push(new_path)
        

    def dfs_recursive(self, starting_vertex, destination_vertex, paths=Queue(), visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = paths.dequeue()
        if path == None:
            path = [starting_vertex]
        
        if path[-1] not in visited:
            visited.add(path[-1])
            for n in self.get_neighbors(path[-1]):
                if n == destination_vertex:
                    path.append(n)
                    return path
                new_path = list(path)
                new_path.append(n)
                paths.enqueue(new_path)
            return self.dfs_recursive(starting_vertex, destination_vertex, paths, visited)
    def bft_find_furthest(self, starting_vertex):
        qq= Queue()
        qq.enqueue(starting_vertex)
        visited = set()
        while qq.size() > 0:
            v = qq.dequeue()
            if v not in visited:
                visited.add(v)
                for n in self.get_neighbors(v):
                    qq.enqueue(n)
                    # return furthest:
                    if v == starting_vertex:
                        return -1
                    else:
                        return v    

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
