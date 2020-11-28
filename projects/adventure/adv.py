from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from collections import deque

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
opp = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

current_room = player.current_room.id

exits = player.current_room.get_exits()

graph[current_room] = {e: '?' for e in exits}

while '?' in graph[current_room].values():
    d = random.choice([k for k,v in graph[current_room].items() if v == '?'])

    prev_room = current_room
    player.travel(d)
    traversal_path.append(d)
    current_room = player.current_room.id

    if current_room not in graph:
        graph[current_room] = {e: '?' for e in player.current_room.get_exits()}

    graph[prev_room][d] = current_room
    graph[current_room][opp[d]] = prev_room

    if '?' not in graph[current_room].values():
        if len(graph) == 500:
            break

        queue = deque()
        visited = set()

        queue.append([current_room])

        while len(queue) > 0:
            curr_path = queue.popleft()
            curr_room = curr_path[-1]

            if '?' in graph[curr_room].values():
                break
            
            if curr_room not in visited:
                visited.add(curr_room)

                for e in graph[curr_room]:
                    new_path  = list(curr_path)
                    new_path.append(graph[curr_room][e])
                    queue.append(new_path)

        for i in range(1, len(curr_path)):
            d = [k for k,v in graph[current_room].items() if v == curr_path[i]][0]
            player.travel(d)
            traversal_path.append(d)
            current_room = player.current_room.id



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
