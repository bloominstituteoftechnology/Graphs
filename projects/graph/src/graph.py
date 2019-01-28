"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {
        }

    def add_vertex(self, string):
        # adds vertexs and defaults it to a set
        self.vertices[string] = set()

    def add_edge(self, from_vertex, to_vertex):
        # check to see if theres a key with the name sent to from_vertex
        try:
            self.vertices[to_vertex].add(from_vertex)
            self.vertices[from_vertex].add(to_vertex)
        except:
            print('there is no vertex named', to_vertex, ' in the graph')

    def bst_traversal(self, start_node):
        nodes = []
        visited = []
        node = start_node
        nodes.insert(0, node)

        # enqueue the starting node
        while nodes:
            node = nodes.pop(0)
            # check if node has edges
            if len(self.vertices[node]) is 0:
                # dequeue next num
                visited.insert(0, node)
                pass
            else:
                # dequeue first node
                edge_nodes = list(self.vertices[node].copy())
                visited.insert(0, node)
                for i in edge_nodes:
                    if i in visited:
                        pass
                    else:
                        nodes.append(i)
                print(nodes)

        print("i have visited", visited)
        pass


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.bst_traversal('0')
# graph.add_edge('0', '4')
print(graph.vertices)