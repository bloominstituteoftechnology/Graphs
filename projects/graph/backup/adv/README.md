## Part 6: Write an algorithm that will let you create any number of random adventure rooms

Part 1 may have felt familiar as you were filling out your graph class. Creating vertices and adding edges is very similar to creating Rooms and adding connections to your adventure game from [Week 1](https://github.com/LambdaSchool/Intro-Python). Your adventure room map can be thought of as a graph where each node has four possible edges: n_to, s_to, e_to and w_to.

Write an algorithm, `createRandomRooms` that takes in a number and generates that number of rooms. Each room should be connected and reachable from the player's starting room.

* It may help to assign a unique room_id to each room.
* None of the rooms should overlap and they should all exist on a valid grid. For example, starting in the lower left and traveling E,W,N,S or N,E,S,W should always return you to the original room.
```
[_]-[_]
 |   |
[_]-[_]
```
* How can you verify that all of the rooms are connected? (Hint: use a traversal)
* Some information about the room, like possible exits, should be present in the room description.
* Try to keep your runtime complexity to O(n).


## Part 7: Randomly drop a Treasure, then write a `search` method to find it.

Create a large number of rooms (say, 100) then drop a treasure in a random room before the game starts. Then, write a function for your player that uses BFS to find the shortest path to the treasure.
