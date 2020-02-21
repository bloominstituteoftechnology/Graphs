## Description

You are provided with a pre-generated graph consisting of 500 rooms. You are responsible for filling `traversal_path` with directions that, when walked in order, will visit every room on the map at least once.

Open `adv.py`. There are four parts to the provided code:

* World generation code. Do not modify this!
* An incomplete list of directions. Your task is to fill this with valid traversal directions.
* Test code. Run the tests by typing `python3 adv.py` in your terminal.
* REPL code. You can uncomment this and run `python3 adv.py` to walk around the map.


You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.

To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:

```
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
```

Try moving south and you will find yourself in room `5` which contains exits `['n', 's', 'e']`. You can now fill in some entries in your graph:

```
{
  0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
  5: {'n': 0, 's': '?', 'e': '?'}
}
```

You know you are done when you have exactly 500 entries (0-499) in your graph and no `'?'` in the adjacency dictionaries. To do this, you will need to write a traversal algorithm that logs the path into `traversal_path` as it walks.

## Hints

There are a few smaller graphs in the file which you can test your traversal method on before committing to the large graph. You may find these easier to debug.

Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a `'?'` for an exit. If you use the `bfs` code from the homework, you will need to make a few modifications.

1. Instead of searching for a target vertex, you are searching for an exit with a `'?'` as the value. If an exit has been explored, you can put it in your BFS queue like normal.

2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w directions before you can add it to your traversal path.

If all paths have been explored, you're done!

## Minimum Viable Product

* __1__: Tests do not pass
* __2__: Tests pass with `len(traversal_path) <= 2000`
* __3__: Tests pass with `len(traversal_path) < 960`

## Stretch Problems

It is very difficult to calculate the shortest possible path that traverses the entire graph. Why?

My best path is 957 moves. Can you find a shorter path?


## Rubric
| OBJECTIVE | TASK | 1 - DOES NOT MEET Expectations | 2 - MEETS Expectations | 3 - EXCEEDS Expectations | SCORE |
| ---------- | ----- | ------- | ------- | ------- | -- |
| _Student can demonstrate applied knowledge of Graph Theory by traversing a large map_ | Complete traversal of a large Graph | Student unable to produce a valid traversal path of 2000 moves or less | Student is able to produce a valid traversal path between 960 and 2000 | Student produces a valid traversal path of 959 moves or less |  |
| **FINAL SCORE** | | **0-1** | **2** | **3** |  |

