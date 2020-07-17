from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

def opposite_direction(direction):
    if direction == 'n':
        return 's'
    if direction == 's':
        return 'n'
    if direction == 'e':
        return 'w'
    if direction == 'w':
        return 'e'

def what_is_it(object):
    if object == None:
        print("It's a None")
        return 
    if isinstance(object, int):
        print("It's an int")
        return 
    print("It's a Class")
    return 

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

# My Code Goes Here
traversal_graph = {}

traversal_graph[player.current_room.id] = {'n': player.current_room.n_to, 's': player.current_room.s_to, 'w': player.current_room.w_to, 'e': player.current_room.e_to}
direction_of_travel = 'n'
prior_room_id = player.current_room.id
player.travel(direction_of_travel, False)
traversal_path.append(direction_of_travel)

traversal_graph[player.current_room.id] = {'n': player.current_room.n_to, 's': player.current_room.s_to, 'w': player.current_room.w_to, 'e': player.current_room.e_to}
traversal_graph[prior_room_id][direction_of_travel] = player.current_room.id
traversal_graph[player.current_room.id][opposite_direction(direction_of_travel)] = prior_room_id

print(type(traversal_graph[player.current_room.id]['n'])) # <class 'room.Room'>
print(type(traversal_graph[player.current_room.id]['s'])) # <class 'int'>
print(type(traversal_graph[player.current_room.id]['w'])) # <class 'NoneType'>

what_is_it(traversal_graph[player.current_room.id]['n'])
what_is_it(traversal_graph[player.current_room.id]['s'])
what_is_it(traversal_graph[player.current_room.id]['w'])

player.travel('n', False)
traversal_path.append('n')

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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
