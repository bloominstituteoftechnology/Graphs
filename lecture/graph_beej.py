from collections import deque


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


# print(f"a: {a}")
# print(f"b: {b}")
# print(f"c: {c}")
# print(f"d: {d}")
# print(f"e: {e}")


# DEPTH FIRST TRAVERSAL
def dft(node_in: GraphNode):
    visited_nodes = set()

    def dft_util(node):
        nonlocal visited_nodes

        if node in visited_nodes:
            return

        print(node.value)  # visit node

        visited_nodes.add(node)

        for edge in node.edges:  # visit neighbors
            dft_util(edge)  # recurse with nodes in node.edges

    dft_util(node_in)


# a -> b -> c -> d -> e
# dft(a)


def pre_order(node: GraphNode):
    print(node.value)
    for edge in node.edges:
        dft(edge)


# def dfs_util(value, visited):
#     visited.add(value)
#     print(f"{value} ")
#     for neighbor in
#
# def dfs(value):
#     visited_nodes = set()


# def bfs(node: GraphNode):
#     dq = deque()
#     visited = set()
# dq.append()

def judge_trust(n, trust):
    trust_in = {i: 0 for i in range(1, n+1)}
    trust_out = {i: 0 for i in range(1, n+1)}

    for [truster, trustee] in trust:
        trust_out[truster] += 1
        trust_in[trustee] += 1

    judge = 0
    for key in trust_out:
        if trust_out[key] == 0:
            judge = key

    if judge > 0 and trust_in[judge] == (n - 1):
        return judge
    else:
        return -1


print(judge_trust(2, [[1, 2]]))  # 2
print(judge_trust(3, [[1, 3], [2, 3]]))  # 3
print(judge_trust(3, [[1, 3], [2, 3], [3, 1]]))  # -1
print(judge_trust(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))  # 3
