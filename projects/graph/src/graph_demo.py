from sys import argv
from graph import Graph
from draw import BokehGraph
import random


def createDefaultGraph():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')

    bg = BokehGraph(graph)
    bg.draw()


# O(n^2)
def createRandomGraph(numNodes, numEdges):
    graph = Graph()  # Instantiate your graph

    all_edges = []

    # O(n^2)
    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            all_edges.append( (i,  j) )

    # O(n)
    random.shuffle(all_edges)
    edges = all_edges[:numEdges]

    # O(1)
    if numEdges > len(all_edges):
        print("Warning: Too many edges")

    # O(n)
    for edge in edges:
        print(edge)

    # O(n)
    for i in range(numNodes):
        graph.add_vertex(i)

    # O(n)
    for edge in edges:
        print(edge)
        graph.add_edge(edge[0], edge[1])

    print(len(edges))

    bg = BokehGraph(graph)
    bg.draw()




def main(style, numNodes,  numEdges):
    if style  == "default":
        createDefaultGraph()
    elif style  == "random":
        createRandomGraph(numNodes, numEdges)
    else:
        createDefaultGraph()




if __name__ == '__main__':
    style = "default"
    numNodes = 5
    numEdges = 5

    for arg in argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "nodes":
                numNodes = int(arg_split[1])
            elif arg_split[0] == "edges":
                numEdges = int(arg_split[1])
            else:
                print("I don't understand that command.\n")

    main(style, numNodes, numEdges)

#
# #############################################
# # TODO::
# # Build Demo classm
# # ^^ takes:
# # -- number of vertices
# # -- number of edges (max = num of vertices)
# #
# # ^^ create Graph() isntance
# # ^^ create vertices (
# #     -> range 50,
# #     -> call add_vertex
# # )
# #
# # ^^ create edges (
# #     -> pick vertex index at random,
# #     -> create random integer,
# #     -> call add_edge
# # )
# #
# # ^^ create BokehGraph() instance
# # ^^ pass Graph to BokehGraph
# #     -> call draw() on instance
# #############################################
#
# class Network_Graph_Builder:
#     def __init__(self, num_v, num_e):
#         self.num_v = num_v
#         self.num_e = num_e
#         self.grf = Graph()
#         self.verts = self.grf.get_vertices()
#         self.bok = BokehGraph(self.grf)
#
#     def create_vertices(self):
#         for v in range(self.num_v):
#             self.grf.add_vertex(v)
#
#     def create_edges(self):
#         for ez in range(self.num_e):
#             a = self.rndm_int(self.num_v)
#             b = self.rndm_int(self.num_v)
#             self.grf.add_edge(a, b)
#
#     def get_rndm_vertex(self):
#         rndm_int = random.randint(self.num_v)
#         verts = self.grf.get_vertices()
#         return verts[rndm_int]
#
#     def rndm_int(self, qty):
#         return random.randint(0, qty-1)
#
#     def init_graph(self):
#         self.create_vertices()
#         self.create_edges()
#         self.bok.draw()
#
#
#
#
#
#
# # def main():
# #
# #
# #
# #
# # if __name__ == '__main__':
# #     # TODO - parse argv
# #     main()
#
#
# ntx = Network_Graph_Builder(20,10)
# ntx.init_graph()