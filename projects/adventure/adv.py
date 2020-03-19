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
# traversal_path = ['n', 'n']
traversal_path = []

# Reservse Directions 

reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# Path for backtracking 

reverse_path = []

# Rooms

rooms = {}

# Start with empty list
# Iterate through rooms and find exits
# Check for duplicates
# Append valid exits
def find_exits(current_room, visited):
    valid_exits = []
    for exit in current_room.get_exits():
        if room_graph[current_room.id][1][exit] not in visited:
            valid_exits.append(exit)
    return valid_exits

# While visited rooms is less than 500 total rooms

# Add first room to visited
# Count variable declaration 
# Grab the reversed traversal
# Get copy of current room and loop through rooms that have valid exits
# Iterate over directions in current rooms that have valid exits
# Append to visited list
# Handle opposite direction (Reverse Traversal)
# Player moves to current room
# Invoke function

def traverse_maze():
    visited = set()
    visited.add(player.current_room.id)
    reverse_path = []

    while len(visited) < len(room_graph.keys()):
        # Setting the current room id to current room
        current_room = player.current_room.id
        # Setting the exits we have found to valid exits
        valid_exits = find_exits(player.current_room, visited)
        print(valid_exits)

        # If valid exits is > 0
        if len(valid_exits) > 0:
            for direction in valid_exits:
                visited.add(room_graph[current_room][1][direction])
                traversal_path.append(direction)
                reverse_path.append(reverse_direction[direction])
                player.travel(direction)
                # Will skip else if statement if found
                break
        else:
            print(reverse_path)
            direction = reverse_path.pop()
            player.travel(direction)
            traversal_path.append(direction)
traverse_maze()
                


        
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
