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
import os.path
map_file = "maps/main_maze.txt"
map_file = os.path.join(os.path.dirname(__file__), map_file)

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
visited = set()
opposite_dir = { 'w': 'e', 'e': 'w', 'n': 's', 's': 'n' }

def dfs(visited, room, traversal_path, direction):
    if room.name not in visited:
        if direction:
            traversal_path.append(direction)
        visited.add(room.name)
        for exit in room.get_exits():
            room_in_dir = room.get_room_in_direction(exit)
            if room_in_dir.name not in visited:
                dfs(visited, room_in_dir, traversal_path, exit)
                traversal_path.append(opposite_dir[exit])

dfs(visited, player.current_room, traversal_path, "")
 
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

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
