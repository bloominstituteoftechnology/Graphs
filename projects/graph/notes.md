# EDGE LIST
# Add neighbor: O(1)
# O(n)
# isNeighbor(): O(n)
# addNode(): O(1)
# removeNode(): O(e)
# How much memory?: O(e)
# Not very flexible 

edge_list - [
(1,2),
(1,4),
(1,7),
(2,3),
(2,5),
(3,6),
(4,7),
(5,6),
(6,7)
]

# ADJACENCY LIST
# Add neighbor: O(1),
# getNeighbor(): O(1)
# isNeighbor(): O(avg_edges)
# addNode(): O(1)
# removeNode(): O(n^2)
# How much memory?: O(n + e), n is number of nodes, e is number of edges
# Best of both worlds, best all purpose representation

adjacency_list = {
1: [2,4,7],
2: [1,3,5],
3: [2,6],
4: [1,7],
5: [2,6],
6: [3, 5, 7],
7: [1, 4, 6],
8: []
}

#ADJACENCY MATRIX
# Add neighbor: O(1),
# getNeighbor(): O(n)
# isNeighbor(): O(1)
# addNode(): O(n^2)
# removeNode(): 0(n^2)
# How much memory?: O(n^2) 
# Good for dense graphs and weighted graphs, kind of a memory hog, 

adjacency_matrix - {
  1:  [0,1,0,0,0,0,0],
  2:  [0,0,1,1,0,0,0],
  3:  [0,0,0,0,1,0,0],
  4:  [0,0,0,0,0,1,1],
  5:  [0,0,1,0,0,0,0],
  6:  [0,0,1,0,0,0,0],
  7:  [1,0,0,0,0,1,0]
}
