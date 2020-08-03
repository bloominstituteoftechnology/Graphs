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
graph[player.current_room.id] = {exit_: '?' for exit_ in player.current_room.get_exits()}


def bfs(start, goal):
    visited = set()
    q = deque() 
    q.append([player.current_room.id]) 
    route_q = deque()
    route = []

    while len(q) > 0:
        path = q.popleft()
        if route_q:
            route = route_q.popleft()
        room = path[-1]

        if room == '?':
            return route
  
        list_direct = list(graph[room ].keys())
        for direct in list_direct:
            
            if graph[room ][direct] not in visited:
                visited.add(room )
                new_route = route + [direct]
                new_path = path + [graph[room ][direct]]
                q.append(new_path)
                route_q.append(new_route)

while len(graph.keys()) < len(world.rooms.keys()):
    path = deque(bfs(player, graph))
    old_room = player.current_room.id 
    direct = path.popleft()  
    player.travel(direct) 
    room  = player.current_room.id   
    if room not in graph:
        graph[room ] = {exit_: '?' for exit_ in player.current_room.get_exits()}
        
    graph[old_room][direct] = room  
    dir_ = {'n':'s','s':'n','e':'w','w':'e'}
    graph[room ][dir_[direct]] = old_room
    traversal_path.append(direct)


# TRAVERSAL TEST - DO NOT MODIFY
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
#player.current_room.print_room_description(player)
#while True:
#    cmds = input("-> ").lower().split(" ")
#    if cmds[0] in ["n", "s", "e", "w"]:
#        player.travel(cmds[0], True)
#    elif cmds[0] == "q":
#        break
#    else:
#        print("I did not understand that command.")