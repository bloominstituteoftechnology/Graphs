from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    q.enqueue([starting_node])
    longest_path = []
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

        if len(path) > len(longest_path):
            longest_path = path

        for i in range(len(ancestors)):
            if ancestors[i][1] is v:
                new_path = path.copy()
                # print(new_path)
                new_path.append(ancestors[i][0])
                q.enqueue(new_path)
        print('longest_path', longest_path)

    earliest = longest_path.pop()

    if earliest is starting_node:
        earliest = -1
    return earliest
