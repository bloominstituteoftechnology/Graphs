"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # dictionary

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()  # initializing a new set

    def add_edge(self, key, value):
        if key not in self.vertices:
            raise Exception(f"No {key} vertex")
        self.vertices[key].add(value)
        if value not in self.vertices:
            raise Exception(f"No {value} vertex")
        self.vertices[value].add(key)
        #self.vertices[key].add(value)


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_edge("0", "1")
    graph.add_edge("0", "3")
    print(graph.vertices)
    # graph.add_edge("0", "4")

