from collections import deque


# Bi-Directional Search
# Operates by running two BFS simultaneously, one from the starting node and one from the destination node
# Each iteration, we'll take one step forward and one step back
# Once the paths overlap, we know we've hit a short path
#
# Queue for FORWARD --- represents the next nodes to visit in the starting_node's BST
# Queue for BACKWARD -- represents the next nodes to visit in the destination_node's BST
#
#
# https://www.cs.princeton.edu/courses/archive/spr06/cos423/Handouts/EPP%20shortest%20path%20algorithms.pdf
def bidi_search(graph, start, destination):
    if start == destination:
        return [start]

    # Get dictionary of currently active vertices with their corresponding paths.
    active_vert_paths = {
        start: [start],
        destination: [destination]
    }

    inactive_vert = set()

    while len(active_vert_paths) > 0:

        active_verts = list(active_vert_paths.keys())

        for vert in active_verts:
            current_path = active_vert_paths[vert]
            origin = current_path[0]
            current_neighbours = set(graph[vert]) - inactive_vert
            breakpoint()
            # Check if our neighbours hit an active vertex
            hits = current_neighbours.intersection(active_verts)

            if len(hits) > 0:
                for meeting_vertex in current_neighbours.intersection(active_verts):
                    # Check the two paths didn't start at same place. If not, then we've got a path from start to goal.
                    if origin != active_vert_paths[meeting_vertex][0]:
                        # Reverse one of the paths.
                        active_vert_paths[meeting_vertex].reverse()
                        # return the combined results
                        return active_vert_paths[vert] + active_vert_paths[meeting_vertex]

            # No hits, so check for new neighbours to extend our paths.
            new_neighbors = set(current_neighbours) - inactive_vert - set(active_verts)
            if len(new_neighbors) == 0:
                # If none, then remove the current path and record the endpoint as inactive.
                active_vert_paths.pop(vert, None)
                inactive_vert.add(vert)
            else:
                # Otherwise extend the paths, remove the previous one and update the inactive vertices.
                neighbors = current_neighbours - inactive_vert - set(active_verts)
                for neighbour_vertex in neighbors:
                    active_vert_paths[neighbour_vertex] = current_path + [neighbour_vertex]
                    active_verts.append(neighbour_vertex)
                popped = active_vert_paths.pop(vert, None)
                inactive_vert.add(vert)

    return None


def bidirectional_search(graph, start, destination):
    # print(f"\n\n--------------------\nRUNNING FUNCTION---args: start={start}, dest={destination}")

    q1 = deque()
    q2 = deque()
    q1.append(start)
    q2.append(destination)
    v1 = set()
    v2 = set()
    visited = set()
    path_forward = deque()
    path_backward = deque()

    while q1 or q2:
        step_f = q1.popleft()
        step_b = q2.popleft()
        iter_msg = f"""
ITER --- 
    step_f={step_f} 
    step_b={step_b}
    
    v1={v1}
    v2={v2}
    
    path_f={path_forward}
    path_b={path_backward} 
"""
        print(iter_msg)

        try:
            b_is_last_f = path_forward[-1] == step_b
        except IndexError:
            b_is_last_f = False
        try:
            f_is_last_b = path_backward[0] == step_f
        except IndexError:
            f_is_last_b = False
        f_is_b = step_f == step_b

        tie_f = step_f in v2
        tie_b = step_b in v1

        if f_is_b:
            if f_is_last_b and b_is_last_f:
                return list(path_forward + path_backward)
            elif not (f_is_last_b or b_is_last_f):
                path_forward.append(step_f)
                return list(path_forward + path_backward)
            else:
                path_forward.append(step_f)

        if f_is_last_b and b_is_last_f:
            q1.clear()
            q2.clear()
            return list(path_forward + path_backward)

        if not f_is_last_b and not b_is_last_f:
            if tie_f:
                path_forward.append(step_f)
                return list(path_forward + path_backward)
            if tie_b:
                path_forward.append(step_b)
                return list(path_forward + path_backward)

            path_forward.append(step_f)
            path_backward.appendleft(step_b)

        elif not b_is_last_f:
            return list(path_forward + path_backward)

        elif not f_is_last_b:
            return list(path_forward + path_backward)

        for connection in graph[step_f]:
            if connection not in v1:
                v1.add(connection)
                visited.add(connection)
                q1.append(connection)

        for connection in graph[step_b]:
            if connection not in v2:
                v2.add(connection)
                visited.add(connection)
                q2.append(connection)


