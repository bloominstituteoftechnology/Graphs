# 3 STEPS TO SOLVE GRAPH PROBLEM

# 1 - TRANSLATE PROBLEM INTO GRAPH TERMS -- NODES AND EDGES(RELATIONSHIP)

# 2 - BUILD GRAPH

# 3 - TRAVERSE GRAPH

from util import Queue

def find_latters(begin_word, end_word):
    q = Queue()
    q.enqueu()
    visited = set()
    while q.size() > 0:
        path= q.equeue()
        w = path[-1]
        if w == end_word:
            return path
        if w not in visited:
            visited.add(w)
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                q.enque(path_copy)
