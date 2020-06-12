from room import Room
from player import Player
from world import World
from collections import deque

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
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path_for_test = []
traversal_path = []

reversal_dict = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w'
}

visited = set([player.current_room.id])

log = {}
log[player.current_room.id] = {}
for exits in player.current_room.get_exits():
    log[player.current_room.id].update({exits : '?'})

while len(visited) != len(room_graph):
    checkForChange = False

    for direction in player.current_room.get_exits():
        if log[player.current_room.id][direction] == '?':
            checkForChange = True
            #Save our current room
            saved_room = player.current_room.id

            #Move rooms
            player.travel(direction)

            #Add to visited, and path.
            visited.add(player.current_room.id)
            traversal_path_for_test.append(direction)
            traversal_path.append(reversal_dict[direction])

            #Update our previous room's log
            log[saved_room][direction] = player.current_room.id

            #Make a new log for this room
            if player.current_room.id not in log:
                log[player.current_room.id] = {}
                for e in player.current_room.get_exits():
                    log[player.current_room.id].update({e : '?'})
            log[player.current_room.id][reversal_dict[direction]] = saved_room

            break

    if player.current_room.get_exits() == list(traversal_path[-1]):
        queue = deque()
        queue.append(player.current_room.id)

        vis = []

        while len(queue) > 0:
            curr = queue.popleft()

            if curr not in vis:
                vis.append(curr)
                
                for adj in log[curr]:
                    if log[curr][adj] == '?':
                        while player.current_room.id != curr:
                            checkForChange = True
                            print('room', player.current_room.id)
                            print('trav', traversal_path)
                            print('eehh', log[player.current_room.id])
                            print('total_path', traversal_path_for_test)
                            backwards = traversal_path.pop(-1)
                            player.travel(backwards)
                            traversal_path_for_test.append(backwards)
                        break

                    queue.append(log[curr][adj])
    if checkForChange == False:
        break

    print(log)
    


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room.id)

for move in traversal_path_for_test:
    player.travel(move)
    visited_rooms.add(player.current_room.id)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path_for_test)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")