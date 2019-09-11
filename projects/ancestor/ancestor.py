
def createGraph(ancestor):
    vertices = {}
    for i in ancestor:
        if i[1] not in vertices:
            vertices[i[1]] = set()
        if i[0] not in vertices:
            vertices[i[0]] = set()
        vertices[i[1]].add(i[0])
    return vertices


def earliest_ancestor(ancestor, starting_node):
    a = createGraph(ancestor)
    v = [False]*(len(a)+1)
    s = []
    s.append(starting_node)
    p = []
    sv = starting_node

    while s:
        starting_node = s[-1]
        s.pop()
        if (not v[starting_node]):
            p.append(starting_node)
            v[starting_node] = True
        for node in a[starting_node]:
            if (not v[node]):
                s.append(node)

    if sv == p[-1]:
        return -1
    else:
        if p[-1] not in a[p[-2]] and p[-2] < p[-1]:
            return p[-2]
        else:
            return p[-1]


test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
        (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test, 6))
