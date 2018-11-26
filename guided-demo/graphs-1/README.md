# Implement a Graph

## Using an Adjacency Matrix 

One way of representing connections between verts is with a matrix that
records `1` for a connection or `0` for no connection.

```
    A B C D
  +--------
A | 0 0 1 1
B | 0 0 1 0
C | 1 0 0 1
D | 1 0 1 0
```

In the above example B connects to C, but C does not connect back to B.

## Using an Adjacency List

Another way is to store a list of verts that a particular vert connects
to.

```
A -> [ C D ]
B -> [ C ]
C -> [ A D ]
D -> [ A C ]
```

This is the recommended approach for our graph projects.

## Comparison

What are the relative advantages and disadvantages of both methods?

An adjacency matrix uses O(n*n) memory. It has fast lookups to check for presence or absence of a specific edge, but slow to iterate over all edges.

Adjacency lists use memory in proportion to the number edges, which might save a lot of memory if the adjacency matrix is sparse. It is fast to iterate over all edges, but finding the presence or absence specific edge is slightly slower than with the matrix.


Origins of Graph Theory
7 bridges of Koenigsberg Before we start with the actual implementations of graphs in Python and before we start with the introduction of Python modules dealing with graphs, we want to devote ourselves to the origins of graph theory.
The origins take us back in time to the Künigsberg of the 18th century. Königsberg was a city in Prussia that time. The river Pregel flowed through the town, creating two islands. The city and the islands were connected by seven bridges as shown. The inhabitants of the city were moved by the question, if it was possible to take a walk through the town by visiting each area of the town and crossing each bridge only once? Every bridge must have been crossed completely, i.e. it is not allowed to walk halfway onto a bridge and then turn around and later cross the other half from the other side. The walk need not start and end at the same spot. Leonhard Euler solved the problem in 1735 by proving that it is not possible. He found out that the choice of a route inside each land area is irrelevant and that the only thing which mattered is the order (or the sequence) in which the bridges are crossed. He had formulated an abstraction of the problem, eliminating unnecessary facts and focussing on the land areas and the bridges connecting them. This way, he created the foundations of graph theory. If we see a "land area" as a vertex and each bridge as an edge, we have "reduced" the problem to a graph. 

http://interactivepython.org/courselib/static/pythonds/Graphs/VocabularyandDefinitions.html


