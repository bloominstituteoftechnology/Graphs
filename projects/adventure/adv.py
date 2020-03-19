from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

#load file to read graph
# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
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
traversal_path = [] #path traveled to visit room

#reverse direction
reverse_dir = {'n':'s', 's':'n', 'e': 'w', 'w':'e'}

#track reverse path 
reverse_path = []

rooms = {} #set dictionary to iterate through exits

#Add room zero to rooms
rooms[0] = player.current_room.get_exits()

#while rooms visited is less than the total number of rooms:
while len(rooms) < len(room_graph)-1:
    #If room hasnt been visited..
    if player.current_room.id not in rooms:
        #add exits for current room to rooms
        rooms[player.current_room.id] = player.current_room.get_exits()
        #grab last direction traveled
        last_dir = reverse_path[-1]
        # remove exit from exits
        rooms[player.current_room.id].remove(last_dir)

    #while there arent any rooms left
    while len(rooms[player.current_room.id]) < 1:
        #pop last direction in reverse path
        reverse = reverse_path.pop()
        #Add reverse direction to traversal_path and travel that way
        traversal_path.append(reverse)
        player.travel(reverse)
        player.travel(reverse)

    #Travel in first ready exist direction inside of room
    exit_dir = rooms[player.current_room.id].pop(0)
    #Add traversal path
    traversal_path.append(exit_dir)
    #Add reverse direction to path
    reverse_path.append(reverse_dir[exit_dir])
    #travel
    player.travel(exit_dir)



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
        print("Que? The wise space dog does not understand")
