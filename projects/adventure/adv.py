# Import libraries, packages, modules, functions:

# External
from ast import literal_eval
from numpy import NaN
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


# -----------------------------------------------------------------------------
# LOAD MAP:

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

#DFT:

map = Map()

# Initialize stack:
rooms_to_visit = Stack()

current_room = player.current_room

rooms_to_visit.push(current_room.id)

# ---------------------------------------
# ??

neighbors = {direction:current_room.get_room_in_direction(direction).id for direction in current_room.get_exits()}
neighbors["placeholder"] = 0  # [?? To do: REMOVE/fix this! ??]

while rooms_to_visit.size() > 0:
    # Get nearest room that is not yet visited from stack:
    next_room_id = rooms_to_visit.pop()

    # If the next room in our rooms_to_visit stack has not already been visited+processed, visit and process it:
    if next_room_id not in map.rooms:
        if next_room_id not in neighbors.values():
            if set(neighbors.values()).issubset(map.rooms.keys()):
                print("Yes all neighbors already visited.")
                print("REVERSE!\n")

                retrace_path = traversal_path.copy()  # traversal_path[::-1]
                retrace_path.reverse()
                for original_direction in retrace_path:
                    reverse_direction = opposite_direction[original_direction]
                    player.travel(direction=reverse_direction, show_rooms=True)
                    print(f"original_direction: {original_direction}, reverse_direction: {reverse_direction}")
                    traversal_path.append(reverse_direction)

                # for step_back in range(-1, -len(traversal_path) - 1, -1):
                #     original_direction = traversal_path[step_back]
                #     reverse_direction = opposite_direction[original_direction]
                #     player.travel(direction=reverse_direction, show_rooms=True)
                #     traversal_path.append(reverse_direction)
                    
                    current_room = player.current_room
                    neighbors = {direction:current_room.get_room_in_direction(direction).id for direction in current_room.get_exits()}
                    if next_room_id in neighbors.values():
                        break
                print("break broke out of FOR loop but not WHILE! Good")
                # --> continue with the loop as usual?
            else:
                print(f"WAIT! We MISSED some neighbors of room # {current_room.id}! \nThe neighbors are: {[element not in map.rooms.keys() for element in neighbors.values()]}")

            print("OK we are here now! Line 98.")
        
        # Travel to current room (if not already in that room):
        if player.current_room.id is not next_room_id:
            for dir in neighbors:
                if neighbors[dir] == next_room_id:
                    direction_to_travel = dir
            # ??
            player.travel(direction=direction_to_travel, show_rooms=True)

            # (How -- 2 different stacks for immediate retracing route vs. rooms to visit??)

            # Add the direction you traveled to traversal_path:
            traversal_path.append(direction_to_travel)

            # Mark that connection for both rooms (prev and new) with add_edge on our map
        
        current_room = player.current_room

        neighbors = {direction:current_room.get_room_in_direction(direction).id for direction in current_room.get_exits()}

        map.add_room(room_id=current_room.id, neighbors=neighbors)

        for room in neighbors.values():
            if room not in map.rooms:
                rooms_to_visit.push(room)
        
        rooms_left = len(set(world.rooms.keys()) - set(map.rooms.keys()))

        if rooms_left < 160:
            print("rooms left < 160")
    
    # Otherwise: If the next room in our rooms_to_visit stack has been visited+processed already, 
    # then skip it and go to the next room in the stack:
    else:
        rooms_left = len(set(world.rooms.keys()) - set(map.rooms.keys()))

        if rooms_left < 160:
            print("rooms left < 160")

        print(f"Rooms left to visit: {rooms_left} \nWhich rooms: {set(world.rooms.keys()) - set(map.rooms.keys())}")
        continue


print(map)
print(rooms_to_visit)
print(traversal_path)
print(f"map.rooms: {map.rooms.keys()} should contain everything in {[world.rooms[room].id for room in world.rooms]}")
print(f"Does it?: {len(set([world.rooms[room].id for room in world.rooms]) - set(map.rooms.keys())) == 0}")





# -----------------------------------------------------------------------------
# TEST:
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
