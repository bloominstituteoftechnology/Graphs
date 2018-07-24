from graph import Graph
from draw import BokehGraph

def main():

    graph = Graph()

    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')

    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('D', 'E')
    graph.add_edge('A', 'D')

    bg = BokehGraph(graph)
    print(bg.pos)
    print(bg.plot)
    bg.show()

if __name__ == "__main__":
    main()