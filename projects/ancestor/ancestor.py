def earliest_ancestor(ancestors, starting_node, valid_paths=None, out=None):

    if not out:
        out = []

    if not valid_paths:
        valid_paths = {x: [] for x in ancestors}

    visited = [x[1] for x in ancestors]

    if starting_node not in visited:
        return -1

    for x in ancestors:
        if starting_node == x[1]:
            starting_node = x[0]
            valid_paths[x].append(x)
            earliest_ancestor(ancestors, starting_node, valid_paths, out)

    valid_paths = {x: len(valid_paths[x]) for x in valid_paths}

    path_len = max(valid_paths, key=valid_paths.get)[0]

    valid_paths = [x for x in valid_paths.keys() if valid_paths[x] == path_len]

    if len(valid_paths) > 1:
        for k, v in valid_paths:
            if v == path_len:
                out.append(k)

        out = max(out)

    else:
        out = path_len

    return out
