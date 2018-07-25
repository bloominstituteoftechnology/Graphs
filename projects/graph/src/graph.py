#!/usr/bin/python

from random import (randint, sample)


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()


"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self, random=True):
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
        Search Breath first.
        Arguments:
            'to_search': Node to search in the Graph
        Returns:
            a. If passed the arguments:
                True: if the argument/node is in the Graph
                None: If the argument/node is not in the Graph
            b. If not argument is passed:
                It builds a list with all the 'connected_components'
                in the Graph and put it in 'self.connected_components'
                property.
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
        '''
        BFS for each Component in the Graph
        '''
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
                # print('\n\n', {
                #     'Found value': current_vertex,
                #     'deep': deep,
                #     'Connected Nodes': control,
                #     'Visited nodes': visited_nodes,
                # })
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

    def add_random_data(self, vertices=None, edges=None):
        '''
        Fill the Graph with mock data.
        '''
        self._random_vertices(vertices)
        self._random_edges(edges)

    def _random_vertices(self, number=None):
        '''
        Add random vertices, is not argument provided
        add between 10 and 30 vertices.
        '''
        if not number:
            number = randint(10, 30)

        for i in range(number):
            self.add_vertex(str(i))

    def _random_edges(self, num_edges=None):
        '''
        Add random Edges.
        If argument provided, it checks for the the
        Maxnumber of allowed edges (based on the number of Vertices)

        If not argument provided, it assign a random number of edges
        from 1 to the 'Max_number_of_allowed_edges'
        '''
        # Get max numner of edges
        num_vertices = len(self.vertices.keys())
        max_edges = num_vertices * (num_vertices - 1)

        # Check number of edges
        if not num_edges:  # Assign a random num of edges
            num_edges = randint(1, max_edges) // 3

        # Check if the passed number is not greater than the
        # allowed number of edges
        elif num_edges > max_edges:
            num_edges = max_edges

        for _ in range(num_edges):
            vertices = sample(self.vertices.keys(), 2)
            self.add_edge(vertices[0], vertices[1])


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
