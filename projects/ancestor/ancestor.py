
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for vertex_1, vertex_2 in ancestors:
        graph.add_vertex(vertex_1)
        graph.add.add_vertex(vertex_2)

        //add edge to both vetrices
        for vertex_1, vertex_2 in ancestors:
            graph.add_edge(vertex_1,vertex_2)

        target_vertex = None
        