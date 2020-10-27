import random
import math
from ast import literal_eval
from projects.adventure.util import Stack, Queue
from projects.adventure.room import Room
from projects.adventure.player import Player
from projects.adventure.world import World

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

def get_neighbors(compas):
    neighbors = []

    [n],[s],[w],[e] = compas
    # north 
    if n > 0 and room_graph[n-1][s][w][e] == '?':
        neighbors.append((n-1, s, w, e))
    # next path -- len(room_graph)-1 && room_graph compas == "?"
    if n < len(room_graph) - 1 and room_graph[n+1][s][w][e] == '?':
        neighbors.append((n+1, s, w, e))
    # south 
    if s > 0 and room_graph[n][s-1][w][e] == '?':
        neighbors.append((n, s-1, w, e))
    # next path -- len(room_graph[compas]) && room_graph compas == "?"
    if s < len(room_graph[compas]) and room_graph[n+1][s][w][e] == '?':
        neighbors.append((n+1, s, w, e))
        
# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = set()
counter = 0
path = []
# string = {n:s, s:n, e:w, w:e} 
opposite_room = {'n': 's','s': 'n','e': 'w','w': 'e'}
room = {}

while len(visited) < len(room_graph):
        #   pop or dequeue the vertex of the queue:
            current_room = player.current_room.id
        #   if vertex not in visited_vertices:
            if current_room not in visited:
            #   add the vertex to the visited set()
                visited.add(current_room)
            possible_exits = player.current_room.get_exits()
            room[current_room] = possible_exits
# loop tthrough all poss rooms 
while len(room[current_room]) >= 0:
        # more rooms? keep looping. 
        if len(room[current_room]) > 0: 
            # assign player_move to room queue 
            player_move = room[current_room].pop()
            get_room = player_move[-1]
            
            if get_room not in visited:
                # add to the path 
                path.append(player_move)
                # save player_move
                traversal_path.append(player_move)
                # add player_move to the room
                player.travel(player_move)
                counter += 1
               
            #   break so it wont break again 
                break
            
            # traverse backwards 
        elif len(room[current_room]) == 0:
            # pop prev move from path 
            prev = path.pop()
            # find the prev direction.
            prev_direction = opposite_room[prev]
            # append  prev move to traveral_path 
            traversal_path.append(prev_direction)
            player.travel(prev_direction)
            counter += 1
            break





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
