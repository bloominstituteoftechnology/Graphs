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
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())


# room_graph = {
#   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
#   1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}],
#   2: [(3, 7), {'s': 1}],
#   3: [(4, 5), {'w': 0, 'e': 4}],
#   4: [(5, 5), {'w': 3}],
#   5: [(3, 4), {'n': 0, 's': 6}],
#   6: [(3, 3), {'n': 5, 'w': 11}],
#   7: [(2, 5), {'w': 8, 'e': 0}],
#   8: [(1, 5), {'e': 7}],
#   9: [(1, 4), {'n': 8, 's': 10}],
#   10: [(1, 3), {'n': 9, 'e': 11}],
#   11: [(2, 3), {'w': 10, 'e': 6}],
#   12: [(4, 6), {'w': 1, 'e': 13}],
#   13: [(5, 6), {'w': 12, 'n': 14}],
#   14: [(5, 7), {'s': 13}],
#   15: [(2, 6), {'e': 1, 'w': 16}],
#   16: [(1, 6), {'n': 17, 'e': 15}],
#   17: [(1, 7), {'s': 16}]
# }
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

traversal_path = []
reverse = {"n": "s", "s": "n", "e": "w", "w": "e"}
maze_graph = {}

def starting_room():
    direction_dict = {}
    room = player.current_room
    exits = player.current_room.get_exits()
    for way_out in exits:
        direction_dict[way_out] = "?"
    maze_graph[room.id] = direction_dict
    print(maze_graph)

def explore(direction):
    direction_dict = {}
    current = player.current_room.id
    room = player.current_room.get_room_in_direction(direction)
    player.travel(direction)
    maze_graph[current][direction] = room.id
    if room.id not in maze_graph:
        for way_out in room.get_exits():
            some_room = room.get_room_in_direction(way_out)
            if some_room.id not in maze_graph:
                direction_dict[way_out] = "?"
            elif way_out is reverse[direction]:
                direction_dict[way_out] = current
            elif maze_graph[some_room.id][reverse[way_out]] is "?":
                maze_graph[some_room.id][reverse[way_out]] = room.id
        maze_graph[room.id] = direction_dict
    traversal_path.append(direction)

def complete_maze():
    pass    

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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
