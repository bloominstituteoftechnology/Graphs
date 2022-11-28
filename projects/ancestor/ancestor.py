from collections import deque

class Graph:
    def __init__(self):
        self.nodes = dict()
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()
    def add_edge(self, node, edge):
        if node in self.nodes and edge in self.nodes:
            self.nodes[node].add(edge)
        else:
            return ValueError('Node not found')
    def get_edges(self, target):
        if target in self.nodes:
            return self.nodes[target]
        else:
            return ValueError('Node not found')



def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_node(parent)
        graph.add_node(child)
        graph.add_edge(child, parent)
    q = deque()
    q.append([starting_node])
    longest = (None,0)

    if len(graph.get_edges(starting_node)) == 0:

        return -1

    curs = q.__len__()

    while curs > 0:
        end_of_q = q.pop()
        index = end_of_q[-1]
        lenth_of_q = len(end_of_q)


        if longest[1] is None:
            longest = (index, lenth_of_q)
        if lenth_of_q > longest[1]:
            longest = (index, lenth_of_q)
        elif lenth_of_q == longest[1]:
            if index < longest[0]:
                longest = (index, lenth_of_q)


        for i in graph.get_edges(index):
            temp_q = end_of_q.copy()
            temp_q.append(i)
            q.append(temp_q)
        curs = q.__len__()
    return(longest[0])
            

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))