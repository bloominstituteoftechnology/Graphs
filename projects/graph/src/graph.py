"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, item):
        self.vertices.update({item.label: item.edges})

    def add_edge(self, start, end, is_directed=False):
        start.edges.add(end.label)
        if not is_directed:
            end.edges.add({start.label})
    
    def breadth_first_search(self, vertex):
        nodes = []
        colors = {}
        my_queue = deque()

        for key in self.vertices.keys():
            # all vertices start out white
            colors[key] = 'white'

        my_queue.append(vertex)
        # gray means scheduled to be explored
        colors[vertex] = 'gray'

        while my_queue:
            node = my_queue[0]
            neighbors = self.vertices[node]

            for n in neighbors:
                if colors[n] == 'white':
                    my_queue.append(n)
                    colors[n] = 'gray'
            # black indicates exploration complete
            colors[node] = 'black'
            nodes.append(my_queue.popleft())
        return nodes
    
    def depth_first_search(self, vertex):
        
        def DFS_visit(vert):
            colors[str(vert)] = 'gray'
            nodes.append(vert)
            for n in self.vertices[vert]:
                if colors[str(n)] == 'white':
                    DFS_visit(n)
            colors[v] = 'black'

        nodes = []
        colors = {}
        for key in self.vertices.keys():
            colors[str(key)] = 'white'
        for v in self.vertices:
            if colors[str(v)] == 'white':
                DFS_visit(v)
            return nodes
    
    def connected_components(self):
        components = []
        visited = set()
        # loop through all nodes in graph
        # if node not visited
            # do bfs
            # save returned component
        for vertex in self.vertices.keys():
            if vertex not in visited:
                comp = self.breadth_first_search(vertex)
                components.append(comp)
                for c in comp:
                    visited.update(comp)

        return components
