"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # adjacency list
        self.color = {} # color list for recursion

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2.
        """
        # check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('ERROR ADDING EDGE: Vertex not found')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # breakpoint()
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while qq.size() > 0:
            # dequeue/pop first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        qq = Stack()
        qq.push([starting_vertex])
        # breakpoint()
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while qq.size() > 0:
            # dequeue/pop first vertex
            path = qq.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.push(new_path)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # helper function for recursion
        def visit(vert):
            self.color[vert] = 'gray'
            print(vert)
            for neighbor in self.get_neighbors(vert):
                if self.color[neighbor] == 'white':
                    visit(neighbor)
            self.color[vert] = 'black'


        # set all nodes color to white
        for vert in self.vertices:
            self.color[vert] = 'white'
        # set current vert's color to gray
        self.color[starting_vertex] = 'gray'
        # print the vertex
        print(starting_vertex)
        # begin recursion
        for neighbor in self.get_neighbors(starting_vertex):
            if self.color[neighbor] == 'white':
                visit(neighbor)
        self.color[starting_vertex] = 'black'

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        qq.enqueue([starting_vertex])
        # breakpoint()
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while qq.size() > 0:
            # dequeue/pop first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                if path[-1] == destination_vertex:
                    return path
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        qq = Stack()
        qq.push([starting_vertex])
        # breakpoint()
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while qq.size() > 0:
            # dequeue/pop first vertex
            path = qq.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                if path[-1] == destination_vertex:
                    return path
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def visit(path):
            final_path = [1]
            if path[-1] == destination_vertex:
                return path
            self.color[path[-1]] = 'gray'
            for neighbor in self.get_neighbors(path[-1]):
                if self.color[neighbor] == 'white':
                    new_path = list(path)
                    new_path.append(neighbor)
                    final_path = visit(new_path)
            self.color[path[-1]] = 'black'
            return final_path

        # set all nodes color to white
        for vert in self.vertices:
            self.color[vert] = 'white'
        # set current vert's color to gray
        self.color[starting_vertex] = 'gray'
        # begin recursion
        for neighbor in self.get_neighbors(starting_vertex):
            if self.color[neighbor] == 'white':
                path = [starting_vertex, neighbor]
                final_path = visit(path)
                if final_path[-1] == destination_vertex:
                    return final_path
        self.color[starting_vertex] = 'black'
        return final_path

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
