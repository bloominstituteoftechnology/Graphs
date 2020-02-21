from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    
    #one direction, children -> parents
    g = Graph()
    graph = {}
    family = set()

    for tup in ancestors:
        if tup[1] not in graph:
            graph[tup[1]] = set() 
        graph[tup[1]].add(tup[0])
        
        family.add(tup[0])
        family.add(tup[1])

    # for p, c in ancestors:
    #     g.add_vertex(c)    
    #     g.add_edge(c, p)

    g.vertices = graph
    
    print(graph)
    print(family)
    print(g.vertices)

    neighbors = g.get_neighbors(starting_node)

    if len(neighbors) == 0:
        return -1

    else:
        return g.dft(starting_node)









test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

node1 = earliest_ancestor(test_ancestors, 1)
print("node1 = 10?: ", node1)

node2 = earliest_ancestor(test_ancestors, 2)
print("node2 = -1?: ", node2)

node3 = earliest_ancestor(test_ancestors, 3)
print("node3 = 10?: ", node3)

node4 = earliest_ancestor(test_ancestors, 4)
print("node4 = -1?: ", node4)

node5 = earliest_ancestor(test_ancestors, 5)
print("node5 = 4?: ", node5)

node6 = earliest_ancestor(test_ancestors, 6)
print("node6 = 10?: ", node6)

node7 = earliest_ancestor(test_ancestors, 7)
print("node7 = 4?: ", node7)

node8 = earliest_ancestor(test_ancestors, 8)
print("node8 = 4?: ", node8)

node9 = earliest_ancestor(test_ancestors, 9)
print("node9 = 4?: ", node9)

node10 = earliest_ancestor(test_ancestors, 10)
print("node10 = -1?: ", node10)

node11 = earliest_ancestor(test_ancestors, 11)
print("node11 = -1?: ", node11)