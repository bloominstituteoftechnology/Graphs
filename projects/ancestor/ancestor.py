from collections import deque

def earliest_ancestor(ancestors, starting_node):
    struct = {}
    for i in ancestors:
        parent = i[0]
        child = i[1]
        if child not in struct:
            struct[child] = []
        struct[child].append(parent)

    q = deque()
    q.append([starting_node])
    l = [1,-1]
    while len(q) > 0:
        curr = q.popleft()
        last = curr[-1]
        if last not in struct:
            if len(curr) > l[0]:
                l = [len(curr), last]
            if len(curr) == l[0] and last < l[1]:
                l = (len(curr), last)
        else:
            for x in struct[last]:
                q.append(curr + [x])

    return l[1]