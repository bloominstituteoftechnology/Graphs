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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
"""
Traversal:
Needs player, the world, and the room_graph
7 8 9
4 5 6
1 2 3
If player is in 5, connected rooms are 2, 4, 6, 8
Need structures for:
Path - list
Each room (for connected rooms) - stack
Visited room - stack
We need a new structure for each room, so in each function call/iteration of loop:
New queue for each room's connected rooms
Loop stops when len(visited_rooms) == len(world.rooms)
current_room goes on stack
Add current_room to visited_rooms
Add connecting_rooms to queue
Get connecting rooms with graph[current_room][1]
284: [(4, 16), {'n': 470, 's': 349, 'e': 254, 'w': 368}]
Check if they are in visited
If connecting_rooms are not in visited_rooms
Add them to queue
Set next_room to first item in queue
Add it to the stack
If next_room is in connecting_rooms: 
Set to current room and add it to path
Rerun until 44 is satisfied?
"""


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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
