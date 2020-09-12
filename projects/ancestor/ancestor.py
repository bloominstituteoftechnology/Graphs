import sys
sys.path.append('../graph/')
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    pairings = {}
    children = set()
    s = Stack()
    for pair in ancestors:
        children.add(pair[1])
        if pair[1] not in pairings:
            pairings[pair[1]] = [pair[0]]
        else:
            pairings[pair[1]].append(pair[0])

    def get_parent(node):
        if node in pairings:
            return pairings.get(node)


    if starting_node not in children:
        return -1
    else:
        s.push(starting_node)
        while s.size() > 0:
            c = s.pop()
            if get_parent(c) is not None:
                for p in get_parent(c):
                    s.push(p)
            elif get_parent(c) is None and s.size() == 0:
                return c
     

