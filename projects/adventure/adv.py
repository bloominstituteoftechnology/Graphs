from room import Room
from player import Player
from world import World

import random
from random import choice
from ast import literal_eval
from utils import Stack, Queue

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Helper function to get the reverse of given direction
# if player can't move in given direction he must go back
def reverse_direction(dir):
    if dir == "n":
        return "s"
    if dir == "s":
        return "n"
    if dir == "e":
        return "w"
    if dir == "w":
        return "e"

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# all moves will be in a stack 
moves = Stack()

# end point: the number of visited rooms is the total number of rooms
while len(visited_rooms) < len(world.rooms):
    # get exits from current room
    exits = player.current_room.get_exits()
    # initialize a list containing all possible directions
    available_directions = []
    # loop through all exits from current room
    for exit in exits:
        # if room in a direction is not visited append to available directions
        if exit is not None and player.current_room.get_room_in_direction(exit) not in visited_rooms:
            available_directions.append(exit)
    # Once in new room set current room to visited
    visited_rooms.add(player.current_room)

    # If there is any direction available to move/path exists
    if len(available_directions) > 0:
        # pick a random direction
        move = random.randint(0, len(available_directions) - 1)
        # push that direction onto moves stack
        moves.push(available_directions[move])
        # player travels in that direction
        player.travel(available_directions[move])
        # and we append the direction to the traversal path
        traversal_path.append(available_directions[move])

    # unless there are no other available directions
    else:
        # get the last move made
        last_move = moves.pop()
        # the player travels in the reverse direction of the las move made
        player.travel(reverse_direction(last_move))
        # and append the move to the traversal path
        traversal_path.append(reverse_direction(last_move))

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
