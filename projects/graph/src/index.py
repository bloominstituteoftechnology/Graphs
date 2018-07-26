from graph import Graph, Vertex
from draw import BokehGraph

def main():
    graph = Graph()    
    
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_vertex("4")
    graph.add_vertex("5")
    graph.add_vertex("6")
    graph.add_vertex("7")
    graph.add_vertex("8")
    graph.add_vertex("9")
    graph.add_vertex("10")
    graph.add_vertex("11")
    graph.add_vertex("12")
    graph.add_vertex("13")
    graph.add_vertex("14")
    graph.add_vertex("15")
    graph.add_vertex("16")
    graph.add_vertex("17")
    graph.add_vertex("18")
    graph.add_vertex("19")
    graph.add_edge("1", "2")
    graph.add_edge("2", "7")
    graph.add_edge("7", "6")
    graph.add_edge("5", "6")
    graph.add_edge("5", "10")
    graph.add_edge("3", "8")
    graph.add_edge("7", "6")
    graph.add_edge("8", "7")
    graph.add_edge("8", "13")
    graph.add_edge("8", "9")
    graph.add_edge("9", "14")
    graph.add_edge("12", "13")
    graph.add_edge("13", "14")
    graph.add_edge("15", "16")
    graph.add_edge("16", "17")

    # graph.vertices

    # graph.get_connected_components()
    bg = BokehGraph(graph)

    # dir(bg)
    # bg.pos
    # bg.plot
    bg.show()
    # graph

if __name__ == "__main__":
    main()
