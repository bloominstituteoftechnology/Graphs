# Graphs

## Objectives

* [Graph Intro](objectives/graph-intro)
* [Graph Representations](objectives/graph-representations)
* [Breadth First Search](objectives/breadth-first-search)
* [Depth First Search](objectives/depth-first-search)
* [Randomness](objectives/randomness)
* [Connected Components](objectives/connected-components)

## Projects

### Day 1
* [Graph Traversal and Search](projects/graph)

What is a graph?
- a bunch of nodes (vertexes, verteces or notes) that contain data.
    - The Nodes store the data
    - nodes are connected by "edges"
        - can be "unidirectional" or "bidriectional" (also called "nondirectional").
        - if a graph has directional edges it's called a "directed graph"
- Linked lists are graphs!!!
- If a series of nodes are all connected then they are in a "cylce"
    - Linked lists can't loop back on themselves. If the final node in a LL points to the first node, it's just a graph but no longer a LL.

Traversing
- Keep track of which nodes have been visited to avoid revisiting them

    * visited flag
    * Hash Table
    * Set

- we do this by starting at the top of the stack and going through each node until there aren't anymore. we store all of the visited nodes.


Depth-First Traversal
_______
What makes it depth-first? ==> starts at root node and traverses as far as it can along every branch before backtracking.

    push starting node on stack

    while stack isn't empty:
        pop the node off the top of the stack
        if node isn't visited:
            visit the node (e.g. print it out)
            mark it as visited
            push all its neighbors on the stack
Example:
_______

(A) => (B) => (C) => (D)
_______

Stack: <stack empty> 
Visited: A B C D
______________
______________
______________

Breadth-First Traversal
_______
What makes it breadth-first? ==> 

    push starting node on queue

    while stack isn't empty:
        pop the node off the front of the queue
        if node isn't visited:
            visit the node (e.g. print it out)
            mark it as visited
            add all its neighbors on the queue

Graph Representations
_____________________
'How we store the graph in memory

1. Adjacency matrix
2. Adjacency List

A matrix is a gric

  A B C D E F G H    TO
A   T   T       T
B T   T 
C   T         T
D T
E
F
G       T
H T

FROM

List:

A [B H D]
B [C A F E]
C [B G]
D [A]
E [B]
F [B]
G [C H]
H [G A]

Breadth First Search
_____________________
What is the shortest way to get from one path to another?

### Day 2
* [Earliest Ancestor](projects/ancestor)

### Day 3
* [Random Social Network](projects/social)

connected components
____________________

Parts of the graph that are connected, but disjoint from other parts of the graph.

from each node:
    if node not visited:
        traverse from that node
        increment counter

Graph:
             T  T  T  T  T  T  T  T  T  T  T
    nodes = [1, 2, 3, 4, 5, 7, A, B, C, D, E]
                               
    edges = [(A, B), (B, C), ... ]

Counter = 3

### Day 4
* [Adventure Map Traversal](projects/adventure)
