
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_vertex(10)
    graph.add_vertex(11)
    for a in ancestors:
        graph.add_edge(a[1], a[0])
    # create empty stack
    s = Stack()
    s.push(starting_node)
    # create array to store vertices
    visited = []
    # while stack isn't empty,
    while s.size() > 0:
        popped = s.pop()
        for i in sorted(graph.vertices[popped]):
            s.push(i)
        # if vertex not visited, mark it as visited then add neighbors
        if popped not in visited and popped != starting_node:
            visited.append(popped)
    if len(visited) < 1:
        return -1
    elif len(visited) == 1:
        for v in visited:
            return v
    return visited[len(visited) - 1]
