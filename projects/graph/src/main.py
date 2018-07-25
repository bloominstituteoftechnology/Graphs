from graph import Graph
from draw import BokehGraph


def main():
    print("hello")
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    bg = BokehGraph(graph)
    bg.plot
    bg.show()

if __name__ == '__main__':
    main()
