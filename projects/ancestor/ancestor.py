# Import Graph, Queue and Stack from the graph folder
import sys
sys.path.append('../graph')
from graph import Graph
from util import Queue, Stack


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # print(ancestors)
    print(f"starting node: {starting_node}")

    for num in range(1, 12):
        graph.add_vertex(num)

    
    for pair in ancestors:
        # print(pair)
        graph.add_edge(pair[0], pair[1])

    
    test_number = ''
    test_array = []
    children_array = []

    # print(graph.vertices)
    for num in graph.vertices:
        # print(num)
        while len(graph.vertices[num]) > 0:
            test_number = graph.vertices[num].pop()
            # print(test_number)
            test_array.append((test_number, num))
            children_array.append(test_number)

    print(test_array)
    print(children_array)

    for i in test_array:
        print(i)
        if i[0] == starting_node:
            if i[1] in children_array:
                return earliest_ancestor(ancestors, i[1])
            else:
                print(i[1])
                return i[1]

    print(-1)
    return -1
