# Graphs FAQ

## Contents

* [What is a Graph?](#q100)
* [Why is it important to learn Graphs?](#q101)
* [How many types of graphs are there?](#q102)
* [What is the time complexity (big-O) to add/remove/get a vertex/edge for a graph?](#q103)


## Questions

<a name="q100"></a>
### What is a Graph?
A Graph is a data structure that models objects and pairwise relationships between them with nodes and edges. For example: Users and friendships, locations and paths between them, parents and children, etc.

<a name="q101"></a>
### Why is it important to learn Graphs?
Graphs represent relationships between data. Anytime you can identify a relationship pattern, you can build a graph and often gain insights through a traversal. These insights can be very powerful, allowing you to find new relationships, like users who have a similar taste in music or purchasing.

<a name="q102"></a>
### How many types of graphs are there?
Graphs can be directed or undirected, cyclic or acyclic, weighted or unweighted. They can also be represented with different underlying structures including, but not limited to, adjacency lists, adjacency matrices, object and pointers, or a custom solution.

<a name="q103"></a>
### What is the time complexity (big-O) to add/remove/get a vertex/edge for a graph?
It depends on the implementation. ([Graph Representations](https://github.com/LambdaSchool/Graphs/tree/master/objectives/graph-representations)). Before choosing an implementation, it is wise to consider the tradeoffs and complexities of the most commonly used operations.