from random import randint

class Vertex:
    """Vertices have a label and a set of edges."""
    def __init__(self, label, color="white"):
        self.label = label
        self.edges = set()
        self.color = color

    def __repr__(self):
        return str(self.label)

class ListGraph:
    """Adjacency list graph."""
    def __init__(self):
        self.vertices = set()

    def __str__(self):  
        return str(self.vertices)

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('This is not a vertex!')
        self.vertices.add(vertex)

    def breadth_first_search(self, target):
        queue = []
        #visited = []
        def bfs_helper(queue):
            if queue == []:
                return False
            current = queue.pop(0)
            #print(current)
            #if current in visited:
            #    return False
            #visited.append(current)
            if current.color == "black":
                return False
            if current.label == target:
                return True
            else:
                for x in current.edges:
                    if not x.color == "grey" and not x.color == "black":
                        x.color = "grey"
                        queue.append(x)
                    else:
                        continue
                current.color = "black"
                return bfs_helper(queue)

        queue.append(list(self.vertices)[0])
        return bfs_helper(queue)

    def depth_first_search(self, target):
        stack = []
        def dfs_helper(stack):
            current = stack.pop(0)
            if current.label == target:
                return True
            if current.color == "black":
                return False
            current.color = "grey"
            
            stack.insert(0, list(current.edges)[0])
            return dfs_helper(stack)

        stack.insert(0, list(self.vertices)[0])
        return dfs_helper(stack)

lg = ListGraph()
ints = []
for x in range(0, 50):
    ints.append(x)

for x in ints:
    lg.add_vertex(Vertex(f"v {x}"))

for x in range(0,75):
    lg.add_edge(list(lg.vertices)[randint(0, 49)], list(lg.vertices)[randint(0, 49)])

#print(lg.breadth_first_search("v 700"))
print(lg.depth_first_search("v 15"))
