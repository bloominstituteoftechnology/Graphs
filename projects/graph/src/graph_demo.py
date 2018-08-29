
#!/usr/bin/python
from draw import BokehGraph
from graph import Graph, Vertex
"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv

# def draw_random_graph( graph, vertices, edges ):
#     pass

def main():
    graph = Graph()
    graph.insert_vertex('1')
    graph.insert_vertex('2')
    graph.insert_vertex('3')
    graph.insert_edge('1', '2')
    graph.insert_edge('1', '3')
    print(graph.vertices)    
    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    # TODO - parse argv
    main()