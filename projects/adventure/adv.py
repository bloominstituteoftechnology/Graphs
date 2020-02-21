from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval


def unexplored_exits(graph, current_room):
    return [k for k, v in graph[current_room].items() if v=='?']


def backtrack_path(graph, player):
    # Create an empty queue
    q = Queue()
 
    # Add a PATH TO the starting vertex_id to the queue
    q.enqueue( [(player.current_room.id, None)] )
    #Create an empty set
    visited = set()
    # While the queue is not empty
    while q.size() > 0:
        #Dequeue the first path
        path = q.dequeue()
        # grab the last vertex from the path
        v = path[-1][0]
        # check if it's the target
        if '?' in graph[v].values():
            # if so, return the path
            return [i[1] for i in path[1:]]
        if v not in visited:
            visited.add(v)
            for key, val in graph[v].items():
                # make a copy of the path before adding
                path_copy = path.copy()
                print(f"Path copy: {path_copy}")
                path_copy.append((val, key))
                q.enqueue(path_copy)

# def path_to_directions(bpath, graph2):
#     bdirections = []
#     for i in range (len(bpath)-1):
#         print(i)
#         for k, v in graph2[i].items():
#             if v == bpath[i+1]:
#                 bdirections.append(k)
#     return bdirections



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
num_rooms = 500
opposite = {'s': 'n', 'n': 's', 'w': 'e', 'e': 'w'}

'''
Pick a random unexplored direction
Travel that direction and log the step in your route
Then loop
'''
source = None 
old_room = None
visited = set()
counter = 0

while len(visited) < num_rooms:  
    # get a list of exits from the current room
    current_room = player.current_room.id
    print(f"You are in Room {current_room}")
    visited.add(current_room)

    exits = player.current_room.get_exits() # returns list of exits
    print(f"The exits are {exits}")

    if current_room not in graph:
        print(f"Room {current_room} not in graph.")
        graph[current_room] =  {}
        print("Added!")
        print(f"Graph length is {len(graph)}")
        for e in exits:
            graph[current_room][e]= '?'
    
    if len(visited) == num_rooms:
        break

    print(f"length of graph: {len(graph)}")
    if source and no_back:
        graph[current_room][source] = old_room
    no_back = True
    
    print(graph[current_room])

    unexplored_exits_list = unexplored_exits(graph, current_room)
    print(f"Unexplored exits: {unexplored_exits_list}")

    
    # record the connections
    # randomly select an exit and travel in that direction
    if len(unexplored_exits_list)>0:
        direction = random.choice(unexplored_exits_list)
        player.travel(direction)
        graph[current_room][direction] = player.current_room.id
        source = opposite[direction]
        old_room = current_room
        # graph[player.current_room.id][opposite[direction]] = current_room
        print(f'travelled {direction}')
        traversal_path.append(direction)
        print(f"trav_path: {traversal_path}")
        # print(f"Traversal path: {traversal_path}") 
    else:
        print("Backtracking...")
        backtrack_path_list = backtrack_path(graph, player)
        print(f"Backtrack list: {backtrack_path_list}")
        for d in backtrack_path_list:
            player.travel(d)
            traversal_path.append(d)
        no_back = False
    
    counter += 1


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    print(f"Final Traversal passed: {traversal_path}")
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
