from room import Room
from player import Player
from world import World
from util import Stack

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

visited_list = [0]

known_information = {}
exits = player.current_room.get_exits()
known_information[player.current_room.id] = {}
for ext in exits:
    known_information[player.current_room.id][ext] = '?'

rooms_with_untapped_potential = Stack()

opposites = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

path_from_origin = []
fully_explored_room = 0

def document(previous_room_num, previous_direction_of_travel, known_information):
    traversal_path.append(previous_direction_of_travel)
    room_num = player.current_room.id
    exits = player.current_room.get_exits()
    if room_num not in known_information.keys():
        known_information[room_num] = {}
        for ext in exits:
            known_information[room_num][ext] = '?'
        known_information[room_num][opposites[previous_direction_of_travel]] = previous_room_num
        known_information[previous_room_num][previous_direction_of_travel] = room_num
    else:
        known_information[previous_room_num][previous_direction_of_travel] = room_num
        known_information[room_num][opposites[previous_direction_of_travel]] = previous_room_num


while len(known_information.keys()) < 500:
    room_num = player.current_room.id
    
    # print(f"{len(known_information.keys())} rooms visited after {len(traversal_path)} steps traveled. Current room:{room_num} with known information: {known_information[room_num]} Rooms With Untapped Potential = {rooms_with_untapped_potential.size()}", end='\r')
    
    exits = player.current_room.get_exits()
    if list(known_information[room_num].values()).count('?') > 1:
        rooms_with_untapped_potential.push(room_num)            
    
    for direction in known_information[room_num].keys():
        new = False
        if known_information[room_num][direction] == '?':
            player.travel(direction)
            path_from_origin.append(direction)
            visited_list.append(player.current_room.id)
            document(room_num, direction, known_information)
            new = True
            break
    if not new:
        fully_explored_room += 1
        destination = rooms_with_untapped_potential.pop()
        if '?' in known_information[destination].values():
            pass
        else:
            destination = rooms_with_untapped_potential.pop()
        backtrack_list = path_from_origin.copy()
        backtrack_list.reverse()
        for direction in backtrack_list:
            back = opposites[direction]
            player.travel(back)
            path_from_origin = path_from_origin[:-1]
            visited_list.append(player.current_room.id)
            traversal_path.append(back)
            if player.current_room.id == destination:
                break

for element in visited_list:
    if visited_list.count(element) > 4:
        print(f"element{element} visited{visited_list.count(element)} times")
    

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
##player.current_room.print_room_description(player)
##while True:
##    cmds = input("-> ").lower().split(" ")
##    if cmds[0] in ["n", "s", "e", "w"]:
##        player.travel(cmds[0], True)
##    elif cmds[0] == "q":
##        break
##    else:
##        print("I did not understand that command.")
