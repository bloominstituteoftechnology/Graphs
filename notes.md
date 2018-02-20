# Graphs 

1. Graphs - can represent any network of data where each you have relationsh 1 to many different types of data. The nodes are the vertices and the lines are the edges. e.g subway where each station is the node or vertex while the tracks connecting ech station represent the line or edges. 
 
2. Directed Graph - the edges have direction or arrows. It isa one way connection. Bi directional relationships betweennodes can be epressed using two edges with arrows point toeach other. Undirected graphs have no arrows or sense of direction

3. Cyclic - The graph forms a cycle like a race course. Thesegraphs can have elements of cyclic without having to haveevery element involved in the process. So a cyclic graph isalways cyclic even if not every node is part of the cycle. Ascyclic cannot have any cycles in th graph or ways to visit a previous vertex.

4. Weighted Edges - edges themselves can have value e.g 1, 2and can represent measurements such as distance between twovertices or the cost to get from one vertex to another. 

5. Directed Ascylic - A graph that has no cycles and is notdirectional so each node goes in one direction

6. Binary Trees - Binary trees are special case of a graph which is both directed and asyclical. Binary trees has a root node though graphs don't. Binary trees do not represent bi directional realtionships as well. Graphs have more leeway to representing data compared to trees. 

7. Breadth first search - A search across a graph that starts at one node and spread out evenly to all the vertices from that node taking in all nodes from one layer before jumping into the next layer or depth. Can be used to find social connections or neighbors etc. 

8. Connected components - Breadth first seach help fnd these connected components. Breadth first search will search each neighbor of the node before jumping to the next node. 

c-b and c-a;  

start at c. c is added to the queue. c has neighbor a and b. a and b is added to queue. Once search is over, c is removed from queue and queue moves onto a. a neighbor is added to queue then a is removed. b's neighbor then added with b then removed from queue. Once queue is empty, breadth search is completed. Any node not connected at all will never be explored by the breadth first search as there is no way to reach it. 

 Note that a cycle can exist if nodes previously added to queue are being mentioned again as a neighbor node. Note that nodes that are already added to Queue and explored already will not be explored again meaning there will be no edge or line between these two nodes even if mentioned again. 