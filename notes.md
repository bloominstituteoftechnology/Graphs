# Graphs 

1. Graphs - can represent any network of data where each you have relationsh 1 to many different types of data. The nodes are the vertices and the lines are the edges. e.g subway where each station is the node or vertex while the tracks connecting ech station represent the line or edges. 
 
2. Directed Graph - the edges have direction or arrows. It isa one way connection. Bi directional relationships betweennodes can be epressed using two edges with arrows point toeach other. Undirected graphs have no arrows or sense of direction

3. Cyclic - The graph forms a cycle like a race course. Thesegraphs can have elements of cyclic without having to haveevery element involved in the process. So a cyclic graph isalways cyclic even if not every node is part of the cycle. Ascyclic cannot have any cycles in th graph or ways to visit a previous vertex.

4. Weighted Edges - edges themselves can have value e.g 1, 2and can represent measurements such as distance between twovertices or the cost to get from one vertex to another. 

5. Directed Ascylic - A graph that has no cycles and is notdirectional so each node goes in one direction

6. Binary Trees - Binary trees are special case of a graph which is both directed and asyclical. Binary trees has a root node though graphs don't. Binary trees do not represent bi directional realtionships as well. Graphs have more leeway to representing data compared to trees. 

7. Breadth first search - A search across a graph that starts at one node and spread out evenly to all the vertices from that node taking in all nodes from one layer before jumping into the next layer or depth. Can be used to find social connections or neighbors etc. 
- Psuedo Code
BFS(graph, startVert):
  for v of graph.vertexes:
    v.color = white

  startVert.color = gray
  queue.enqueue(startVert)

  while !queue.isEmpty():
    u = queue[0]  // Peek at head of queue, but do not dequeue!

    for v of u.neighbors:
      if v.color == white:
        v.color = gray
        queue.enqueue(v)
    
    queue.dequeue()
    u.color = black

8. Connected components - Breadth first seach help fnd these connected components. Breadth first search will search each neighbor of the node before jumping to the next node. 

c-b and c-a;  

start at c. c is added to the queue. c has neighbor a and b. a and b is added to queue. Once search is over, c is removed from queue and queue moves onto a. a neighbor is added to queue then a is removed. b's neighbor then added with b then removed from queue. Once queue is empty, breadth search is completed. Any node not connected at all will never be explored by the breadth first search as there is no way to reach it. 

Note that a cycle can exist if nodes previously added to queue are being mentioned again as a neighbor node. Note that nodes that are already added to Queue and explored already will not be explored again meaning there will be no edge or line between these two nodes even if mentioned again. You can also go trace back to previous nodes to track the shortest cost to bet back to the root node from the current one. Which sibling is searched first doesn't matter only parents and child node order matters.

9. Implementation of Graph - You can easily find if there is an edge between the two vertex using a hash or two dimensional array. The positive is that you can run this in constant time O(1) with the downside being that it doesn't scale particularly well for larger data sets. 

class Graph {
    constructor() {
        // consists of an array of vertices
        this.vert = [];
    }
}

class Vertex {
    constructor() {
        // each vertex will have an array of edges. These edges would go from this vertex to other vertices
        // Parent will be stored in vertex as well if applicable
        this.edges = [];
        this.parent = null;
    }
}

class Edge {
    constructor {
        // weight could go here as the vertices that the vertex pointing to otherwise known as the destination. 
        this.weight = weight;
        this.destination = destination;    // the destination or the nodes or vertices vertex points to. 
    }
}

The disadvantage of this implementation is that it takes longer to find a particular vertex we might be interested in. However, it does take up less space especially compared to hash. In case of having lots of vertices, it will actually take up more space 

10. Completely connected graph: When vertices are 100 percent all connected with one another. Every node is able to connect with every other node.  

11. Depth First Search - Goes deep into one path until it reaches a node or vertex with no neighbors. Then it backtracks while black each node that has no neighbors. If during the backtrack or reverse it does find a vertex with neighbors, then it will go follow that path as far as it can until it reaches a node with no neighbors, backtracks again while blacking each node with no neighbors along the way and taking path with vertexes that do have neighbors. 

// solving depth first search using recursion
explore(graph) {
    visit(this_vert);
    explore(remaining_graph);
}
- Psuedo Code
DFS(graph):
    for v of graph.verts:
        v.color = white
        v.parent = null

    for v of graph.verts:
        if v.color == white:
            DFS_visit(v)

DFS_visit(v):
    v.color = gray

    for neighbor of v.adjacent_nodes:
        if neighbor.color == white:
            neighbor.parent = v
            DFS_visit(neighbor)

    v.color = black
