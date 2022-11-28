from room import Room
from player import Player
from world import World

import random
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
# traversal_path = ['n', 'n', 's', 's', 's', 's', 'n', 'n', 'e', 'e', 'w', 'w', 'w', 'w']
traversal_path = [] 

#to reverse directions 
inverse_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

#PLAN:
# set up direction for player
# loop thru all the exits 
# set up if player has visited the current room to turn around 
# else if the room hasnt been visited to add the new path 
# and update the status to the new one using recursion 
# return the path 
#fill in the traversal path with the traverse func

def traverse(starting_room, visited=set()):
    #tracking the new path in a list
    path = []
    # looping thru the get_exits to find all exits
    for direction in player.current_room.get_exits(): #using get exits from room py
        player.travel(direction)
        
        if player.current_room in visited: 
            #if a player is in a room that is visited, then turn to another direction by using inverse_direct
            player.travel(inverse_directions[direction]) 

        else: 
            #if the room has not been visited add the new path
            visited.add(player.current_room)
            path.append(direction)

            #recurse to update current status
            path = path + traverse(player.current_room,visited)
            player.travel(inverse_directions[direction])
            path.append(inverse_directions[direction])

    return path

#fills in the list w the traverse func
traversal_path = traverse(player.current_room)


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
