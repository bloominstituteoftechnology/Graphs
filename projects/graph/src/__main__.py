from graph import Graph
from draw import BokehGraph
from random import sample
""""
num_vertices=[v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19]
#def main():
#  graph = Graph()
#   for num in range(num_vertices):
#       graph.add_vertex(str(num))

    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        #TODO check if edge exists
        graph.add_edge(vertices[0], vertices[1])

if __name__ == '__main__'
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main() #accepts defaults
"""







def main():

    graph = Graph()

    graph.add_vertex('v0')
    graph.add_vertex('v1')
    graph.add_vertex('v2')
    graph.add_vertex('v3')
    graph.add_vertex('v4')
    graph.add_vertex('v5')
    graph.add_vertex('v6')
    graph.add_vertex('v7')
    graph.add_vertex('v8')
    graph.add_vertex('v9')
    graph.add_vertex('v10')
    graph.add_vertex('v11')
    graph.add_vertex('v12')
    graph.add_vertex('v13')
    graph.add_vertex('v14')
    graph.add_vertex('v15')
    graph.add_vertex('v16')
    graph.add_vertex('v17')
    graph.add_vertex('v18')
    graph.add_vertex('v19')
    

    graph.add_edge('v1', 'v2')
    graph.add_edge('v2', 'v7')
    graph.add_edge('v7', 'v6')
    graph.add_edge('v7', 'v8')
    graph.add_edge('v8', 'v3')
    graph.add_edge('v8', 'v9')
    graph.add_edge('v9', 'v14')
    graph.add_edge('v14', 'v13')
    graph.add_edge('v13', 'v8')
    graph.add_edge('v13', 'v12')
    
    
    graph.add_edge('v15', 'v16')
    graph.add_edge('v16', 'v17')



    bg = BokehGraph(graph)
    print(bg.pos)
    print(bg.plot)
    bg.show()

if __name__ == "__main__":
    main()