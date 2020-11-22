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



graph = {}
visited = set()
direction = None

# starting room
current = world.starting_room
visited.add(current)
# print(f"current: {current.name}")

# make the first move, to get a starting direction
exits = current.get_exits()
direction = random.choice(exits)
traversal_path.append(direction)
current = current.get_room_in_direction(direction)
visited.add(current)
# print(f"current: {current.name}")

while len(visited) < len(room_graph):
    direction = current.next_available_direction_to_the_right(direction)
    traversal_path.append(direction)
    # print(f"direction: {direction}")
    current = current.get_room_in_direction(direction)
    visited.add(current)
    # print(f"current: {current.name}")

    OKAY: I got through the smaller test maps fine, but on the larger one I'm getting into an infinite loop.
    I need to create a graph, like they told us to! Study the README again, and write down in comments
    what the requirements are. Should be easy.


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
    print(f"{len(visited_rooms)} visited rooms")
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
