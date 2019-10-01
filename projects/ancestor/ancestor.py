from typing import Optional, NoReturn, Dict, Set, List

class Graph:
    """Represent a graph as a dictionary of vertices
        mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}
        self.adj_matrix = [[0 for _ in self.vertices]
                           for _ in self.vertices]

    def vert_not_exists_error(self, v: int) -> Optional[NoReturn]:
        """
        show an error to the screen if vertex does not exist
        """
        try:
            assert v in self.vertices.keys()
        except AssertionError:
            raise Exception(f"Vertex {v} does not exist")
        else:
            return None

    def add_vertex(self, vertex: int):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        pass

    def add_edge(self, v1: int, v2: int):
        """
        Add a directed edge to the graph.
        """
        self.vert_not_exists_error(v1)
        self.vert_not_exists_error(v2)

        self.vertices[v1].add(v2)
        pass

def bfs_distances(ancestors: Dict[int, Set[int]],
                  starting_node: int) -> Dict[int, int]:
    """ do bfs and return dictionary of all the distances
        reference: https://youtu.be/s-CYnVz-uh4 37 minutes
    """
    level: Dict[int, int] = {starting_node: 0}
    parent: Dict[int, Optional[int]] = {starting_node: None}
    i: int = 1
    frontier: List[int] = [starting_node]
    while frontier:
        next = []
        for u in frontier:
            for v in ancestors[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1

    return level

def earliest_ancestor(ancestors, starting_node):
    levels = bfs_distances(ancestors, starting_node)
    print(levels)
    curr_earliest = None
    curr_max = -99

    for node, level in levels.items():
        if level > curr_max:
            curr_max = level
            curr_earliest = node
    return curr_earliest

if __name__=='__main__':

    STARTING_NODE = 6

    EDGES = [(1, 3), (2, 3), (3, 6), (5, 6),
             (5, 7), (4, 5), (4, 8), (8, 9),
             (11, 8), (10, 1)
    ]

    VERTICES = {t[0] for t in EDGES} | {t[1] for t in EDGES}

    G = Graph()

    for v in VERTICES:
        G.add_vertex(v)
    for e in EDGES:
        G.add_edge(e[1], e[0])

    earliest = earliest_ancestor(G.vertices, STARTING_NODE)

    print(earliest)
