# Import libraries, packages, modules, functions:

# External
from ast import literal_eval
import random

# Internal for this project:
from data_structures import Stack, Queue
from map import Map
from room import Room
from player import Player
from world import World


# Fixed constants:
directions = ["n", "s", "w", "e"]
opposite_direction = {"n": "s", "s": "n", "w": "e", "e": "w"}
threshold_unexplored_neighbors = 3


# -----------------------------------------------------------------------------
# SETUP & LOAD MAP:

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

# # Print an ASCII map
world.print_rooms()

# -----------------------------------------------------------------------------
# TRAVERSAL: Traverse all of the rooms:

# Initialize traversal path as empty list (no rooms visited yet):
traversal_path = []  # traversal_path = ['n', 'n']

# Initialize player, and put player in starting_room:
player = Player(world.starting_room)

# DFT w/ improved retrace for efficiency:

map = Map()

# Initialize stack:
rooms_to_visit = Stack()

current_room = player.current_room

rooms_to_visit.push(current_room.id)

sort_order = [dir for dir in ["e", "w", "s", "n"]]
exits = sorted(current_room.get_exits(), key=lambda direction: sort_order.index(direction))
neighbors = {direction:current_room.get_room_in_direction(direction).id for direction in exits}
# neighbors = {direction:current_room.get_room_in_direction(direction).id for direction in current_room.get_exits()}
neighbors["placeholder"] = 0  # [?? To do: REMOVE/fix this! ??]

while rooms_to_visit.size() > 0:
    # Get nearest room that is not yet visited from stack:
    next_room_id = rooms_to_visit.pop()

    # If the next room in our rooms_to_visit stack has not already been visited+processed, visit and process it:
    if next_room_id not in map.rooms:
        if next_room_id not in neighbors.values():
            assert set(neighbors.values()).issubset(map.rooms.keys())
            # If all of this room's neighbor's have already been explored:
            if set(neighbors.values()).issubset(map.rooms.keys()):
                # Go back:
                retrace_path = map.bfs(starting_room=current_room.id, target_room=next_room_id)

                for direction in retrace_path:
                    player.travel(direction=direction, show_rooms=True)
                    traversal_path.append(direction)
                    current_room = player.current_room
                    # sort_order = [dir for dir in ["e", "w", "s", "n"]]
                    exits = sorted(current_room.get_exits(), key=lambda direction: sort_order.index(direction))
                    neighbors = {direction:current_room.get_room_in_direction(direction).id for direction in exits}
                    # neighbors = {direction:current_room.get_room_in_direction(direction).id for direction in current_room.get_exits()}
            
            # else:
            #     print(f"WAIT! We MISSED some neighbors of room # {current_room.id}! \nThe neighbors are: {set(neighbors.values()) - set(map.rooms.keys())}")
        
        # Travel to current room (if not already in that room):
        if player.current_room.id is not next_room_id:
            for dir in neighbors:
                if neighbors[dir] == next_room_id:
                    direction_to_travel = dir
            player.travel(direction=direction_to_travel, show_rooms=True)
            # Add the direction you traveled to traversal_path:
            traversal_path.append(direction_to_travel)
        
        current_room = player.current_room

        # sort_order = [dir for dir in ["e", "w", "s", "n"]]
        exits = sorted(current_room.get_exits(), key=lambda direction: sort_order.index(direction))
        neighbors = {direction:current_room.get_room_in_direction(direction).id for direction in exits}
        # neighbors = {direction:current_room.get_room_in_direction(direction).id for direction in current_room.get_exits()}

        map.add_room(room_id=current_room.id, neighbors=neighbors)

        # Add current_room's neighbors to our stack to visit next:
        for room in neighbors.values():
            if room not in map.rooms: # and room not in rooms_to_visit.stack
                rooms_to_visit.push(room)
    
    # Otherwise: If the next room in our rooms_to_visit stack has been visited+processed already, 
    # then skip it and go to the next room in the stack:
    else:
        continue


# -----------------------------------------------------------------------------
# TESTS:
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

# # ######
# # UNCOMMENT TO WALK AROUND
# # ######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
