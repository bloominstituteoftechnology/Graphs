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


--------
API = Application Programming Interface

--what operations are supported so far?? 
 - add vertex, add edge

we want to add operations: search!

- breadth first search
    * This explores the ever increasing distance from the starting vertex. 
    * The algorithm never attempts to explore a vert that it either has explored or is exploring.
    
# Uses of BFS
* Pathfinding, Routing
* Web crawlers
* Finding people n connections away on a social site
* Find neighboring locations in a graph

```

pseudocode for BFS

BFS(graph, start)
    for v of graph, vertices:
        v.color = white
    startVert.color = gray
    queue.enqueue(startVert)

    while !queue.isEmpty():
        u = queue[0]

        for v of u.neighbors:
        if v.color = white:
            v.color = gray

            queue.enqueue(v)
        queue.dequeue()
        u.color = black
```
---------
# Depth First Search
* We don't visit the neighbor children first. We go as deep as possible first. This "dives" deep before needing to backtrack and explore a different branch. 
* The algorithm never attempts to explore a vert that it either has explored or is exploring

# Applications of DFS
* solving and generating mazes
* detecting cycles in graphs
* Path finding
* Topological sorting, useful for scheduling sequences for independent jobs.

```

pseudocode for DFS

DFS(graph):
    for v of graph.verts:
        v.color = white
        v.parent = null
    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)

DFS_visit(v):
    v.color = gray

    for neighbor of v.adjacent_nodes
        if neighbor.color == white:
            neighbor.parent = v
            DFS_visit(neighbor)

    v.color = black 


```

```
```

pseudocode for DFS (stack)

DFS(graph, start)
    for v of graph, vertices:
        v.color = white
    startVert.color = gray
    stack.restack(startVert)

    while !stack.isEmpty():
        u = stack[0]

        for v of u.neighbors:
        if v.color = white:
            v.color = gray

            stack.restack(v)
        stack.unstack()
        u.color = black

# Graphics
* Bokeh - Japanese term for an artsy photography style.
    - for our purposes it is a python library that can generate all sorts of neat visualizations 
    - geographic visualizations are pretty common here. 
    - how do we get to this?

What's the difference between pixel based and vector based graphics?    - how they are rendered. 
    - bitmaps / pixels have colors at coordinate levels that tell you what color something is. As you zoom in, gets pixelly. 
    - vector based graphics follow a mathematical formula that tells you how to draw something. As you zoom in, renders perfectly because the math equation is responsible for creating the graphic. 

----------

# Connected Components

Usefulness of Connected Components
* Social Networks
* Predict the spread of a zombie apocalypse
* Determining which parts of a computer network are reachable from another
* Finding clusters of related information
* Spread of disease

degree - the number of edges a vertex is connected to
cut - what you lose when you cut out a vertex. 

Finding Connected Components

If you have a BFS or DFS finding connected components is pretty straightforward if you modify your search to return number of verts visited. Also modify the search to not always color the verts white at the start. 

```
connected_components = []
visited = set()

for v in graph.vertices:
    v.color = white

for v in graph.vertices:
    if v not in visited:
        component = bfs(v)
        visited.update(component)
        connected_components.append(component)

```

asymptotic data - approach something without ever getting there. 