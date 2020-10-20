from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # create a new graph
    g = Graph()

    # loop through every tuple of values being passed in
    # and add vertices for all values
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])

    # loop through all tuples,
    # and add an edge from value at index 0 to value at index 1
    for pair in ancestors:
        g.add_edge(pair[1], pair[0])

    # call the modified DFS function on the graph class,
    # finding the earliest ancestor for the starting node passed in
    ancestor = g.find_earliest_ancestor(starting_node)

    # if the last value in the list is the starting node,
    # there is no earliest ancestor,
    # return -1 indicating failure
    if ancestor[-1] == starting_node:
        return -1
    # else return the last element from the list
    else:
        return ancestor[-1]


if __name__ == "__main__":
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(ancestors, 3))

    # Expected output: 10


"""
Example input
    6
  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Expected Output
    10
"""
