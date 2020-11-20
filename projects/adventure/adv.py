from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map≥
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
current = player.current_room.id

s = []
traversal_path = []
graph = {}
s.append(current)

# for i in world.rooms:
#     graph[i] = {}
# len of visited is less than total rooms

while len(s) > 0:
    room = s.pop(0)
    open_exits = player.current_room.get_exits()

    if room not in graph:
        graph[room] = {}
        for i in open_exits:
            graph[room][i] = "?"
        if traversal_path[-1] == 'n':
            graph[room]['s'] =
        ind = random.randint(0, len(open_exits)-1)
        direction = open_exits.pop(ind)
        player.travel(direction)
        traversal_path.append(direction)
        if player.current_room.id != room:
            graph[room][direction] = player.current_room.id
            s.append(player.current_room.id)
    else:
        for i in open_exits:
            if i == '?':
                player.travel(i)
                if player.current_room.id != room:
                    graph[room][direction] = player.current_room.id
                    s.append(player.current_room.id)
print(graph)
print(traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
