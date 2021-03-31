from collections import deque


def bidirectional_search(graph, start, destination):
    q1 = deque()
    q2 = deque()
    q1.append(start)
    q2.append(destination)
    v1 = set()
    v2 = set()
    v1.add(start)
    path_forward = deque()
    path_backward = deque()

    def print_all(message=None):
        if message:
            print(f"{message}")
        else:
            print(f"--------")
        print(f"\tq1: {q1}\n\tq2: {q2}")
        print(f"\tv1: {v1}\n\tv2: {v2}")
        print(f"\tforward: {path_forward}\n\tbackward: {path_backward}")

    while q1 or q2:
        n1 = q1.popleft()
        n2 = q2.popleft()

        if n1 in v2 or n2 in v1:  # path found
            combined = list(path_forward + path_backward)
            return combined if combined else [start]

        for connection in graph[n1]:
            if connection not in v1:
                v1.add(connection)
                q1.append(connection)

        for connection in graph[n2]:
            if connection not in v2:
                v2.add(connection)
                q2.append(connection)

        path_forward.append(n1)
        if n2 != n1:
            path_backward.appendleft(n2)
