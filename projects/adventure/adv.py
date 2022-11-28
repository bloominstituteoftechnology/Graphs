from room import Room
from player import Player
from world import World

import random
from random import choice
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

visited = set()

player.current_room = world.starting_room

visited.add(player.current_room.id)

prv = ""

nxt = ""

exits = dict()

nxt = "e"

traversal_path.append(nxt)

while len(visited) < 500:

    player.travel(nxt)

    visited.add(player.current_room.id)

    prv = nxt

    if prv == "e":

        if "s" in player.current_room.get_exits():

            nxt = "s"

        elif "e" in player.current_room.get_exits():

            nxt = "e"

        elif "n" in player.current_room.get_exits():

            nxt = "n"

        else:

            nxt = "w"

    elif prv == "w":

        if "n" in player.current_room.get_exits():

            nxt = "n"

        elif "w" in player.current_room.get_exits():

            nxt = "w"

        elif "s" in player.current_room.get_exits():

            nxt = "s"

        else:

            nxt = "e"

    elif prv == "n":

        if "e" in player.current_room.get_exits():

            nxt = "e"

        elif "n" in player.current_room.get_exits():

            nxt = "n"

        elif "w" in player.current_room.get_exits():

            nxt = "w"

        else: 

            nxt = "s"

    elif prv == "s":

        if "w" in player.current_room.get_exits():

            nxt = "w"

        elif "s" in player.current_room.get_exits():

            nxt = "s"

        elif "e" in player.current_room.get_exits():

            nxt = "e"

        else: 

            nxt = "n"

    if len(player.current_room.get_exits()) == 4:

        curr = player.current_room.id

        if curr not in exits:

            exits[curr] = []

        if nxt not in exits[curr]:

            exits[curr].append(nxt)

        elif len(exits[curr]) < 4:

            nxt = choice([i for i in ["n", "s", "e", "w"] if i not in exits[curr]])

            exits[curr].append(nxt)

        else:

            nxt = exits[curr][len(exits[curr]) % 4]

            exits[curr].append(nxt)

    traversal_path.append(nxt)

    if len(traversal_path) > 2000:

        break

# print("Rooms visited: ", len(visited))

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
