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
        # set up queue
        q = Queue()
        traversed = []
        q.enqueue(starting_vertex)
        # while the queue still has values in it
        while q.size() > 0:
            cur_val = q.dequeue()
            traversed.append(cur_val)
            for val in self.vertices[cur_val]:
                # make sure we've not gone that way
                if val not in traversed:
                    q.enqueue(val)
            print(cur_val)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # set up stack
        s = Stack()
        traversed = [starting_vertex]
        s.push(starting_vertex)
        # while the stack still has values in it
        while s.size() > 0:
            cur_val = s.pop()
            print(cur_val)
            for val in self.vertices[cur_val]:
                # make sure we've not gone that way
                if val not in traversed:
                    traversed.append(val)
                    s.push(val)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # recusive function
        def recurse(graph, traversed, vertex):
            # endpoints: already been there
            if vertex in traversed:
                return
            # work: print the vertex,
            #       mark where we've been
            print(vertex)
            if vertex not in traversed:
                traversed.append(vertex)
            # recurse
            for val in graph[vertex]:
                recurse(graph, traversed, val)
        
        recurse(self.vertices, [], starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # set up queue
        q = Queue()
        # reverse lookup table
        traversed = {1: None}
        cur_val = None
        q.enqueue(starting_vertex)
        # while the queue still has values in it
        while cur_val != destination_vertex:
            cur_val = q.dequeue()
            for val in self.vertices[cur_val]:
                # make sure we've not gone that way
                if val not in traversed:
                    traversed[val] = cur_val
                    q.enqueue(val)
        # map our way back
        returnlist = []
        while cur_val is not None:
            returnlist.append(cur_val)
            cur_val = traversed[cur_val]
        # reverse the list and return it
        returnlist.reverse()
        return returnlist


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # set up stack
        s = Stack()
        # reverse lookup table
        traversed = {1: None}
        cur_val = None
        s.push(starting_vertex)
        # while the queue still has values in it
        while cur_val != destination_vertex:
            cur_val = s.pop()
            for val in self.vertices[cur_val]:
                # make sure we've not gone that way
                if val not in traversed:
                    traversed[val] = cur_val
                    s.push(val)
        # map our way back
        returnlist = []
        while cur_val is not None:
            returnlist.append(cur_val)
            cur_val = traversed[cur_val]
        # reverse the list and return it
        returnlist.reverse()
        return returnlist

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # recursive function
        def recurse(graph, traversed, goal, vertex):
            # endpoints: already been there or goal found
            if vertex in traversed:
                # return none to show dead end
                return None
            if vertex == goal:
                # return list to append onto to map way back
                return [vertex]
            # work: mark where we've been
            if vertex not in traversed:
                traversed.append(vertex)
            # recurse: return the string if found
            for val in graph[vertex]:
                result = recurse(graph, traversed, goal, val)
                if result is not None:
                    result.append(vertex)
                    return result
            # catch, return nothing if all dead ends
            return None
        
        # get result from recursion and reverse
        result = recurse(self.vertices, [], destination_vertex, starting_vertex)
        result.reverse()
        return result


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