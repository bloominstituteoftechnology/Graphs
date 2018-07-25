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
        self.connected_components = self.bfs()

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

    def bfs(self, to_search=None):
        '''
        Search Breath first. Argunments:
        'to_search': Node to search
        '''
        deep = 0
        connected_components = []
        visited_nodes = set()

        # print(f'''SELF VERTICES {self.vertices.keys()}''')
        for vertex in self.vertices.keys():
            bf = [vertex]
            if vertex not in visited_nodes:  # if fvertex no visited.
                # print('\n\nNO PASSED', vertex, '\n')
                response = self._bfs_connected_nodes(
                    to_search, deep, visited_nodes, bf)
                if isinstance(response, str):
                    return True
                else:
                    connected_components.append(response)
        # print('\nconnected_components', connected_components)
        self.connected_components = connected_components

    def _bfs_connected_nodes(self, to_search, deep, visited_nodes, bf):
        # print('\nDEF _BFS_CONNECTED', visited_nodes)
        control = set()
        while bf:
            # print(f'''BF{bf}\n{control}''')
            deep += 1
            current_vertex = bf[0]

            if str(to_search) == current_vertex:
                bf += [*self.vertices[current_vertex]]
                visited = bf.pop(0)
                control.add(visited)
                visited_nodes.add(visited)
                print('\n\n', {
                    'Found value': current_vertex,
                    'deep': deep,
                    'Connected Nodes': control,
                    'Visited nodes': visited_nodes,
                })
                return current_vertex
            elif current_vertex in control:
                bf.remove(current_vertex)
            else:
                # ADD to 'bf' list the current_vertex`s edges
                bf += [*self.vertices[current_vertex]]

                # Remove the curent_vertex from 'bf', and add it to 'control'
                visited = bf.pop(0)
                control.add(visited)
                visited_nodes.add(visited)

        # print({
        #     'Searched value': f'''{to_search} No found''',
        #     'deep': deep,
        #     'Connected Components': control,
        #     'Visited nodes': visited_nodes,
        # })
        return control

    def dfs(self, starting_vertex=0, to_search=None):
        pass


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()


# _graph = Graph()  # Instantiate your graph
# _graph.add_vertex('0')
# _graph.add_vertex('1')
# _graph.add_vertex('2')
# _graph.add_vertex('3')
# _graph.add_vertex('4')
# _graph.add_vertex('5')
# _graph.add_vertex('6')
# _graph.add_vertex('7')
# _graph.add_edge('0', '1')
# _graph.add_edge('0', '3')
# print('\nGraph vertices: ', _graph.vertices)
# _graph.bfs()
# print('\nConnected components', _graph.connected_components)
# print('\nVertex 3 in graph:', _graph.bfs(3))
# print('\nVertex 100 in graph:', _graph.bfs(100))
# graph.add_edge('0', '4')
