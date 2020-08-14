from room import Room
from player import Player
from world import World
import random
from ast import literal_eval

from util import Stack, Queue

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

# get the room exits and mark as unvisited
def get_paths(room):
    paths = {}

    for i in room.get_exits():
        paths[i] = "?"
    
    return paths

# get the opposite direction
def reverse(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"

def explore(room, visited = None):
    # if no visited set, create one
    if visited is None:
        visited = set()

    # initialize the traversal path
    traversed_path = []

    # get the possible exits for the current room
    for direction in get_paths(room):
        # travel in available directions
        player.travel(direction)

        # check if room has been visited:
        if player.current_room.id not in visited:
            # add room to visited
            visited.add(player.current_room.id)
            # add the direction to the traversed path
            traversed_path.append(direction)
            # recursively call explore for the new current_room
            traversed_path += explore(player.current_room, visited)
            # travel in the opposite direction
            player.travel(reverse(direction))
            # append the opposite movement to the traversed path
            traversed_path.append((reverse(direction)))
        else:
            # room already visited, travel in opposite direction
            player.travel(reverse(direction))
    
    return traversed_path

traversal_path = explore(player.current_room)
    
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