TESTS PASSED: 957 moves, 500 rooms visited
Final Traversal passed: ['n', 's', 's', 'w', 'e', 'n', 'e', 's', 's', 'w', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'w', 'w', 's', 'w', 's', 'n', 'e', 's', 'n', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'n', 'w', 'n', 's', 'e', 'e', 'n', 'w', 'e', 'n', 'w', 'e', 'n', 'w', 'w', 's', 'n', 'e', 'e', 'n', 'w', 'e', 'n', 'w', 'e', 'e', 'e', 's', 's', 's', 's', 's', 'n', 'e', 's', 's', 's', 'e', 's', 's', 's', 'n', 'n', 'e', 's', 's', 'n', 'n', 'e', 's', 's', 'n', 'n', 'w', 'w', 'n', 'e', 'e', 'n', 'e', 'e', 'e', 'w', 's', 's', 's', 's', 'n', 'n', 'e', 'w', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 'w', 'w', 'w', 's', 's', 'w', 's', 'n', 'e', 's', 's', 'n', 'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 'w', 'n', 'n', 'n', 'e', 'e', 's', 'e', 'n', 'e', 's', 's', 'n', 'n', 'w', 's', 'w', 's', 'e', 's', 'e', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'n', 'w', 's', 's', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 'n', 'n', 'e', 's', 'n', 'w', 'n', 'e', 'w', 'n', 'n', 'w', 'n', 'w', 'e', 'n', 'w', 'n', 'w', 'n', 's', 'e', 'n', 'n', 'w', 'w', 'n', 'w', 'e', 's', 'e', 'n', 's', 'e', 's', 's', 's', 'w', 'w', 'w', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 'n', 'w', 'w', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 'w', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 'e', 'e', 'n', 'n', 's', 's', 'e', 'n', 'n', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 's', 's', 's', 'w', 'w', 'e', 'e', 'e', 's', 'e', 'n', 's', 'e', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'e', 'e', 'e', 'e', 's', 'n', 'n', 'n', 'w', 'n', 'n', 'w', 'n', 'w', 'e', 'e', 'w', 's', 'e', 's', 's', 'e', 'n', 'n', 'e', 'e', 'n', 's', 'e', 'e', 'w', 'n', 'e', 'n', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 'e', 'w', 'w', 'n', 'n', 'e', 'n', 'e', 'n', 'e', 'e', 'w', 's', 'n', 'w', 'n', 's', 's', 'w', 'n', 's', 's', 'w', 'n', 'n', 's', 's', 's', 'w', 'n', 'n', 'n', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'n', 'w', 'w', 'e', 'e', 's', 'w', 's', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 'w', 'w', 'w', 'n', 'n', 'n', 'n', 's', 's', 's', 'w', 'n', 'n', 'w', 'e', 's', 's', 'e', 's', 'w', 's', 'w', 'e', 'n', 'w', 'n', 's', 'w', 'n', 's', 'e', 'e', 'e', 'e', 'e', 'n', 'w', 'n', 's', 'e', 'n', 's', 's', 'e', 's', 'e', 'w', 's', 's', 'e', 'e', 'w', 'w', 's', 's', 's', 'w', 'n', 's', 's', 's', 'w', 'w', 'w', 'n', 's', 'w', 'n', 's', 'w', 'n', 'w', 'w', 'e', 'n', 'w', 'e', 's', 'e', 's', 'w', 'w', 'w', 'n', 'w', 'w', 's', 'n', 'w', 'e', 'e', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 'n', 's', 's', 'e', 'n', 's', 's', 'w', 'e', 'e', 'e', 'e', 's', 's', 'n', 'w', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'w', 'w', 'n', 's', 'w', 'e', 'e', 's', 'w', 'w', 'e', 's', 'e', 's', 's', 'e', 's', 'e', 'e', 'e', 's', 'w', 's', 'w', 's', 'n', 'e', 'n', 'w', 'w', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'w', 's', 'w', 'e', 's', 's', 's', 'n', 'w', 'w', 'e', 'e', 'n', 'w', 'e', 'n', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 's', 's', 's', 'e', 'w', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'e', 'e', 'n', 'e', 'n', 'n', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 'n', 'w', 'w', 'w', 's', 'w', 'n', 's', 'e', 'n', 'e', 'e', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'e', 'n', 'n', 'n', 'e', 's', 'n', 'e', 'e', 's', 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'e', 'e', 'n', 'e', 'e', 's', 's', 's', 'n', 'n', 'e', 's', 'e', 'e', 's', 'e', 'e', 'e', 'w', 's', 'n', 'w', 'w', 's', 's', 'e', 'e', 'w', 'n', 's', 'w', 's', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'n', 'n', 'n', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'w', 's', 'e', 'w', 'n', 'n', 'w', 'n', 'e', 'e', 's', 'n', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'n', 's', 'e', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w', 'n', 'e', 'n', 'n', 'e', 'e', 'n', 'e', 'w', 's', 'w', 'n', 'n', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 's', 's', 'w', 's', 'e', 'e', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'e', 'e', 'w', 'n', 'e', 'w', 's', 'w', 'w', 's', 'n', 'w', 's', 'w', 's', 'w', 's', 'w', 'w', 'n', 'e', 'n', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 'e', 'n', 'n', 'e', 'n', 'n', 'e', 'e', 'n', 's', 'e', 'e', 'w', 'n', 's', 'w', 'w', 'n', 's', 'w', 's', 's', 'w', 'n', 's', 's', 's', 'w', 's', 'w', 's', 'w', 'n', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 's', 'w', 'n', 'w', 'w', 'w', 'n', 's', 'w', 'w', 'w', 's', 'w', 's', 'w', 'w', 'w', 'n', 's', 's', 'w', 's', 'e', 's', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 'w', 'w', 's', 'w', 's', 'n', 'e', 'n', 'e', 'e', 'e', 'n', 's', 'e', 'e', 'e', 's', 's', 's', 's', 's', 's', 'w', 'e', 'n', 'e', 'e', 's', 's', 'e', 'w', 's', 'w', 'e', 'n', 'n', 'n', 'w', 's', 'n', 'w', 'n', 'n', 'n', 'w', 's', 's', 's', 'n', 'n', 'w', 's', 'w', 'e', 's', 'w']
