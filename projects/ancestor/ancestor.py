from graph import Graph
from util import Stack, Queue  # These may come in handy


def earliest_ancestor(ancestors, starting_node):
    a_graph = Graph()

    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        if child not in a_graph.vertices:
            a_graph.add_vertex(child)

        a_graph.add_edge(child, parent)

    print(a_graph.vertices)
    if starting_node not in a_graph.vertices:
        return -1
    else:
        s = Stack()

        s.push(starting_node)

        visited = set()

        parent_1, parent_2 = None, None

        while s.size():

            current_node = s.pop()
            print("current_node", current_node)

            if current_node not in visited:
                visited.add(current_node)

                try:
                    neighbors = a_graph.get_neighbors(current_node)
                    print("neighbors", neighbors)
                    for neighbor in neighbors:
                        s.push(neighbor)

                    if len(neighbors) == 2:
                        for index, neighbor in enumerate(neighbors):
                            if index == 0:
                                parent_1 = neighbor
                            elif index == 1:
                                parent_2 = neighbor
                    elif len(neighbors) == 1:
                        for neighbor in neighbors:
                            parent_1 = neighbor
                            parent_2 = None

                    print("new parents |", parent_1, parent_2)
                except:
                    pass

        if parent_2 == None:
            return parent_1
        elif parent_1 == None:
            return parent_2
        else:
            if parent_1 > parent_2:
                return parent_2
            else:
                return parent_1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


print(earliest_ancestor(test_ancestors, 3))
