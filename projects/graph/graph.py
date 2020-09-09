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
            # self.vertices[v2].add(v1) # bidirectional 
        else:
            raise IndentationError("nonexistent vertex")
         

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
        # helps find shortest path
        # create an empty Queue
        q = Queue()
        # Add starting vertex ID 
        q.enqueue(starting_vertex)
        # create set for visited verts
        visited = set()
        # while queue is not empty
        while q.size() > 0:
            # Deque a vert
            v = q.dequeue()
            # If not visited
            if v not in visited:
                # visit it
                # print(v)
                # mark as visited
                visited.add(v)
                # add all neighbors to the queue
                for neighbors in self.get_neighbors(v):
                    q.enqueue(neighbors)
                


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack
        s = Stack()
        # add the starting vertext to the stack
        s.push(starting_vertex)
        # create a set for the visited verts
        visted = set()
        # while q is not empty
        while s.size() > 0:
            # pop a vert
            v = s.pop()
            # if not in visited
            if v not in visted:
                # visit it
                # print(v)
                # mark as visited
                visted.add(v)
                # add all the neighbors to the stack
                for neighbors in self.get_neighbors(v):
                    s.push(neighbors)

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
        # create an empty queue
        q = Queue()
        # enqueue the starting vert path
        q.enqueue([starting_vertex])
        # create a set for visited verts
        visited = set()
        # while q is not empty
        while q.size() > 0:
            # dequeue a vert 
            v = q.dequeue()
            # grab the last vertex from the path
            last_vertex = v[-1]
            # if that vertex has not been visited
            if last_vertex not in visited:
                # check if its the target
                if last_vertex == destination_vertex:
                    # if it is return
                    return v
                # mark it as visited
                visited.add(last_vertex)
                # add a path to its neighbors
                for i in self.vertices[last_vertex]:
                    new_path = list(v)
                    new_path.append(i)
                    q.enqueue(new_path)


            

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            v = s.pop()
            last_vertex = v[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return v
                visited.add(last_vertex)
                for i in self.vertices[last_vertex]:
                    new_path = list(v)
                    new_path.append(i)
                    s.push(new_path)
        

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()

        if starting_vertex == destination_vertex:
            return starting_vertex
        if starting_vertex not in visited:
            visited.add(starting_vertex)
        for i in self.vertices[starting_vertex]:
            if i not in visited:
                new_path = list(visited)
                new_path.append(i)
            return self.dfs_recursive(new_path, destination_vertex)


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
    # graph.dft_recursive(1)

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
    # print(graph.dfs_recursive(1, 6))
