from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

import sys
sys.path.append(r"C:\Users\Samuel\repos\Graphs\projects\graph")

# `from graph import Graph`
from util import Queue, Stack
import operator
import time

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\test_line.txt"
map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\test_cross.txt"
# map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\test_loop.txt"
# map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\test_loop_fork.txt"
# map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\main_maze.txt"

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
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# Passed Line Test:

# while player.current_room.n_to:
#     player.current_room = player.current_room.n_to
#     traversal_path.append('n')


# Pass Cross Test:

# Implement DFT using dictionary as a graph

# Create adjacency_dict
adjacency_dict = {}

# adjacency_dict[player.current_room.id] = {
#     "n": player.current_room.n_to.id,
#     "s" : player.current_room.s_to.id,
#     "e" : player.current_room.e_to.id,
#     "w" : player.current_room.w_to.id
#     }

# adjacency_dict[player.current_room.id] = {}

# attributes = ["n_to", "s_to", "e_to", "w_to"]
# for attr in attributes:
#     if operator.attrgetter(f"current_room.{attr}")(player):
#         adjacency_dict[player.current_room.id][attr[0]] = operator.attrgetter(f"current_room.{attr}.id")(player)
#     else:
#         adjacency_dict[player.current_room.id][attr[0]] = operator.attrgetter(f"current_room.{attr}")(player)

# for direction in adjacency_dict[player.current_room.id]:
#     print(direction, adjacency_dict[player.current_room.id][direction])


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
