"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import copy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Does the vertex already exist?
        if vertex_id in self.vertices:
            # passed vertex already exists
            print("vertex {vtx} already exists".format(vtx=vertex_id))
            return False

        # New vertex, add to the vertices dict
        self.vertices[vertex_id] = {}
        return vertex_id

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Do the passed vertices exist in the graph?
        if v1 not in self.vertices or v2 not in self.vertices:
            # one or both vertices do not exist in the graph
            print("vertex {vtx1} or {vtx1} do not exist in the graph".format(
                vtx1=v1,
                vtx2=v2))
            return False

        # Both vertices exist.  Add an edge from v1 to v2
        # Does this vertex have any existing edges (or is this to be added)?
        if len(self.vertices[v1]) == 0:
            # No existing edges for v1, add the first one
            self.vertices[v1] = {v2}
            return v2
        
        # Does the edge already exist?
        if v2 in self.vertices[v1]:
            # edge already exists, nothing to do
            print("Edge: {vtx1} to {vtx2} already exists".format(vtx1=v1, vtx2=v2))
            return False

        # Add v2 as an edge connection to v1
        self.vertices[v1].add(v2)
        return v2

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # Does the vertex exist in the graph?
        if vertex_id not in self.vertices:
            # vertex not found, return None
            print("vertex {vtx} not found".format(vtx=vertex_id))
            return None

        # Return neighbors of the vertex
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Validate the passed parameter: is the passed vertex valid?
        if starting_vertex not in self.vertices:
            # vertex not found, nothing to do
            print("vertex {vtx} not found, nothing to do".format(vtx=starting_vertex))
            return False

        # Define a vertex search queue - "vertexes to traverse"
        vert_queue = Queue()
        # Define a vertex status map - "status of the vertex's traversal"
        vert_status = {}

        # Set the initial status for each vertex as "not_started"
        for vtx in self.vertices:
            vert_status[vtx] = "search_not_started"

        # Start the breadth search with the passed vertex
        vert_status[starting_vertex] = "search_started"
        # Place the start vertex in our queue
        vert_queue.enqueue(starting_vertex)

        # Process while there are vertices in the queue
        while vert_queue.size() != 0:
            tmp_vtx = vert_queue.peek(0)  # access the top of the queue (but don't dequeue)
            if tmp_vtx == None:
                print("error taking a peek at the queue")
                quit()

            # Iterate through the current vertex's neighbors
            #    and initate the search process on those vertices
            for vrtx in self.get_neighbors(tmp_vtx):
                if vert_status[vrtx] == "search_not_started":
                    vert_status[vrtx] = "search_started"
                    vert_queue.enqueue(vrtx)

            # Dequeue the current vertex
            vert_queue.dequeue()
            print(tmp_vtx)
            vert_status[tmp_vtx] = "search_completed"
            
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Validate parameter: is the passed vertex valid?
        if starting_vertex not in self.vertices:
            # vertex not found, nothing to do
            print("vertex {vtx} not found, nothing to do".format(vtx=starting_vertex))
            return False

        # Define a vertex search queue - "vertexes to search"
        vert_stack = Stack()
        # Define a vertex search status map - "status of the vertex's search"
        vert_status = {}

        # Set the search status for each vertex as "not_started"
        for vtx in self.vertices:
            vert_status[vtx] = "search_not_started"

        # Place the start vertex in our stack
        vert_stack.push(starting_vertex)

        # Process while there are vertices in the stack
        while not vert_stack.is_empty():
            # Pop the vertex at the top of the stack
            tmp_vtx = vert_stack.pop()
            # Indicate we have started the search on the popped vertex
            vert_status[tmp_vtx] = "search_started"

            # Print out the vertex
            print(tmp_vtx)
            # Indicate we have completed the search on the popped vertex
            vert_status[tmp_vtx] = "search_completed"

            # Push the current vertex's child vertices
            if len(self.vertices[tmp_vtx]) != 0:
                # Push this vertex's children on the stack
                lst_set = list(self.vertices[tmp_vtx])
                lst_set.reverse()
                for v_elm in lst_set:
                    # Has this vertex been processed?
                    if vert_status[v_elm] != "search_not_started":
                        # This vertex has already been processed - skip
                        continue

                    # Vertex to be processed, push on the stack
                    vert_stack.push(v_elm)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Define a vertex search status map - "status of the vertex's search"
        vert_status = {}

        # proc_vtx prints a graph vertex and it's children in a DFT sequence
        def proc_vtx(vtx):
            # print the vertex
            print(vtx)
            # indicate that the vertex has been printed/processed
            vert_status[vtx] = "search_completed"

            # Iterate through the vertex's children
            tmp_lst = list(self.vertices[vtx])
            for v in tmp_lst:
                # has the vertex been processed?
                if vert_status[v] != "search_not_started":
                    # vertex already in process, skip
                    continue

                # process/print the vertex
                proc_vtx(v)

        # Set the search status for each vertex as "not_started"
        for vtx in self.vertices:
            vert_status[vtx] = "search_not_started"

        # Process the passed in vertex
        proc_vtx(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Validate parameter: is the passed vertex valid?
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            # one or both vertices not found, nothing to do
            print("vertex {vtx} not found, nothing to do".format(vtx=starting_vertex))
            return False
        
        # Set up working objects
        set_vrtx_inspected = set()  # set of vertices already inspected/visited

        # Define a vertex search queue
        que_vert = Queue()  # queue of path lists

        # Place the start vertex in our queue
        que_vert.enqueue(list([starting_vertex]))

        # Process while there are vertex paths in the queue
        while que_vert.size() != 0:
            iter_path = que_vert.dequeue()  # dequeue the next path to be processed
            curVtx = iter_path[-1]

            # Have we found the destination node?
            if curVtx == destination_vertex:
                # Yes. Found destination, return path
                return iter_path

            # Have we inspected the current vertex before
            if curVtx not in set_vrtx_inspected:
                set_vrtx_inspected.add(curVtx)        # flag the current vertex as inspected

                # Process the current vertex's neighbors
                for v_nbr in self.vertices[curVtx]:
                    # enqueue a new potential search path
                    lst_poss_path = copy.deepcopy(iter_path)
                    # add the current neighbor to the this potential path
                    lst_poss_path.append(v_nbr)

                    # add this new potential path to the queue
                    que_vert.enqueue(lst_poss_path)

        # Destination not found - return empty list
        return []
        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Validate the passed parameter: is the passed vertex valid?
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            # one or both vertices not found, nothing to do
            print("vertex {vtx} not found, nothing to do".format(vtx=starting_vertex))
            return False

        # Set up working objects
        set_vrtx_inspected = set()  # set of vertices already inspected/visited

        # Define a vertex search queue
        stk_vert = Stack()  # queue of path lists

        # Place the initial path in the queue - path that includes includes on the starting vertex
        stk_vert.push(list([starting_vertex]))

        # Process while there are vertex paths in the queue
        while stk_vert.size() != 0:
            iter_path = stk_vert.pop()  # pop the next path to be processed
            curVtx    = iter_path[-1]   # grab the last vertex in the current path 

            # Have we found the destination node?
            if curVtx == destination_vertex:
                # Yes. Found destination, return path
                return iter_path

            # Have we inspected the current vertex before
            if curVtx not in set_vrtx_inspected:
                set_vrtx_inspected.add(curVtx)        # flag the current vertex as inspected

                # Process the current vertex's neighbors
                for v_nbr in self.vertices[curVtx]:
                    # enqueue a new potential search path
                    lst_poss_path = copy.deepcopy(iter_path)
                    # add the current neighbor to the this potential path
                    lst_poss_path.append(v_nbr)

                    # add this new potential path to the queue
                    stk_vert.push(lst_poss_path)      

        # Destination not found - return empty list
        return []

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        def proc_path(pth):
            # have we found the destination vertex?
            curVtx = pth[-1]
            if curVtx == destination_vertex:
                # Yes. Return the current path
                return pth

            set_vrtx_inspected.add(curVtx)

            # Process the current vertex's neighbors
            for v_nbr in self.vertices[curVtx]:
                # already processed this vertex?
                if v_nbr in set_vrtx_inspected:
                    # yes skip
                    continue

                # construct a new potential search path
                lst_poss_path = copy.deepcopy(pth)
                # add the current neighbor to the this potential path
                lst_poss_path.append(v_nbr)

                # recursively call proc_path with the potential path
                result = proc_path(lst_poss_path)
                if len(result) > 0:
                    return result

            return []
        
        # Validate parameter: is the passed vertex valid?
        if starting_vertex not in self.vertices or destination_vertex not in self.vertices:
            # one or both vertices not found, nothing to do
            print("vertex {vtx1} or {vtx2} not found, nothing to do".format(
                vtx1=starting_vertex,
                vtx2=destination_vertex))
            return False

        # Set up working objects
        set_vrtx_inspected = set()  # set of vertices already inspected/visited

        # Trigger the search with the starting vertex path and return the results
        ret_val =  proc_path(list([starting_vertex]))
        return ret_val

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
    # TODO: LEFT OFF HERE
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    graph.dfs(1, 6)
    print("graph.dfs_recursive...")
    print(graph.dfs_recursive(1, 6))
