connected_components = []

for v in graph.vertices:
    v.color = white

for v in graph.vertices:

    if v.color == white:
        component = BFS(v)

        connected_components.push(component)
