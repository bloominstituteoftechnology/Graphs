
#!/usr/bin/python
from draw import BokehGraph
from graph import Graph, Vertex
"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from random import randint
def draw_random_graph( graph, vertices, edges ):
    # create vertices range from 0 to vertices
    # for loop 0 -> vertices:
    #     graph.insert_vertext(str(i))
    for i in range(int(vertices)):
        graph.insert_vertex(str(i))
    # for i in range(edges):
        # variable completed = edges
        # pick a random number in range(edges)
        # connect it to a random edge
        # if other random number == current random number
            # pick again and add edge
        # completed -= 1
    # so maybe a while loop, based on completed > 0
    completed = int(edges)
    
    while completed > 0:
        rand1 = str(randint(0, int(vertices)))
        rand2 = str(randint(0, int(vertices)))
        if rand1 == rand2:
            continue
        else:
            print("rand1:", rand1)
            print("rand2:", rand2)
            graph.insert_edge_bi_directional(rand1, rand2)
            completed -= 1

def main(vertices=5, edges=3):
    graph = Graph()
    # graph.insert_vertex('1')
    # graph.insert_vertex('2')
    # graph.insert_vertex('3')
    # graph.insert_vertex('4')
    # graph.insert_edge_bi_directional('1', '2')
    # graph.insert_edge_bi_directional('1', '3')
    draw_random_graph(graph, vertices, edges)
    print(graph.vertices)
    print("bfs search", graph.breadth_first_search('1'))
    print("connected components", graph.connected_components()) 
    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    # TODO - parse argv
    if len(argv) > 1:
       main(argv[1], argv[2])
    else:
        main()