from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import random

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# USEFUL FUNCTIONS
current_room_id = player.current_room.id
exits = player.current_room.get_exits()
# travel = player.travel(direction)

traversal_path = []

# UPER

# UNDERSTAND
# FILL TRAVERSAL PATH WITH DIRECTIONS, 'n', 's' ECT TO GO TO EVER LOCATION ON THE MAP

x = random.choice([1, 2, 3, 4])
print('x', x)
room_id_log = []
# PLAN
while len(traversal_path) < 900:
    print('traversal_pathlength:', len(traversal_path))

    for direction in exits:
        print('direction:', direction )
        if direction == 'n' and x == 1:
            traversal_path.append(direction)
            player.travel(direction)
            print('current_room_id', current_room_id)



        elif direction == 's' and x == 2:

            print('current_room_id', current_room_id)
            traversal_path.append(direction)
            player.travel(direction)


        elif direction == 'e' and x == 3:

            print('current_room_id', current_room_id)
            traversal_path.append(direction)
            player.travel(direction)

        elif direction == 'w' and x == 4:

            print('current_room_id', current_room_id)
            traversal_path.append(direction)
            player.travel(direction)
        else:
            pass


print('traversal_path', traversal_path)
#
# def direct():
#     traversal_path.append('s')
#
#
# direct()

# Fill this out with directions to walk
# traversal_path = ['n', 'n']



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
