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
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set ()

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
        #create an empty queue and enqueue with current node neighbours
        queue = Queue()
        queue.enqueue({
            'current_vertex' : starting_vertex,
            'edges': [starting_vertex] #value of that vertex
            })
        #create a set of visited vertices
        visited_vertices =set ()
        #while queue is not empty
        while queue.size() >0:
            #get current vertex edges (dequeue from queue)
            current_obj= queue.dequeue()
            current_edges = current_obj['edges'] 
            current_vertex = current_obj['current_vertex']
            #check current vertex is not in visited vertex list
            if current_vertex not in visited_vertices:
                # Mark as visited vertices
                visited_vertices.add(current_vertex)
                for neighbour_vertex in self.get_neighbors(current_vertex):
                    new_edges = list(current_edges)
                    new_edges.append(neighbour_vertex)
                    queue.enqueue({
                        'current_vertex' : neighbour_vertex,
                        'edges' : new_edges
                    })
        return visited_vertices


        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO

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
        #create an empty queue and enqueue with current node neighbour
        queue = Queue()
        queue.enqueue({
            'current_vertex': starting_vertex,
            'path' : [starting_vertex]
        })
        # create a list of visited vetex
        visited_vertex = set()
        #while queue is not empty
        while queue.size() >0:
            #get a current obj path(dequeue it from queue)
            current_obj = queue.dequeue()
            current_vertex = current_obj['current_vertex']
            current_path = current_obj['path']
            #compare the current vertex with destination vertex
            if current_vertex  == destination_vertex:
                return current_path
            #check if the vertex in the visited_vetex list
            if current_vertex  not in visited_vertex:
                #add th vertex in the visted vertex list
                visited_vertex.add(current_vertex)
                #get all the neighbours of the current_vertex
                for neighbour in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbour)
                    # enqueu the neighbour in the queue
                    queue.enqueue({
                        'current_vertex': neighbour,
                        'path': new_path
                    })

                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

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
    print(graph.bft(1))

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
