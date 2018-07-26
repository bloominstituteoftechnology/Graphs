from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph

def main(num_vertices=8, num_edges=8, test=0):
    graph = Graph()

    if test == 1:
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_vertex('D')
        graph.add_vertex('E')
        graph.add_vertex('F')
        graph.add_vertex('G')

        graph.add_edge('A', 'B')
        # graph.add_edge('A', 'D')
        # graph.add_edge('A', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('D', 'G')
        # graph.add_edge('G', 'F')
        graph.add_edge('E', 'F')

        # print (graph.vertices)
        # print (graph.search())

    if test == 2:
        graph.add_vertex('0')
        graph.add_vertex('1')
        graph.add_vertex('2')
        graph.add_vertex('3')
        graph.add_vertex('4')
        graph.add_vertex('5')
        graph.add_vertex('6')

        graph.add_edge('0', '1')
        graph.add_edge('0', '2')
        graph.add_edge('1', '3')
        graph.add_edge('1', '4')
        graph.add_edge('2', '5')
        graph.add_edge('2', '6')

    else:
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

        # print (graph.vertices)
        # print (graph.search())

    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        TEST = (argv[3])
        if NUM_EDGES > (NUM_VERTICES * (NUM_VERTICES-1)) / 2:
            print('Too many edges, creating default graph')
            main()
        else:
            main(NUM_VERTICES, NUM_EDGES, TEST)
    elif len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        if NUM_EDGES > (NUM_VERTICES * (NUM_VERTICES-1)) / 2:
            print('Too many edges, creating default graph')
            main()
        else:
            main(NUM_VERTICES, NUM_EDGES)
    elif len(argv) == 2:
        TEST = int(argv[1])
        main(test=TEST)
    else:
        main()