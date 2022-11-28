import sys
sys.path.insert(1, '/Users/ShawnJames/Developer/Github/Graphs/projects/graph') #change location to wherever graph file is located locally
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
        graph = Graph()
        # add vertexes
        for vertex_1, vertex_2 in ancestors:
            graph.add_vertex(vertex_1)
            graph.add_vertex(vertex_2)
        # add edges
        for vertex_1, vertex_2 in ancestors:
            graph.add_edge(vertex_1, vertex_2)

        targetVertex = None
        longestPath = 1
        for vertex in graph.vertices:
            # vertex is start, starting_node is destination
            path = graph.dfs(vertex, starting_node)
            if path:
                if len(path) > longestPath:
                    longestPath = len(path)
                    targetVertex = vertex
            elif not path and longestPath == 1:
                targetVertex = -1

        return targetVertex
    
    
    ## In file quick-test ##
    
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

'''
     10
 /
1   2   4  11
 \ /   / \ /
    3   5   8
     \ / \   \
        6   7   9
'''

print(earliest_ancestor(test_ancestors, 1))