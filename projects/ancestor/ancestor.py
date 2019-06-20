import sys
sys.path.append('../graph')
from graph import Graph
from util import Stack, Queue


def earliest_ancestor(arr, k):
    assert len(arr[0]) == 2, 'input array must have 2 columns'
    g = Graph()  # child to parent
    for row in arr:
        g.add_vertex(row[0], True)
        g.add_vertex(row[1], True)
        g.add_edge(row[1], row[0])  # link child to parent

    can = []
    q = Queue()
    q.enqueue(k)

    while q.size() > 0:
        child_q = Queue()
        v = q.dequeue()
        for neighbor in g.vertices[v]:
            child_q.enqueue(neighbor)
            q.enqueue(neighbor)
        if child_q.size() == 0 and v != k:
            l = len(g.bfs(k, v))
            can.append([l,v])

    can.sort(key = lambda r: g.max_vertex * r[0] - r[1])
    return can[-1][1] if len(can) > 0 else -1

if __name__ == '__main__':

    vs = [
        [1, 3],
        [2, 3],
        [3, 6],
        [5, 6],
        [5, 7],
        [4, 5],
        [4, 8],
        [11, 8],
        [10, 1]

    ]

    print(earliest_ancestor(vs, 6)) # 10
    print(earliest_ancestor(vs, 8)) # 4
    print(earliest_ancestor(vs, 11)) # -1

