from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval #<-- What is that? Check Python Docs

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
walking_directions = {'n': 's', 's': 'n', 'e': 'w','w': 'e'}

# traversal_path = ['n', 'n']
traversal_path = []

#Problem:
#The goal is to move from one room to the next in under 2000 steps (Goal is actually 950), the strategy is to only visit one room going in one direction around the map.  The problem is if we go in 1 direction, how do we backtrack if the player reaches a dead end?


def dfs_path(room, visited=None):
    #If visited is none, we're going initialize it to equal set
    if visited is None:
        visited = set()
    explored_path = []
        #If the room has not been visited, add to visited
    visited.add(room.id)
        #For each room, we want to check for exits
    for exit in room.get_exits():
        next_room = room.get_room_in_direction(exit)
        if next_room.id not in visited:
            #Now that we have visited our first room, we can carry onto the next room with recursion and determine the path. 
            path_has_no_dead_ends = dfs_path(next_room, visited)
            if path_has_no_dead_ends:
                 #Update the path with each visit--check for exits, and this time, include walking directions.
                current_path = [exit] + path_has_no_dead_ends + [walking_directions[exit]]
            else:
                    #If path does have dead ends, backtrack.  Leave out the path that has no dead ends and show the walking directions with just an exit (no other rooms present).
                current_path = [exit, walking_directions[exit]]
                #The explored path will now include the explored path with the current path, in either case
            explored_path = explored_path + current_path

    return explored_path

#Now we assign the dfs function to the traversal path with the player in the current room
traversal_path = dfs_path(player.current_room)
            

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

print("")
# print traversal path
# print(f"traversal-path: {traversal_path}")
print("")

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
