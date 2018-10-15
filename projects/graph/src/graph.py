"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        {
        '0': set(),
        '1': {'4', '5'},
        '2': set(),
        '3': {'4'},
        '4': {'1','3'},
        '5': {'1'},
        }

# This represents a graph with five vertices and three total (bidirectional) edges. 
# The vertex '0' and 2' have no edges, while '1' is connected to both '4' and '5', and '3' is connected to '4'.

graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_edge('1', '4')
graph.add_edge('1', '5')
graph.add_edge('3', '4')
print(graph.vertices)
