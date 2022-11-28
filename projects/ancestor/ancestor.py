
class Anc_Graph():
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        parents = set()
        children = set()
        self.vertices[vertex_id] = [parents, children]
        
    def add_edge(self, parent, child):
        if parent in self.vertices and child in self.vertices:

            self.vertices[child][0].add(parent)
            self.vertices[parent][1].add(child)
        elif child in self.vertices:
            self.add_vertex(parent)
            self.vertices[parent][1].add(child)
            self.vertices[child][0].add(parent)
        elif parent in self.vertices:
            self.add_vertex(child)
            self.vertices[parent][1].add(child)
            self.vertices[child][0].add(parent)
        else:
            self.add_vertex(parent)
            self.add_vertex(child)
            self.vertices[parent][1].add(child)
            self.vertices[child][0].add(parent)
    
    def get_parents(self, v):
        return self.vertices[v][0]

def earliest_ancestor(ancestors, starting_node):
    anc_tree = Anc_Graph()
    # fill graph
    for i in range(len(ancestors)):
        anc_tree.add_edge(ancestors[i][0], ancestors[i][1])

    # account for no ancestors
    if anc_tree.get_parents(starting_node) == set():
        return -1
    # create visited set to keep track of visited nodes
    visited = set()
    # longest_paths to keep track of longest paths, and longest paths of same length
    longest_paths = [[starting_node]]
    
    s = Stack()
    s.push([starting_node])
    while s.size() > 0:
        new_path = s.pop()
        last_node = new_path[-1]
        if last_node not in visited:
            visited.add(last_node)
            if len(new_path) > len(longest_paths[0]):
                longest_paths = [new_path]
    
            elif len(new_path) == len(longest_paths[0]):
                longest_paths.append(new_path)
            for parent in anc_tree.get_parents(last_node):
                path_copy = new_path.copy()
                path_copy.append(parent)
                s.push(path_copy)
    # check for duplicate longest paths
    if len(longest_paths) > 1:
        low_id = float('inf')
        for i in range(len(longest_paths)):
            if longest_paths[i][-1] < low_id:
                low_id = longest_paths[i][-1]
        
        return low_id
    # if no duplicates, return the last index of longest path
    
    return longest_paths[0][-1]