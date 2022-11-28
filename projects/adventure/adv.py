from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import time

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
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
return_sequence = []

print("STARTING")
my_room_graph = {}
visited_rooms = set()
all_rooms_visited = False
opposite_directions = {
    "n": "s",
    "s": "n",
    "w": "e",
    "e": "w"
}

def add_room_to_graph(room_id, exit_options, prev_r=None, prev_r_direction=None):
    my_room_graph[room_id] = {}
    for exit_option in exit_options:
        if exit_option == prev_r_direction:
            my_room_graph[room_id][exit_option] = prev_r
        else:
            my_room_graph[room_id][exit_option] = "?"

def get_moves(current_exits):
    moves = []
    for exit_option in current_exits:
        if my_room_graph[room_id][exit_option] == "?":
            moves.append(exit_option)
    return moves

# add first room to graph
add_room_to_graph(player.current_room.id, player.current_room.get_exits())

while not all_rooms_visited:
    current_exits = player.current_room.get_exits()
    room_id = player.current_room.id
    print("-"*10)
    print(f"Current room: {room_id} - {current_exits}")
    print(f"Curr return moves: {return_sequence}")
    print(my_room_graph)

    my_moves = get_moves(current_exits)
    for exit_option in current_exits:
        if my_room_graph[room_id][exit_option] == "?":
            my_moves.append(exit_option)
    if len(my_moves) == 0:
        if len(return_sequence) == 0:
            all_rooms_visited = True
        else:
            # return spot until you have moves
            my_move = return_sequence.pop(-1)
            print(f"moving {my_move}")
            traversal_path.append(my_move)
            player.travel(my_move)
            # if at starting room, reset return_sequence
            # check for loop by seeing ...
            if player.current_room.id == world.starting_room:
                return_sequence = []

    else:
        my_move = my_moves[0]
        print(f"moving {my_move}")
        traversal_path.append(my_move)
        return_sequence.append(opposite_directions[my_move])
        player.travel(my_move)
        new_room_id = player.current_room.id

        # add new_room_id to room_id's graph
        my_room_graph[room_id][my_move] = new_room_id
        if new_room_id not in visited_rooms:
            # add new room to visited
            visited_rooms.add(new_room_id)
            # add new_room_id to graph
            add_room_to_graph(new_room_id, player.current_room.get_exits(), room_id, opposite_directions[my_move])
    print()




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