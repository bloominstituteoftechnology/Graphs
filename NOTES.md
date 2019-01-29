Node / Vertices
Edge 
Weight (cost) 

Directed Graph 

Cyclic Graph multiple visits
  Water cycle (sun -> evaporation -> condensation -> participation -> ground water -> evaportion -> etc.)
Acyclic graph only visited once
  Recipes 

Breadth First
Good for finding shortest path
Good if the vertex should be close to the start node
Getting from one city to another
How closely connected people are in a social network.

Begin starting vertex (s)
Explore vertex:
  while +1 unscheduled vertices adjacent to current vertex:
    schedule adjacent vertex to be explored (queue)
Mark vertex as explored and remove from queue 

Home -> School
\           \
 \            \
  -> Store -> Work

Home    1. remove from queue
School  2. remove from queue
Store   3. remove from queue
Work    4. remove from queue

Depth First 
Good for Strongly Connected Components
Only 1 solution (eg maze)

Begin starting vertex (s)
Explore vertex:
  if unexplored, adjacent vertex
    expore adjacent vertex

Mark explored once all adjacent vertices have been explored using a stack 

Home -> School
\           \
 \            \
  -> Store -> Work

Home   
School  
Work      1. remove from stack
School    2. remove from stack
Home
Store     3. remove from stack
Home      4. remove from stack
  -- not explored Store   


Shortest path of tree
Detecting cycle in a graph
Solving puzzles with only one solution (like a maze)
```
Adjacency Matrix    Graph   Adjacency List
  A B X P T                      
A 0 1 0 0 0         A  X        { A: B
B 1 0 1 1 1         | /           B: A, X, P, T
X 0 1 0 1 0         B             X: B, P
P 0 1 1 0 0         | \           P: X, B
T 0 1 0 0 0         T  P          T: B }
```
O(v^2)                            O(V + n) => O(# of vertices + # of edges)

Takeaways: Adjacency Matrix vs Adjacency List
Space efficiency: Adjacency lists are more space efficient for sparse graphs while adjacency matrices become efficient for dense graphs.
Adding vertices: is very efficient in adjacency lists but very inefficient for adjacency matrices.

```Python
#Matrix
for v in self.edges:
  self.edges[v].append(0)
v.append([0] * len(self.edges + 1))

#List
self.vertices["H"] = set()
```
Removing vertices: is inefficient in both adjacency matrices and lists but more inefficient in matrices.
Adding edges: to both adjacency lists and matrices is very efficient.
```Python
#Matrix
self.edges[v1][v2] = 1
#List
self.vertices[v1].add(v2)
```
Removing edges: from both adjacency lists and matrices is very efficient.
Finding edges: from both adjacency lists and matrices is very efficient.
Fetching all edges: is more efficient in an adjacency list than an adjacency matrix.
Undirected Matrix
