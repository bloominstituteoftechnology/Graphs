import sys
sys.path.insert(1, '/Users/Sheila/Documents/Github/Graphs/projects/graph')# I think I should find it locally, just incase
from util import Stack, Queue
from room import Room
from player import Player
from world import World

import random
import collections
from ast import literal_eval

##SETUP##

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt" #end result

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()  #n,s,e,w Implement a stack and a dictionary
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
#player in current room, what room is it, if the room is not visited player exits current room
#if player has not exited room, then player pop off to next room
#if player hasnt visited a room the patient will travel to next room in specified direction, and add to path
#player needs to be able to travel backwards also
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#implement quick test
#test the traversal
#test includes pass or fail

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
