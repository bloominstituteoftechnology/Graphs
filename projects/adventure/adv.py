### IMPORT ###

import sys
sys.path.insert(1, '/Users/ShawnJames/Developer/Github/Graphs/projects/graph') #change location to wherever graph file is located locally
from util import Stack, Queue

from room import Room
from player import Player
from world import World

import random
import collections
from ast import literal_eval

### SETUP ###

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt" <-- this one should be final

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

### PROPERTIES ###

visited = set()
backtrack = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
stack = Stack()
dictionary = {}

## LOGIC ##

while len(visited) < len(room_graph):
    currentRoomId = player.current_room.id
    if currentRoomId not in visited:
        visited.add(currentRoomId)
        exits = player.current_room.get_exits()
        dictionary[currentRoomId] = exits

    numExits = len(dictionary[currentRoomId])
    while numExits > -1:
        if numExits is not 0:
            direction = dictionary[currentRoomId].pop()
            if player.current_room.get_room_in_direction(direction).id not in visited:
                stack.push(direction)
                player.travel(direction)
                traversal_path.append(direction)
                break
                
        numExits = len(dictionary[currentRoomId])
        if numExits is 0:
            prevMove = stack.pop()
            prevDirection = backtrack[prevMove]
            player.travel(prevDirection)
            traversal_path.append(prevDirection)
            break

### QUICK TEST ###

if len(visited) == len(room_graph):
    print("It worked!")

### MORE TESTING ###

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
#player.current_room.print_room_description(player)
#while True:
#    cmds = input("-> ").lower().split(" ")
#    if cmds[0] in ["n", "s", "e", "w"]:
#        player.travel(cmds[0], True)
#    elif cmds[0] == "q":
#        break
#    else:
#        print("I did not understand that command.")