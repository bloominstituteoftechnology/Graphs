"""
Simple graph implementation
"""

from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = []

    def add_edge(self, v1, v2):
        self.vertices[v1].append(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Create an empty que and add the starting_vertex 
        q = Queue()
        q.enqueue([starting_vertex])
        # Create an empty set to track visited verticies
        seen = set()
        # while the que is not empty: 
        while q.size() != 0:
            verts = q.dequeue()
            for vert in verts:
                if vert not in seen:
                    seen.add(vert)
                    q.enqueue(self.get_neighbors(vert))
        print(seen)
        


    def dft(self, starting_vertex):
        # Create an empty que and add the starting_vertex 
        s = Stack()
        s.push([starting_vertex])
        # Create an empty set to track visited verticies
        seen = set()
        # while the que is not empty: 
        while s.size() != 0:
            verts = s.pop()
            for vert in verts:
                if vert not in seen:
                    seen.add(vert)
                    s.push(self.get_neighbors(vert))
        print(seen)
        """
    def dft_recursive(self, seen):
        if type(seen) != set:
            seen = self.dft_recursive(set([seen]))
        
        if len(seen) != len(self.vertices):
            neighbors = set( [] )
            for el in seen:
                return
            unseen = seen.difference(neighbors)
            if (unseen):
                seen = seen.union(unseen)
                seen.union(self.dft_recursive(seen))


        return seen
        """
    def dft_recursive(self, seen):
        if type(seen) != list:
            seen = self.dft_recursive( [set([seen]), set()] )
            return seen[1]

        seen[1] = seen[1].union(seen[0])
        if len(seen[0]) != len(self.vertices):

            for vert in seen[1]:
                set(self.get_neighbors(vert))

            return self.dft_recursive(seen)
        """
        if len(seen[0]) != len(self.vertices):
            neighbors = set( [] )
            for el in seen:
                return
            unseen = seen.difference(neighbors)
            if (unseen):
                seen = seen.union(unseen)
                seen.union(self.dft_recursive(seen))
        """
        print(seen[1])

        return seen
        """
        for neighbor in neighbors:
            if neighbor not in vert:
                print(f'{neighbor} is a neighbor of {last_vert_in_set}')
                vert.add(neighbor)
                print(vert)
                #return vert
                vert =
        """

                        
        """
        if len(vert) == len(self.vertices): 
            print("yes")
            return vert
        """

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

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
