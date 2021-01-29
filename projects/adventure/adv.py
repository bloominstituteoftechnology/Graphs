from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"  # FINAL MAP — your solution must be able to handle this

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

####################################
#
#
#
#
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
#
#
####################################
player = Player(world.starting_room)
traversal_path = []
opposite_directions = {
    "n": "s",
    "e": "w",
    "s": "n",
    "w": "e"
}
traversal_graph = {}


# Start by writing an algorithm that
#  - picks a random, unexplored direction from the players current room,
#  - travels and LOGS that direction,
#  - then loops.
#
# This should cause your player to walk a depth-first traversal.
# When you reach a dead-end, walk back to the nearest room
# that does contain an unexplored path
count = 1
current_room = 0
print(room_graph)
def dft_explore(last_room=None):
    # if not last_room:
    #     last_room = ['n', '?']
    exits = player.current_room.get_exits()
    # exits = room_graph[current_room].get_exits()
    # viable = False
    viable_exits = []
    for exit in exits:
        if exit == "?":
            # viable = True
            viable_exits.append(exit)
    print(exits)
    print(viable_exits)

    if not viable_exits:
        print("no unexplored exits")
        return

    if player.current_room.id not in traversal_graph:
        traversal_graph[player.current_room.id] = {direction: "?" for direction in exits}
        if last_room is not None:
            traversal_graph[player.current_room.id][last_room[0]] = last_room[1]

    # if "?" not in player.current_room.get_exits():
    next_direction = random.choice(viable_exits)
    # player.travel(next_direction)
    traversal_path.append(next_direction)
    dft_explore([player.current_room.id, next_direction])
    print(next_direction)
    print(traversal_graph)

    # return


dft_explore()
print(traversal_graph)
# print(f"current_room={player.current_room.description}")
# print(f"current_room.id={player.current_room.id}")
# print(f"current_room.get_exits()={player.current_room.get_exits()}")

####################################
# TEST CODE
####################################
#
#
#
#
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
