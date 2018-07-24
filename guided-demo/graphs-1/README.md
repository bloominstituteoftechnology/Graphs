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
