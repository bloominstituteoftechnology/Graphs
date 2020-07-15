from util import Stack


class Graph:
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
            raise IndexError('that vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        dfs_path = Stack()
        dfs_path.push([starting_vertex])
        visited_vertices = set()
        while dfs_path.size() > 0:
            curr_path = dfs_path.pop()
            curr_path_last_vertex = curr_path[-1]
            if curr_path_last_vertex not in visited_vertices:
                if curr_path_last_vertex == destination_vertex:
                    return curr_path
                else:
                    visited_vertices.add(curr_path_last_vertex)
                    neighbors = self.get_neighbors(curr_path_last_vertex)
                    for neighbor in neighbors:
                        curr_path_copy = curr_path[:]
                        curr_path_copy.append(neighbor)
                        dfs_path.push(curr_path_copy)
                        
                        
def earliest_ancestor(ancestors, starting_node):
    # create graph and create path
    ancestor_graph = Graph()
    paths = []
    
    # add verticies
    for vertex in range(0, 20):
        ancestor_graph.add_vertex(vertex)
    
    # add edges
    for ancestor in ancestors:
        ancestor_graph.add_edge(ancestor[0], ancestor[1])
        
    
    # add path to ancestor paths
    for vertex in ancestor_graph.vertices:
        if ancestor_graph.dfs(vertex, starting_node) is not None and len(ancestor_graph.dfs(vertex, starting_node)) > 0:
            paths.append(ancestor_graph.dfs(vertex, starting_node))
            
    if len(paths) == 1:
        return -1
     
    # find earliest neighbor
    start_path = paths[0]
    for path in paths:
        if len(path) > len(start_path) or len(start_path) and path[0] < start_path[0]:
            start_path = path

    return start_path[0]         
    