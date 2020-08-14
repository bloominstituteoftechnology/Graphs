"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist.")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()

        while queue.size() > 0:
            v = queue.dequeue()

            if v not in visited:
                visited.add(v)

                for next_vertex in self.get_neighbors(v):
                    queue.enqueue(next_vertex)
        return visited

    def dft(self, starting_vertex):
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            v = stack.pop()

            if v not in visited:
                visited.add(v)

                for next_vertex in self.get_neighbors(v):
                    stack.push(next_vertex)
        
        # last = visited.pop()
        # return last

    def dft_recursive(self, starting_vertex, visited = None):

        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        for neighbors in self.get_neighbors(starting_vertex):
            if neighbors not in visited:
                self.dft_recursive(neighbors, visited)

        return visited

        # if visited is None:
        #     visited = set()
        
        # if starting_vertex not in visited:
        #     visited.add(starting_vertex)
            
        #     for neighbor in self.get_neighbors(starting_vertex):
        #         self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue and enqueue PATH to the Starting Vertex ID
        queue = Queue()
        queue.enqueue([starting_vertex]) # Enqueue PATH by making SV a List

        # Create a set to store visited vertices
        visited = set()

        # While the queue is not empty:
        while queue.size() > 0:

            # Dequeue the first PATH
            path = queue.dequeue()

            # Grab the last vertex from the PATH
            last_vertex = path[-1]

            # Check if the vertex has not been visited:
            if last_vertex not in visited:

                # Is this the vertex the target?
                if last_vertex == destination_vertex:

                    # If it is, return the PATH
                    return path

                else:
                    # Mark the vertex as visited
                    visited.add(last_vertex)

                    # Then add a PATH to its neighbors to the back of the queue
                    for neighbor in self.get_neighbors(last_vertex):

                        # Make a copy of the PATH
                        newPath = path.copy() # list(path) or [path] Many dif ways

                        # Append the neighbor to the back of the PATH
                        newPath.append(neighbor)

                        # Enqueue out new PATH
                        queue.enqueue(newPath)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        # Create an empty Stack and Push PATH to the Starting Vertex
        stack = Stack()
        stack.push([starting_vertex])

        # Create a set to store visited vertices
        visited = set()

        # While stack is not empty:
        while stack.size() > 0:

            # Pop the first PATH
            path = stack.pop()

            # Grab the last vertex from the PATH
            last_vertex = path[-1]

            # Check if the vertex has not been visited:
            if last_vertex not in visited:

                # Is this vertex the target?
                if last_vertex == destination_vertex:

                    # If it is, return the PATH
                    return path
                
                else:
                    # Mark the vertex as visited
                    visited.add(last_vertex)

                    # Then add a PATH to its neighbors on top of the stack
                    for neighbor in self.get_neighbors(last_vertex):

                        # Make a copy of the PATH
                        newPath = path.copy()

                        # Append the neighbor to the back of the PATH
                        newPath.append(neighbor)

                        # Push out new Path
                        stack.push(newPath)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None):
        if visited == None:
            visited = set()
        if starting_vertex in visited:
            return None
        elif starting_vertex == destination_vertex:
            return [destination_vertex]
        else:
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                neighborSearch = self.dfs_recursive(neighbor, destination_vertex, visited)
                if neighborSearch is not None:
                    return [starting_vertex] + neighborSearch
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
    print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft(1))
    print(graph.dft_recursive(1))

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
