from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph

def main(num_vertices=8, num_edges=8):
    graph = Graph()
    for num in range(num_vertices):
        graph.add_vertex(str(num))

    verts = []
    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        while vertices in verts:
            vertices = sample(graph.vertices.keys(), 2)
        graph.add_edge(str(vertices[0]), str(vertices[1]))
        verts.append(vertices)
        verts.append(vertices[::-1])

    print (graph.vertices)
    graph.search()
    print (graph.vertices)
    graph.search('depth')

    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        if NUM_EDGES > (NUM_VERTICES * (NUM_VERTICES-1)) / 2:
            print('Too many edges, creating default graph')
            main()
        else:
            main(NUM_VERTICES, NUM_EDGES)
    else:
        main()