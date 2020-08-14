from Graphs.projects.adventure.player import Player
from Graphs.projects.adventure.world import World

from random import choice
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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

for x in room_graph:
    room_graph[x].append(0)

# Fill this out with directions to walk


def traversal(graph, starting_vertex):
    visited = {}

    retrace = []

    retrace_map = {'n': 's', 'e': 'w', 'w': 'e', 's': 'n'}

    path = []

    visited[starting_vertex] = player.current_room.get_exits()

    while len(visited.keys()) != len(graph):
        if player.current_room.id not in visited:
            visited[player.current_room.id] = player.current_room.get_exits()
            reverse = retrace[-1]
            visited[player.current_room.id].remove(reverse)

        elif len(visited[player.current_room.id]) == 0:
            reverse = retrace.pop()
            path.append(reverse)
            player.travel(reverse)

        else:
            direction = choice(visited[player.current_room.id])
            visited[player.current_room.id].remove(direction)
            path.append(direction)
            retrace.append(retrace_map[direction])
            player.travel(direction)

    return path


traversal_path = traversal(room_graph, player.current_room.id)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, "
          f"{len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
#
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
