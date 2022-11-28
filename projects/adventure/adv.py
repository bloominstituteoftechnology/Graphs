#import sys
#sys.path.insert(1, '/Users/Sheila/Documents/Github/Graphs/projects/graph')# I think I should find it locally, just incase

from room import Room
from player import Player
from world import World

import random

from ast import literal_eval #Safely evaluate an expression node

##SETUP##

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# keep track of "reverse" directions
# use this to return to a room with valid moves
backtrack = []
reversed_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# instantiate a set to keep track of visited rooms
visited = set()

# while there are still unvisited rooms
while len(visited) < len(room_graph):

    # initialize next move as None
    next_move = None

     # for each exit(neighbor) in the room expressed by (n,s,e,w)
    for exit in player.current_room.get_exits():
         # for each exit, if its not been visited, set as the next move
        if player.current_room.get_room_in_direction(exit) not in visited:
            next_move = exit
            # some rooms have multiple exits, this will break the loop
            # upon the first non-visited exit. It doesn't improve moves
            # but it is slightly faster runtime
            break

    # if there is a viable move...
    if next_move is not None:

        # append the move to the traversal_path
        traversal_path.append(next_move)

        # add the reversed direction to the breadcrumb trail
        backtrack.append(reversed_directions[next_move])

        # make the move and add room to visited list
        player.travel(next_move)  
        visited.add(player.current_room)

    else:
        # there is no valid room -> use backtrack to go back and find a room
        # with a valid move

        # pop the last entry from backtrack
        next_move = backtrack.pop()

        # add that move to traversal path
        traversal_path.append(next_move)

        # make the move
        player.travel(next_move)



# TRAVERSAL TEST
visited_rooms = set()  #n,s,e,w Implement a stack and a dictionary
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

#My Uper Thought process
#player in current room, what room is it, if the room is not visited player exits current room and goes to the next room
#player needs to be able to exit current room
#if player hasnt visited a room then will travel to next room in specified direction, and add to path/visted rooms
#player needs to be able to travel backwards also
#look at what is in room.py, world.py, and player.py
#test the traversal
#test includes pass or fail





#######
# UNCOMMENT TO WALK AROUND
#######
#player.current_room.print_room_description(player)
#while True:
    #cmds = input("-> ").lower().split(" ")
    #if cmds[0] in ["n", "s", "e", "w"]:
      #  player.travel(cmds[0], True)
   # elif cmds[0] == "q":
       # break
    #else:
       # print("I did not understand that command.")
