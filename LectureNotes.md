   A B C D E F
 +-------------
A | 0 0 1 1 1 0
B | 0 0 1 0 0 0
C | 1 0 0 1 0 0
D | 1 0 1 0 0 0
E | 1 0 0 0 0 0
F | 0 0 0 0 0 0
## Using an Adjacency List
Another way is to store a list of verts that a particular vert connects
to.
A: [ C D E ]
B: [ C ]
C: [ A D ]
D: [ A C ]
E: [ A ]
F: []
Adj Matrix
Add node: O(N)
Space complexity: O(N ^ 2)
Is Connected: O(1)
Print All Edges: O(N^2), N is number of nodes
Adj List
Add node: O(1)
Space complexity: O(N * e), where e is avg number of edges between nodes
Is Connected?: O(e), e is avg edges
Print All Edges: O(E), E is TOTAL number of edges




constraint in graphs can be variable equation.
weights in graphs particular 

napsack problem could be used for a credit card payments problem 