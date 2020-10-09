import copy
from util import Stack, Queue  # These may come in handy


def add_vertex(vertices, vertex_id):
    """
    Add a vertex to the graph.
    """
    if vertices.get(vertex_id) is None:
        vertices[vertex_id] = set()


def add_edge(vertices, v1, v2):
    """
    Add a directed edge to the graph.
    """
    if v1 in vertices and v2 in vertices:
        vertices[v1].add(v2)
    else:
        raise IndexError("nonexistent vertex")


def get_neighbors(vertices, vertex_id):
    """
    Get all neighbors (edges) of a vertex.
    """
    return vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):

    # Represent a graph as a dictionary of vertices mapping labels to edges
    vertices = {}
    # create a stack to store it all
    s = Stack()

    for pair in ancestors:
        add_vertex(vertices, pair[0])
        add_vertex(vertices, pair[1])
        add_edge(vertices, pair[1], pair[0])
    # print(graph.vertices)
    # add A PATH TO the starting vertex ID
    path = [starting_node]
    s.push(path)
    # Create a set to store visited vertices
    visited = set()
    # Create a list to store the path to earliest ancestor
    longest_path = []
    # While the stack is not empty...
    while s.size() > 0:

        # Remove the last path from stack
        p = s.pop()

        # Grab the last vertex from the path
        last = p[-1]

        # If two ancestors are from same generation, set longest_path to ancestor with smaller value
        if len(longest_path) == len(p) and last < longest_path[-1]:
            longest_path = p

        # Find longest path
        if len(longest_path) < len(p):
            longest_path = p

        # If that vertex has not been visited...
        if last not in visited:

            # Mark it as visited...
            visited.add(last)

            # Then add A PATH TO its neighbors to the top of the stack
            for neighbor in get_neighbors(vertices, last):
                # Shallow copy the path
                path = copy.copy(p)

                # Append the neighbor to the back
                path.append(neighbor)

                # Add updated path to stack
                s.push(path)

    # return -1 if no ancestors were found
    if len(longest_path) == 1:
        return -1

    # otherwise, return the earliest ancestor
    else:
        return longest_path[-1]
