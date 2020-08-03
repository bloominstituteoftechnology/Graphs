from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#JENN'S (JHL) CODE - HERE GOES NOTHING!!
'''Steps:
Step 1: Describe in graphs terminology
-- What are the nodes? The rooms
-- What are the connections/ when are the nodes connected? 
--- The exits/directions of NSEW
You may find the commands `player.current_room.id`,
`player.current_room.get_exits()` and `player.travel(direction)` useful.
'''

# keep track of "reverse" directions
# use this to return to a room with valid moves
reverse_path = []

#instantiate a set to keep track of visited rooms
visited = {}

#set directions for going back
reverse_directions = {'n' : 's', 's' : 'n', 'e' : 'w', 'w' : 'e'}

# Step 2: Build your graph OR define a get_neighbors function
## -- NOT using a graph per say because the code doesn't call for a graph
# and I am too lazy to refactor all of the code to accommodate it. 

# WHERE AM I AND HOW DO I GET OUT??
#current room
current_room = player.current_room.id

#add current room to visited set
visited_room = visited[current_room]

#find an escape path
exits = player.current_room.get_exits()

# Step 3: Choose graph algorithm - DFT(ish)
        
while len(visited) < len(room_graph) - 1:
    if current_room not in visited:
        #add the current room to the dict and find the exits
        visited_room = exits
        # iterate over exits and remove one by one
        for exit in exits:
            visited_room.remove(reverse_path[-1])
    
    while len(visited_room) == 0:
        #map the path back the way we came
        go_back = reverse_path.pop()
        traversal_path.append(go_back)
        #move the player back too
        player.travel(go_back)
    
    next_room = visited_room.pop()
    traversal_path.append(next_room)
    reverse_path.append(reverse_directions[next_room])
    player.travel(next_room)

# TRAVERSAL TEST - DO NOT MODIFY
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")