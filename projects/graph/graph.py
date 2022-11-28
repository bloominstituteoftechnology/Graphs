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
        # First, make a queue and 'enqueue' your start node
        qu = Queue()
        qu.enqueue(starting_vertex)

        # Next we need a set to track the nodes that we've visited
        seen = set()

        # Now let's algorithm
        # We only work while the queue isn't empty
        while qu.size() > 0:

            # Dequeue from the front of the line (that's how queues work)
            # This will be our current node
            current = qu.dequeue()

            # Have we visited our current node? We only work with nodes we haven't seen yet
            if current not in seen:

                # Mark it as seen and print
                seen.add(current)
                print(current)

                # We also need its neighbors
                neighbors = self.get_neighbors(current)

                # Now we iterate over it's neighbors and enqueue them
                for neighbor in neighbors:
                    qu.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # First make a stack and 'push' your starting node to the top of the stack
        st = Stack()
        st.push(starting_vertex)

        # Make a set to keep track of nodes we've seen
        seen = set()

        # We work while the stack is not empty
        while st.size() > 0:

            # 'pop' off the node at the top of the stack
            # This is our current node
            current = st.pop()

            # Have we seen this node, we only work with nodes we haven't seen as yet
            if current not in seen:

                # Mark it as seen and print
                seen.add(current)
                print(current)

                # Get current's neighbors
                neighbors = self.get_neighbors(current)

                # Now itereate over neighbors 
                for neighbor in neighbors:

                    # Add them to the stack
                    st.push(neighbor)


    # Base case
    # Progress towards the base case
    # Call itself
 
    def dft_recursive(self, starting_vertex, seen=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if seen == None:

            # seen is empty so we need to make a set
            seen = set()
        
        # We only work with nodes we haven't seen
        if starting_vertex not in seen:
            print(starting_vertex)
            seen.add(starting_vertex)
        
            # Get neighbors
            neighbors = self.get_neighbors(starting_vertex)

            # Base case is no neighbors:
            if len(neighbors) == 0:
                return seen
            
            # If not the base case, then we iterate and recurse towards base case
            for neigbor in neighbors:
                self.dft_recursive(neigbor, seen)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # We will bft to the destination vertex then return the path we took

        # First, make a queue 
        qu = Queue()
        # Next we need a set to track the nodes that we've visited
        seen = set()
        # And make our path that we'll be adding nodes to
        path = list()

        # Next we need to add the starting vertex to our path
        path.append(starting_vertex)
        # ... and add the enqueue the path to our queue
        qu.enqueue(path)

        # Again, we only work while the queue isn't empty
        while qu.size() > 0:

            # Dequeue from the front of the line (that's how queues work)
            # This will be added to our current path
            currentpath = qu.dequeue()
            # And the last node in the path is our current node
            currentnode = currentpath[-1]

            # Is our current node the destination? If so return the current path and end traversal
            if currentnode == destination_vertex:
                return currentpath
            
            # If not we need to keep on traversing
            # Have we visited our current node? We only work with nodes we haven't seen yet
            if currentnode not in seen:

                # Mark it as seen and get its neighbors
                seen.add(currentnode)
                neighbors = self.get_neighbors(currentnode)

                # Now we iterate over it's neighbors
                for neighbor in neighbors:

                    # Every neighbor leads to a new path, and we have to keep track
                    # Every neighbor also has the exact same previous steps, so we can copy
                    neighborpath = currentpath.copy()
                    # We now add the neighbor to it's new path
                    neighborpath.append(neighbor)
                    # And we enqueue the neighborpath to our queue to continue our traversal
                    qu.enqueue(neighborpath)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # We will dft to the destination vertex then return the path we took
        # First make a stack, path list and seen set
        st = Stack()
        path = list()
        seen = set()

        # Add the starting vertex to the path, and pus the path to the stack
        path.append(starting_vertex)
        st.push(path)

        # We work while the stack is not empty
        while st.size() > 0:

            # 'pop' off the path at the top of the stack
            currentpath = st.pop()
            # The current node is the last item in current path
            currentnode = currentpath[-1]

            # Is the current node our destination? if so return the current path
            if currentnode == destination_vertex:
                return currentpath

            # If not we have to traverse
            # Have we seen this node, we only work with nodes we haven't seen as yet
            if currentnode not in seen:

                # Mark it as seen get it's neighbors
                seen.add(currentnode)
                neighbors = self.get_neighbors(currentnode)

                # Now itereate over neighbors 
                for neighbor in neighbors:
                    # Again, each neighbor is a new path with the same previous steps
                    # So each neighbor gets its own copy of the path
                    neighborpath = currentpath.copy()
                    neighborpath.append(neighbor)

                    # Lastly we push the path to the stack
                    st.push(neighborpath)
        

    def dfs_recursive(self, starting_vertex, destination_vertex, seen=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Base case
        # Progress towards the base case
        # Call itself

        if seen == None:

            # seen is empty so we need to make a set
            seen = set()
        
        if path == None:

            # path is empty so we make a list
            path = list()

        # We only work with nodes we haven't seen
        if starting_vertex not in seen:
            seen.add(starting_vertex)
            path.append(starting_vertex)

        # Is the starting vertex the same as the destination? if so return path
        if starting_vertex == destination_vertex:
            return path

        # If not Get neighbors
        neighbors = self.get_neighbors(starting_vertex)

        # Now we iterate over each neighbor
        # Each new neighbor is a new path that we must traverse
        for neighbor in neighbors:
            if neighbor not in seen:
                neighborpath = self.dfs_recursive(neighbor, destination_vertex, seen, path)

                # Note, I had a lot of trouble closing off the recursion. Thanks Tim
                if neighborpath is not None:
                    return neighborpath
        
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/BloomInstituteOfTechnology/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
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
