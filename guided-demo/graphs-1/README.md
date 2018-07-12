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

The adjacency list gives a seemingly readable method to follow letters and see what letter(s) are connected by looking in the array that the vertex is pointing towards. A disadvantage is visually it can be hard to picture how the whole graph will look like by just following the letters and trying to make mental images of the vertices and how they connect.

The adjacency matrix has an advantage of being somewhat intuitive when just looking at a series of 0 and 1s. However a disadvantage of looking at the connections this way is that it can be misinterpreted by looking at connections based on the x axis instead of the y. For instance, it could be misinterpreted that B has no connections using the vertices in the x axis, but it actually has 1 connection to C (from looking at it in the y axis).