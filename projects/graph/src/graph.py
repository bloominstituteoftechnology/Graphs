#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, label):
        if label in self.vertices:
            raise Exception("Vertex al ready in the Graph")
        vertex = Vertex(label)
        self.vertices[str(label)] = vertex.edges

    def add_edge(self, start_vertex, end_vertex, bidirectional=True):
        keys = self.vertices.keys()
        if (start_vertex not in keys) and (end_vertex not in keys):
            raise Exception('The vertex are not in the Graph')
        elif start_vertex not in keys:
            raise Exception(
                f'''The vertex {start_vertex} is not in the Graph.''')
        elif end_vertex not in keys:
            raise Exception(
                f'''The vertex {end_vertex} is not in the Graph.''')
        else:  # Both Vertex are in the Graph
            if bidirectional:
                self.vertices[str(start_vertex)].add(str(end_vertex))
                self.vertices[str(end_vertex)].add(str(start_vertex))
            else:
                self.vertices[str(start_vertex)].add(str(end_vertex))

    def bfs(self, starting_vertex=0, to_search=None):
        '''
        Search Breath first. Argunments:
        'starting_vertex': vertex from which start the search.
        to_search: Node to search
        '''
        deep = 0
        control = set()
        bf = [str(starting_vertex)]

        while bf:
            print(f'''BF{bf}\n{control}''')
            deep += 1
            current_vertex = bf[0]

            if str(to_search) == current_vertex:
                bf += [*self.vertices[current_vertex]]
                return {'Found value': current_vertex, 'deep': deep, 'Connected Nodes': control}
            elif current_vertex in control:
                bf.remove(current_vertex)
            else:
                # ADD to 'bf' list the current_vertex`s edges
                bf += [*self.vertices[current_vertex]]

                # Remove the curent_vertex from 'bf', and add it to 'control'
                control.add(bf.pop(0))

        return {
            'Searched value': f'''{to_search} No found''',
            'deep': deep,
            'Minimum Spanning Tree': control
        }


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()


_graph = Graph()  # Instantiate your graph
_graph.add_vertex('0')
_graph.add_vertex('1')
_graph.add_vertex('2')
_graph.add_vertex('3')
_graph.add_vertex('4')
_graph.add_vertex('5')
_graph.add_vertex('6')
_graph.add_vertex('7')
_graph.add_edge('0', '1')
_graph.add_edge('0', '3')
print('\n', _graph.vertices)
print('\n', _graph.bfs(0, 3))
print('\n', _graph.bfs(0, 100))
# graph.add_edge('0', '4')
