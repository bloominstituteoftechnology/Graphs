from graph import Graph
from draw import BokehGraph

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