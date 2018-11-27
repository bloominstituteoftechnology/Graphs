# Searching and Generating Graphs

This is a multi-stage project to draw a graph and show the connected
components of that graph in different colors.


# Day 1-2

## Part 1: Graph, Vertex, Edge Classes

In the file `graph.py`, implement a `Graph` class that supports the API expected
by `draw.py`. In particular, this means there should be a field `vertices` that
contains a dictionary mapping vertex labels to edges. For example:

```python
{
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}
```

This represents a graph with four vertices and two total (bidirectional) edges.
The vertex `'2'` has no edges, while `'0'` is connected to both `'1'` and `'3'`.

You should also create `add_vertex` and `add_edge` methods that add the
specified entities to the graph. To test your implementation, instantiate an
empty graph and then try to run the following:

```python
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
```

You should see something like the first example. As a stretch goal, add checks
to your graph to ensure that edges to nonexistent vertices are rejected.

```python
# Continuing from previous example
graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
```

## Part 2: Implement Breadth-First Traversal

Write a function within your Graph class that takes takes a starting node as an argument, then performs BFT. Your function should print the resulting nodes in the order they were visited.


## Part 3: Implement Depth-First Traversal with a Stack

Write a function within your Graph class that takes takes a starting node as an argument, then performs DFT. Your function should print the resulting nodes in the order they were visited.


## Part 3.5: Implement Depth-First Traversal using Recursion

Write a function within your Graph class that takes takes a starting node as an argument, then performs DFT using recursion. Your function should print the resulting nodes in the order they were visited.

## Part 4: Implement Breadth-First Search

Write a function within your Graph class that takes takes a starting node and a destination node as an argument, then performs BFS. Your function should return the shortest path from the start node to the destination node.

## Part 5: Implement Depth-First Search

Write a function within your Graph class that takes takes a starting node and a destination node as an argument, then performs DFS. Your function should return a valid path (not necessarily the shortest) from the start node to the destination node.


# Day 3-4


## Part 6: Write an algorithm that will let you create any number of random adventure rooms

Part 1 may have felt familiar as you were filling out your graph class. Creating vertices and adding edges is very similar to creating Rooms and adding connections to your adventure game from [Week 1](https://github.com/LambdaSchool/Intro-Python). Your adventure room map can be thought of as a graph where each node has four possible edges: n_to, s_to, e_to and w_to.

Write an algorithm, `createRandomRooms` that takes in a number and generates that number of rooms. Each room should be connected and reachable from the player's starting room.

* It may help to assign a unique room_id to each room.
```
[_]-[_]
 |   |
[_]-[_]
```
* None of the rooms should overlap and they should all exist on a valid grid. For example, starting in the lower left and traveling E,W,N,S or N,E,S,W should always return you to the original room.
* How can you verify that all of the rooms are connected? (Hint: use a traversal)
* Some information about the room, like possible exits, should be present in the room description.
* Try to keep your runtime complexity to O(n).


## Part 7: Randomly drop a Treasure, then write a `search` method to find it.

Create a large number of rooms (say, 100) then drop a treasure in a random room before the game starts. Then, write a function for your player that uses BFS to find the shortest path to the treasure.


