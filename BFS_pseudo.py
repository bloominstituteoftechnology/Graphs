BFS(graph, startVert):
    for v of graph.vertexes:
        v.color = white

    startVert.color = gray
    queue.enqueue(startVert)

    while !queue.isEmpty():
        u = queue[0]

        for v of u.neighbors:
            if v.color is white
            v.color = gray
            queue.enqueue(v)

        queue.dequeue()
        u.color = black
