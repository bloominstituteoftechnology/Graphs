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

backtrack = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
#visited = set() #keep track of where have been
#visited = {}
visited = []
stack = Stack()  #pop when stuck, push when moving
moveCount = 0 #how many moves did this take to accomplish?

### METHODS ###

startingRoom = player.current_room
stack.push(startingRoom)

while stack.size() > 0:
    currentRoom = stack.pop()
    print(currentRoom)
    if currentRoom not in visited:
        visited.append(currentRoom)
        
        #enqueue neighbors
        directionsOfNeighbors = player.current_room.get_exits() #get direction of neighbors
        
        for direction in directionsOfNeighbors:
            if direction == 'n':
#                print(currentRoom.n_to)
                if currentRoom.n_to != None:
                    stack.push(currentRoom.n_to)
            elif direction == 's':
#                print(currentRoom.s_to)
                if currentRoom.s_to != None:
                    stack.push(currentRoom.s_to)
            elif direction == 'e':
#                print(currentRoom.e_to)
                if currentRoom.e_to != None:
                    stack.push(currentRoom.e_to)
            else: # direction == 'w':
#                print(currentRoom.w_to)
                if currentRoom.w_to != None:
                    stack.push(currentRoom.w_to)

if len(visited) == len(room_graph):
    print("it worked!")

#        for neighbor in neighbors:
#            print(neighbor)
#            stack.push(neighbors)
        

        

#startingRoom = player.current_room.id
#stack.push(startingRoom)
#
#while stack.size() > 0:
#    room = stack.pop()
#    if room not in visited:
#        visited.add(room)
#        neighbors = player.current_room.get_exits() #get neighbors
#        for neighbor in neighbors:
#            print(player.current_room.n_to)
#            stack.push(neighbors)

#visited[player.current_room.id] = player.current_room.get_exits()
#
#while len(visited) < len(room_graph):
#    startingRoomId = player.current_room.id
#    
#    if startingRoomId not in visited:
#        visited[startingRoomId] = player.current_room.get_exists() #startingRoomId : neighbors
#        print(visited)

#startingRoom = player.current_room.id
#stack.push(startingRoom)
#
#while stack.size() > 0:
#    nextRoom = stack.pop()
#    if nextRoom not in visited:
#        visited.add(nextRoom)
#        # add neighbors
#        neighbors = player.current_room.get_exits() #get neighbors
#        for neighbors in neighbors:
#            stack.push(neighbors)
#            
#if len(visited) == len(room_graph):
#    print("Test passed")
#else:
#    print(len(visited))
#    print(len(room_graph))
#    print(visited)

#while len(visited) < len(room_graph): # (or while stack is not empty)
#    stack.push = player.current_room.id

#def dft(map, player, path, trail):
#    while len(visited) != len(room_graph):
#        currentRoom = player.current_room.id
#        if currentRoom not in visited:
#            visited.add(currentRoom)
#            
#            neighbors = player.current_room.get_exits() #get neighbors
#            # add exits to dictionary
            
#def dft():
#    stack = Stack()
#    visited = set()
#
#    currentRoom = player.current_room.id
#    stack.push(currentRoom) #prime the stack with starting value
#
#    while stack.size() > 0:
#        
##        moveCount += 1
#        
#        room = stack.pop()
#        if room not in visited:
#            visited.add(room)
#            print(room)
#            neighbors = player.current_room.get_exits() #get neighbors
#            for neighbors in neighbors:
#                stack.push(neighbors)

### TESTING ###

# TRAVERSAL TEST
#visited_rooms = set()
#player.current_room = world.starting_room
#visited_rooms.add(player.current_room)
#
#for move in traversal_path:
#    player.travel(move)
#    visited_rooms.add(player.current_room)
#
#if len(visited_rooms) == len(room_graph):
#    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
#else:
#    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

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