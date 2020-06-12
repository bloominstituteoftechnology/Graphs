from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Queue, Stack

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
#=====================================================
""" 
    Every vertex and edge that is visited exactly once in a clear-cut order 
    determines traversal graph.

    Vertices are marked to be able to track them, 
    during a trasversal, it is crucial to do it to know which one have been visited.
"""
    


def bfs(starting_vertex):
    # In BFS structure starting from starting_vertex to destination_vertex
    # Returns a list containing the shortest pth
    
    # Initializing queue
    q = Queue()

    # Enqueue  a path to the starting vertex
    q.enqueue([[starting_vertex, None]])

    
    # Visited vertices need to be stored in a set
    visited = set()

    # while the queue is greated than zero. Not empty...
    while q.size() > 0:
        # Dequeue the first path
        path = q.dequeue()
        # Grab the vertex from the end of the path
        v = path[-1][0]

        # analize if it is been visited
        # if it hasn't been visited...
        if v not in visited:
            # Mark it as visited
            visited.add(v)

            # check all directions for "?"
            for direction in adjacency_dict[v]:
                # if a '?' is found
                if adjacency_dict[v][direction] == '?':
                    # if so, return the a traversal to that room
                    traversal = []

                    for i in range(len(path)):

                        # cleanup
                        if path[i][1] is not None:
                            traversal.append(path[i][1])
                    return traversal

            # Enqueue a path to all it's neighbors
            for neighbor in adjacency_dict[v]:
                # make a copy of the path
                path_copy = path.copy()

                # enqueue the copy
                path_copy.append([adjacency_dict[v][neighbor], neighbor])
                q.enqueue(path_copy)
    return False 

# make a function that takes in a dir and returns the opposite direction
def opp_dir(dir):
    if dir == 'n':
        return 's'
    
    elif dir == 's':
        return 'n'
    
    elif dir == 'w':
        return 'e'
    
    elif dir == 'e':
        return 'w'



# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
adjacency_dict = {}

# here i will have to make an adjacency dictionary with all possible directions
# use for loop to iterate through all the rooms in the world
# for room_id in world.rooms:

# nested for loop to iterate through the exits in that room
    
    # conditon: if room object hasn't been created yet
    # initiate a dictionary for that room
        # allocote a value of '?' for each exit
        # then i think will choose a direction from current rooms exits
    # if no unxplored direction   if the direction == None:
    # will do a bfs searching for exit with '?'
       # condition: if bfs returns a path
       # then add path to the traversal_path
            # walk that path and continue
            # condition: if bfs return fals
            # then break it
        # otherwise travel in selected direction and mark rooms in adjacency_dict
        # else:
            # player in current room id will assign to previouse room id
            # then player travels
            # --------- not sure
        #assign prev room the direction to current_room_id
        

        # here i will have to assign current rooms id to opposite direction from which we traveled
        # 






       

    

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED, THERE ARE: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
