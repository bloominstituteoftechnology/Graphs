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
visited = {} # added visited dictionary
reverse_path = [] # added reverse path for storing the backtracking
opposite_direction = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'} #added opposite directions for backtracking 

visited[player.current_room.id] = player.current_room.get_exits() # added the first room to the visited dictionary and get its exits 

while len(visited) < len(room_graph): # while the visited list is less than the length of rooms in the graph 
    if player.current_room.id not in visited: # if not visited 
        visited[player.current_room.id] = player.current_room.get_exits() # add it to the visited and get the rooms 
        prev_direction = reverse_path[-1] # access direction just visited and remove it from the unexplored paths/ we have came from that direction 
        visited[player.current_room.id].remove(prev_direction)

    if len(visited[player.current_room.id]) == 0: # if the length of the paths associated with the room is 0 when all the paths have been explored
        prev_direction = reverse_path[-1] # backtracking to the previous room until a room with unexplored path is found 
        reverse_path.pop() # assign the last addition to the reverse path as the previous direction and pop it from reverse path 
        traversal_path.append(prev_direction) # adding the previous direction to the traversal path 
        player.travel(prev_direction) # moves the player into that direction

    else: # if there is an unexplored direction/ add the direction to the traversal path/ explore new room
        direction = visited[player.current_room.id][-1] # the first available direction in the room, assign it to direction and pop it from the list
        visited[player.current_room.id].pop()
        traversal_path.append(direction) # add the direction to the traversal path 
        reverse_path.append(opposite_direction[direction]) # record the opposite direction to the move in the reverse path 
        player.travel(direction) # move the player in that direction 

       # import random do some random shuffle 


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
        
# First pass solution: 
# Record the room in visited
# Get all the exits with the room.
# Move in one direction, add this to the traversal path and pop it off the directions associated with the room
# Work out the opposite direction and add this to a reverse path so that backtracking is possible and remove the opposite direction from the unexplored paths
# Get exits for the new room and keep note of this (in visited)
# Move in a random direction again and add to the traversal path and pop it off the possible directions
# Keep moving until you reach a dead end
# When there are no more unexplored exits - backtrack along the last direction on the backtracked path and remove it from the backtracked path and add it to the traversal path
# Check that room for unexplored directions and repeat the process again
# This keeps going until the number of rooms visited reaches the length of the rooms graph