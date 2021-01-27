class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __str__(self):
        return f"{self.value} + edges: {[x.value for x in self.edges]}"


a = GraphNode(7)
b = GraphNode(3)
c = GraphNode(1)
d = GraphNode(6)
e = GraphNode(9)

a.edges = [b, e]
b.edges = [c, d]
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")


# DEPTH FIRST TRAVERSAL
def dft(node: GraphNode):
    print(node.value)  # visit node

    for edge in node.edges:  # visit neighbors
        dft(edge)  # recurse with nodes in node.edges


# a -> b -> c -> d -> e
dft(a)

# def dfs_util(value, visited):
#     visited.add(value)
#     print(f"{value} ")
#     for neighbor in
#
# def dfs(value):
#     visited_nodes = set()
