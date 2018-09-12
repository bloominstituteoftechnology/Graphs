"""
Simple graph implementation compatible with BokehGraph class.
"""
# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
#     def add_vertex(self, vertix):
#         self.vertices[str(vertix)] = set()
#     def add_edge(self, start, end):
#         start = str(start)
#         end = str(end)
#         if start not in self.vertices or end not in self.vertices:
#             raise Exception('Vertex does not exist!')
#         else:
#             self.vertices[start].add(end)
#             self.vertices[end].add(start)
#     def add_directed_edge(self, start, end):
#         if start in self.vertices and end in self.vertices:
#             self.vertices[start].add(end)
#         else:
#             raise IndexError("That vertex does not exist!")
# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('4')
# graph.add_vertex('5')
# graph.add_vertex('6')
# graph.add_vertex('7')
# graph.add_vertex('8')
# graph.add_vertex('9')
# graph.add_vertex('10')
# graph.add_vertex('11')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)
import networkx as nx
G = nx.DiGraph()
import matplotlib.pyplot as plt
G.add_nodes_from(nx.path_graph(10))
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(0,4)
G.add_edge(4,5)
G.add_edge(4,6)
G.add_edge(6,7)
G.add_edge(6,8)
G.add_edge(8,9)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color = 'r', node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True)
print(list(nx.dfs_edges(G, source=0)))
print(list(nx.bfs_edges(G, source=0)))
plt.show()
