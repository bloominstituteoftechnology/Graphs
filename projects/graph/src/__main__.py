from sys import argv

from draw import BokehGraph
from graph import Graph, Vertex

from random import sample

def main(num_vertices=8, num_edges=8, draw_components=False):
    '''build and show a random graph -- DEMO'''
    graph = Graph()
    #add appropriate num of vertices
    for _ in range(num_vertices):
        graph.add_vertex(Vertex(label=str(_)))
    # add appropriate num of edges

    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        #TODO check if edge exists
        graph.add_edge(vertices[0], vertices[1])
    bg = BokehGraph(graph)
    print(bg.plot)
    print(bg.pos)
    bg.show()

if __name__ == '__main__':
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPONENTS = bool(int(argv[3]))
        main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
    else:
        main() #accepts defaults