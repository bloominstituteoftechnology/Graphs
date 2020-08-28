import sys
sys.path.insert(1, '/Users/Sheila/Documents/Github/Graphs/projects/graph')# I think I should find it locally, just incase
from util import Stack, Queue
from room import Room
from player import Player
from world import World

import random
import collections
from ast import literal_eval #Safely evaluate an expression node

##SETUP##

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
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

#Rooms Visited So Far
visited = set()
backtrack = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'} #How we will track our moves. Needs to be able to track forward to next move and backwards
stack = Stack() #implemented stack
dictionary = {} #implemented dict

# Add room to list once visited 
while len(visited) < len(room_graph):
    currentRoomId = player.current_room.id #which room is the player in?
    if currentRoomId not in visited: #if current room has not been visited yet then add to visited rooms
        visited.add(currentRoomId)
        exits = player.current_room.get_exits() #how to exit the room
        dictionary[currentRoomId] = exits

numExits = len(dictionary[currentRoomId])
while numExits > -1:
        if numExits != 0:
            direction = dictionary[currentRoomId].pop()#if i have been here before then dont go or get out.
            if player.current_room.get_room_in_direction(direction).id not in visited: #Travel to a room that hasn't been visited
                stack.push(direction)
                player.travel(direction)
                traversal_path.append(direction)
                break
        #how to back track        
        numExits = len(dictionary[currentRoomId])
        if numExits == 0:
            prevMove = stack.pop()
            prevDirection = backtrack[prevMove]
            player.travel(prevDirection)
            traversal_path.append(prevDirection)
            break

print ('Rooms I Visited', len(traveled_rooms))
print (len(traversal_path))


if len(visited) == len(room_graph):
    print("It worked!")


# TRAVERSAL TEST
visited_rooms = set()  #n,s,e,w Implement a stack and a dictionary
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

#My Uper Thought process
#player in current room, what room is it, if the room is not visited player exits current room and goes to the next room
#player needs to be able to exit current room
#if player hasnt visited a room then will travel to next room in specified direction, and add to path/visted rooms
#player needs to be able to travel backwards also
#look at what is in room.py, world.py, and player.py
#test the traversal
#test includes pass or fail
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
  #  cmds = input("-> ").lower().split(" ")
    #if cmds[0] in ["n", "s", "e", "w"]:
       # player.travel(cmds[0], True)
   # elif cmds[0] == "q":
      #  break
    #else:
      #  print("I did not understand that command.")
