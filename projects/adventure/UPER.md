# UPER

## Understand

### I/O

INPUT: pre-generated graph consisting of 500 rooms.

OUTPUT: traversal_path — a path with directions that, when walked in order, will visit every room on the map at least
once

INPUT: GRAPH 

OUTPUT: PATH

### File Structure

`adv.py`

- world generation code — do not modify
- incomplete list of directions (this will be returned with valid traversal directions)
- Test Code - run file to run test
- REPL code, uncomment and run to walk around map

### General

To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits
`["n", "s", "w", "e"]`. Your starting graph might look something like so:

```
starting_path = {
    0: {"n": "?", "s": "?", "w": "?", "e": "?"}
}
```

Then, after moving south you'll find yourself in room `5` which contains exits `["n", "s", "e"]`. You can now fill in
some entries in your graph
```
traversal_path = {
    0: {"n": "?", "s": "?", "w": "?", "e": "?"},
    5: {"n": 0, "s": "?", "e": "?"}
}
```

You know you have finished when you have exactly 500 entries (0-499) in your graph and no `?` in the adjacency dictionaries. To do this, you'll need to write a traversal algorithm that logs the path into the `traversal_path` as it walks.

Your solution must generate the solution by using graph traversal algorithms. Hard-coding a solution is not acceptable.

### Hints

Start by writing an algorithm that picks a random unexplored direction from the players current room, travels and logs that direction, then loops. 
This should cause your player to walk a depth-first traversal. When you reach a dead-end, (i.e., a room with no unexplored paths), walk abck to the nearest room that does not contain an unexplored path. 

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `?` for an exit. If you use the `BFS` code from your homework, you'll need to make a few modifications. 

1. Instead of searching for a target vertex, you are searching for an exity with a `?` as the value. If an exit has been explored, you can put it in your BFS queue like normal.
2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

If all paths have been explored, you're done.

### Sandbox
Input: Graph

Output: int?

## Plan

## Execute

## Reflect