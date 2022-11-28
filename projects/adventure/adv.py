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
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

''' WORK HERE '''
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
paths_stack = []
visited = set()
inverse_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

# Main Loop
while len(visited) < len(world.rooms):
    # Add room to visited, get current availabe exits, path to hold available directions in a given room
    visited.add(player.current_room)
    exits = player.current_room.get_exits()
    path = []
    
    # Adding possible exit to path (stack)
    for exit in exits:
        if player.current_room.get_room_in_direction(exit) not in visited:
            path.append(exit)

    # If there is a possible path still needing exploration select from available randomly
    if len(path) > 0:
        direction = random.randint(0, len(path) - 1)
        paths_stack.append(path[direction])
        player.travel(path[direction])
        traversal_path.append(path[direction])
    # Else pop from stack and add reverse directions
    else:
        dead_end = paths_stack.pop(-1)
        player.travel(inverse_directions[dead_end])
        traversal_path.append(inverse_directions[dead_end])

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# Traversal path list tested here
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

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
