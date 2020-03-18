from graph import Graph
from util import Stack
def earliest_ancestor(ancestors, starting_node):
    # ancestor_graph = Graph()
    # steps = -1
    # ancestor_id = None
    # for ancestor in ancestors:
    #     if ancestor[0] not in ancestor_graph.vertices:
    #         ancestor_graph.add_vertex(ancestor[0])
    #     if ancestor[1] not in ancestor_graph.vertices:
    #         ancestor_graph.add_vertex(ancestor[1])
    #     ancestor_graph.add_edge(ancestor[0], ancestor[1])
    # for vertex in ancestor_graph.vertices:
    #     if vertex != starting_node:
    #         path = ancestor_graph.dfs(vertex, starting_node)
    #         if path is not None and len(path) > steps:
    #             steps = len(path)
    #             ancestor_id = path[0]

    # if steps > 0:
    #     return ancestor_id
    # else:
    #     return steps
    ancestor_dict = {}
  

    for ancestor in ancestors:
        key = ancestor[1]
        value = ancestor[0]
        if key in ancestor_dict.keys():
            ancestor_dict[key].add(value)
        else:
            ancestor_dict[key] = set()
            ancestor_dict[key].add(value)
    if starting_node not in ancestor_dict:
        return -1
    def dfs(starting_vertex):
        s = Stack()
        start_path = []
        paths = []
        start_path.append(starting_vertex)
        s.push(start_path)
        while s.size() > 0:
            v = s.pop()
            if len(v) > len(paths):
                paths = [value for value in v]
            if len(v) == len(paths) and v[-1] < paths[-1]:
                paths = [value for value in v]
            last_value = v[-1]
            if last_value in ancestor_dict.keys():
                values = ancestor_dict[last_value]
                for value in values:
                    copy= [node for node in v]
                    copy.append(value)
                    s.push(copy)
        return paths[-1]
    
    return_value = dfs(starting_node)
    return return_value


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)
    