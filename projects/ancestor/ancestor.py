# Imports
from collections import deque
import copy
from util import Stack, Queue  # These may come in handy

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
            # passed vertex already exists?
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
        # Does this vertex have any existing edges (or is this the first edge for this vertex)
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
        # Does the vertex exist in the graph
        if vertex_id not in self.vertices:
            # vertex not found, return None
            print("vertex {vtx} not found".format(vtx=vertex_id))
            return None

        # Return neighbors of the vertex
        return self.vertices[vertex_id]

    def has_neighbors(self, vertex_id):
        """
        Indicate if a vertex has neighbors
        """
        # Does the vertex exist in the graph
        if vertex_id not in self.vertices:
            # vertex not found, return None
            print("vertex {vtx} not found".format(vtx=vertex_id))
            return False

        # Return neighbors of the vertex
        if len(self.vertices[vertex_id]) != 0:
            return True

        return False

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
   
    # get_lineage_ends given a starting vertex (person) will return
    #    a list of ancestors where the line ends (no known parents)
    def get_lineage_ends(self, starting_vertex):
        """
        Returns the ancestors that represent the end of the starting 
        vertex's lineage (ancestors with no known parents) 
        """
        ret_ending_ancestors = []

        # proc_vtx finds a vertex's parent until the end of the line
        def proc_vtx(vtx):
            """
            Recursively find a vertex's parent until the end of the line
            """
            # Are we at the end of the line (person with no known parents)?
            if len(self.vertices[vtx]) == 0:
                # Yes, add this to our list of line ending ancestors
                ret_ending_ancestors.append(vtx)
                # Base case: return
                return

            # Have at least one parent, iterate through this person's parents and 
            #   continue looking for the lineage end
            for rent in self.vertices[vtx]:
                proc_vtx(rent)

            return

        # Process the passed in vertex
        proc_vtx(starting_vertex)
        return ret_ending_ancestors

def earliest_ancestor(ancestors, starting_node):
    """
    Returns the furthest ancestor of the passed vertex
    """
    # Instantiate a graph object
    my_graph = Graph()
    # Instantiate a stack object
    my_stack = deque()

    #* Invert ancestors from "parent->child" to "child->parent"
    inv_ancestors = list([])
    set_peeps     = set()
    for tp in ancestors:
        tmp_tp = (tp[1], tp[0])         # invert from p>c to c>p
        inv_ancestors.append(tmp_tp)    # create a list of c>p tuples
        set_peeps.add(tmp_tp[0])        # create a set of unique people
        set_peeps.add(tmp_tp[1])

    #* Construct a child -> parent oriented graph object
    # Add vertices to our graph object
    for vtx in set_peeps:
        my_graph.add_vertex(vtx)

    # Add edges (c->p) to the graph
    for tmp_t in inv_ancestors:
        my_graph.add_edge(tmp_t[0], tmp_t[1])

    # Is the child an orphan?
    if not my_graph.has_neighbors(starting_node):
        return -1   

    #* Analyze lineage
    # Determine the person's lineage ending vertices
    end_rents = my_graph.get_lineage_ends(starting_node)

    # Iterate through each lineage and determine which ancestral line is longer
    ret_lineage  = []
    for i, vtx in enumerate(end_rents):
        # Return the path from the starting person to the end of the line
        tmp_path = my_graph.bfs(starting_node, vtx)
        
        # Store the longest lineage path
        if len(ret_lineage) == 0:
            # encountering the first path
            ret_lineage = copy.deepcopy(tmp_path)
            continue
        elif len(ret_lineage) == len(tmp_path):
            # current path length is <= saved path length
            #    select the path the lower ancestor value
            if tmp_path[-1] <= ret_lineage[-1]:
                ret_lineage = copy.deepcopy(tmp_path)
                continue
        elif len(tmp_path) > len(ret_lineage):
                # current path length is longer than the saved path length
                ret_lineage = copy.deepcopy(tmp_path)

    #* Done searching, return the furthest ancestor
    return ret_lineage[-1]

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print("The longest ancestral lineage from {node} is: {pth}".format(
            node=3,
            pth=earliest_ancestor(test_ancestors, 3)
        ))
