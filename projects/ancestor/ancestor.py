from collections import deque

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
        else:
            raise IndexError("That vertex does not exist")
 
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        


def earliest_ancestor(ancestors, starting_node):

    # Build the fam tree graph

    fam = Graph()
    for pair in ancestors:
        fam.add_vertex(pair[0])
        fam.add_vertex(pair[1])
        fam.add_edge(pair[1], pair[0])
 


    #initialize
    ancestor = starting_node
    generations = 0
    stack = deque([(ancestor, generations)])
    
    while len(stack) > 0:
        (child, childs_generation) = stack.pop()

        if childs_generation > generations:
            ancestor = child
            generations = childs_generation

        elif childs_generation == generations and child < ancestor:
           ancestor = child

        parents = fam.get_neighbors(child)
        stack.extend([(parent, childs_generation + 1) for parent in parents])
        

    return -1 if generations == 0 else ancestor