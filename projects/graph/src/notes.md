# What are graphs??
* Collection of related data. 
    - They are like trees, except connections can be made from any node to any other node. 
* They are made up of _vertices_ and _edges_. 
    - Vertices denote nodes of a graph.
    - Edges denote a relationship between two verts.
* Graphs can represent any kind of multiway relational data.

**Directed/Undirected Graphs**

_Directed Graph_ = > all edges are 'one way' and represented by using arrows =>

_Undirected Graph_ == all edges are bidirectional...no arrows between verts.

**Cyclic/Acyclic Graphs**

If a cycle can be formed, the graph is _cyclic_. Otherwise it is _acyclic_.

**Weighted Graphs**

Graphs with values associated with the edges are called _weighted graphs_.

The meaning of the weight is dependent on the type of graph. 


**Directed Acyclic Graph**

Notable that git uses DAG. A commit can have a child commit, or more than one child commit. A child could come from one parent commit, or from two (in the case of a merge). But there's no way back to form a repeating loop in the git commit hierarchy.