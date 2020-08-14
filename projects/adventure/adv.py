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
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path is the list of results/moves to go through the rooms
# Reverse directions so that each room can be the equivalent the opposites direction room move
# path is a list to keep track of where to go when we need to reverse our steps
# visit dictionary to have rooms as key and directions as value

# First add players current room to visited, directions will be the exits (‘neighbors’)

# REPL — while visit is still less than the graph of rooms -1, we’ll do all the steps
#when len of visit is the length of graph, it will end the loop

    # Step one, check if that current room’s id is in visit
    # If not, 
        # add to visit
        # Create a variable for the last room/direction in the path
        # Remove the last direction from visited — this will remove direction from visited
        # because we know that direction leads to the room we were just in


#Step two (after each move we need to mark it):
    #Create a variable for the first direction in current room--the move we just made
    #Add that variable to traversal path to track where we've gone
    #add the rooms opposite direction to path (next room to go to) -- so that we can go back if needed
    #let player move through directions




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