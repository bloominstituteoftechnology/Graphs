"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {
        }

    def add_vertex(self, string):
        self.vertices[string] = set()

    def add_edge(self, from_vertex, to_vertex):
        self.vertices[to_vertex].add(from_vertex)
        self.vertices[from_vertex].add(to_vertex)

    def bst_traversal(self, start_node):
        nodes = []
        visited = []
        node = start_node
        nodes.append(node)
        while nodes:
            node = nodes.pop(0)
            if len(self.vertices[node]) is 0:
                visited.append(node)
                pass
            else:
                edge_nodes = list(self.vertices[node].copy())
                visited.append(node)
                for i in edge_nodes:
                    if i in visited or i in nodes:
                        pass
                    else:
                        nodes.append(i)
                print(nodes)

        print(visited)

    def dft_traversal(self, start_node):
        nodes = []
        visited = []
        node = start_node
        nodes.append(node)
        while nodes:

            node = nodes.pop()
            if len(self.vertices[node]) is 0:
                visited.append(node)

                pass
            else:
                edge_nodes = list(self.vertices[node].copy())
                visited.append(node)
                for i in edge_nodes:
                    if i in visited or i in nodes:
                        pass
                    else:
                        nodes.append(i)

                print (nodes)
        print(visited)
        pass


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '5')
graph.add_edge('1', '4')
print(graph.vertices)
graph.bst_traversal('0')
graph.dft_traversal('0')