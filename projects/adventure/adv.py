from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "/Users/chrisgonzales/Documents/LambdaCS/LambdaCS/Unit II/Graphs/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

''' 
To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:

```
{
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}
```

You know you are done when you have exactly 500 entries (0-499) in your graph and no `'?'` in the adjacency dictionaries. To do this, you will need to write a traversal algorithm that logs the path into `traversal_path` as it walks.

Your solution **must** generate the solution by using graph traversal algorithms. Hardcoding a solution is not acceptable.

'''

world_map = {}

def master_explorer(player: Player, dungeon: World):

    # Grab the starting room from the player (player.currentRoom)
    # Create a current path queue
    # Create a room counter

            ## MOVE METHOD ##
            
    # Add the current room to the world_map
    # Increment the room counter
    # Connect the current room to the previous room (if not the first room)
    # Check the exits in the current room
    # Enqueue the current room in the current_path queue
    # Move to a random ?
    # Log the direction in traversal_path

            ## Repeat until no ?'s in the current room
            # -- This means the room either has one door and four walls, or some combo of identified rooms and walls
    
    # Do a BFS to find the nearest ? in the current_path
    # Log the BFS path
    # Add the BFS path to the traversal_path
    # Move to the nearest ? 
    # Clear the current path
    # Repeat the Move Method

        ## Repeat while the counter is less than 500
    



# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