def bidirectional_search_printy(graph, start, destination):
    print(f"\n\n--------------------\nRUNNING FUNCTION---args: start={start}, dest={destination}")

    if start == destination:
        return [start]

    q1 = deque()
    q2 = deque()
    q1.append(start)
    q2.append(destination)
    v1 = set()
    v2 = set()
    visited = set()
    # v1.add(start)
    path_forward = deque()
    path_backward = deque()

    def print_all(message=None):
        if message:
            print(f"{message}")
        else:
            print(f"--------")
        print(f"\tq1: {q1}\n\tq2: {q2}")
        print(f"\tv1: {v1}\n\tv2: {v2}")
        print(f"\tvisited: {visited}")
        print(f"\tforward: {path_forward}\n\tbackward: {path_backward}")

    while q1 or q2:
        step_f = q1.popleft()
        step_b = q2.popleft()

        print_all(f"\nSTART ITER --- step_f={step_f}, step_b={step_b}")
        print()

        if step_f in v2 and step_b in v1:
            print(f"step_f in v2 --- {step_f} in {v2}")
            print(f"step_b in v1 --- {step_b} in {v1}")
            x_f = path_forward.copy()
            x_b = path_backward.copy()
            print(f"for={x_f}, bac={x_b}")
        elif step_b in v1:
            x_f = path_forward.copy()
            x_b = path_backward.copy()
            print(f"step_b in v1 --- {step_b} in {v1}")
            print(f"for={x_f}, bac={x_b}")
        elif step_f in v2:
            x_f = path_forward.copy()
            x_b = path_backward.copy()
            print(f"step_f in v2 --- {step_f} in {v2}")
            print(f"for={x_f}, bac={x_b}")
        else:
            print("neither step in either visited")

        # if n1 in v2 or n2 in v1:  # path found
        # print(f"if {step_f} in {v2} or {step_b} in {v1} --- {step_f in v2 or step_b in v1}")
        # print(f"result would be {list(path_forward + path_backward)}")
        # print(f"if {step_f} in {visited} or {step_b} in {visited} --- {step_f in visited or step_b in visited}")
        # if step_b in visited and step_f in visited:
        #     x_f = path_forward.copy()
        #     x_f.append(step_f)
        #     x_b = path_backward.copy()
        #     x_b.appendleft(step_b)
        #     x_r = list(set(x_f + x_b))
        #     print(f"BOTH in vis == {x_r}")
        #     return x_r
        # elif step_f in visited:
        #     x = path_forward.copy()
        #     x.append(step_f)
        #     x_r = list(x + path_backward)
        #     print(f"step_f in vis == {x_r}")
        # elif step_b in visited:
        #     x = path_backward.copy()
        #     x.appendleft(step_b)
        #     x_r = list(path_forward + x)
        #     print(f"step_b in vis == {x_r}")

        if step_f in v2 or step_b in v1:
            combined = list(path_forward + path_backward)
            print_all(f"*** step_f={step_f}, step_b={step_b}, combined={combined}")
            res = combined
            print(f"\n\nENDING FUNCTION-----returned: {res}")
            return res

        for connection in graph[step_f]:
            if connection not in v1:
                v1.add(connection)
                visited.add(connection)
                q1.append(connection)

        for connection in graph[step_b]:
            if connection not in v2:
                v2.add(connection)
                visited.add(connection)
                q2.append(connection)

        path_forward.append(step_f)
        # if step_b != step_f:
        path_backward.appendleft(step_b)

        print_all(f"\nEND ITER")
        # visited.add(n1)
        # visited.add(n2)
        #
        # print_all(f"\nBEFORE --- step_f={step_f}, step_b={step_b}")
        # print_all(f"AFTER")
        # print_all(f"forward_q={q1}\nbackward_q={q2}")
