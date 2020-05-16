from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval #<-- What is that? Check Python Docs

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

# traversal_path = ['n', 'n']
traversal_path = []

#This traversal graph needs to have 'helper functions listed that will do the following things: 

#Pseudocode
# Make a BFS Function
#1. Place starting room in the unvisited queue
#2. While queue is not empty, place 
#Conditions:
#MOVEMENTS!!!!
#Besides the dft process
#If the first unvisited room is east MOVE east, if west, move west, so on and so forth
#If the room is visited, display the exits
#If the exit is to the east MOVE east, so on and so forth, ***Consider writing a function for this because it's becoming repetitive***
#If len(unvisited) < len(room_graph), find unvisited 
#If len(visited) == len(room_graph), traversal complete



        

#    
#Problem:
#The goal is to move from one room to the next in under 2000 steps (Goal is actually 950), the strategy is to only visit one room going in one direction around the map.  The problem is if we go in 1 direction, how do we backtrack if the player reaches a dead end?

#Solution:
#Move the player to a random room
#Has room been 
#If the player hits a dead-end (meaning no other attached rooms), mark the dead end room as `unvisited`.  This enables the player to backtrack to the previous room and explore another adjacent room which will enable the player to traverse to the other adjacent room and find another path around the map until all rooms have been visited


# TRAVERSAL TEST
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


#######
# UNCOMMENT TO WALK AROUND
#######
# while True:
#       cmds = input("-> ").lower().split(" ")
#        if cmds[0] in ["n", "s", "e", "w"]:
#             player.travel(cmds[0], True)
#         elif cmds[0] == "q":
#             break
#         else:
#             print("I did not understand that command.")


# if n < limit:
    #     room_list = list(world.print_rooms())
    #     i = 0
    #     complete = False

    #     while i < len(room_list) and not complete:
    #         #If visited is none, we're going initialize it to equal set
    #         if visited is None:
    #             visited = set()
    #             traversal_path.append(n)
    #     #If the room has not been visited, add to visited
    #         if player not in visited:
    #             visited.add(player.current_room)
    #             Room.get_exits()
    #             complete = adventure_moves(n+1, traversal_path, room_list[i],limit)
    #         i + 1



    

