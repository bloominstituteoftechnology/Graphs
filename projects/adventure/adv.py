from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import os

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = os.path.join(os.path.realpath(__file__), "..","maps", "test_line.txt")
# map_file = "maps/test_cross.txt"
map_file = os.path.join(os.path.realpath(__file__),  "..", "maps", "test_cross.txt")
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# in here will do the algorithm that will construct the a 
# path that will traverse all the roooms in the map
# will fill out the traversal_path

 # go through each path with depth traversal.
        # call recursively 
        # when there are more than two directions possible will then 
        # each recursive call will return the lenght of moves and the path
        # will go build the steps from this curNode where go to the shortest
        # paths fisrt and then the longes second.
def get_traversal_path(visited=None):
    if not visited:
        visited = set() # making the set that will keep track of the where visited

    go_back = None # This is the the direction that should go back
    num_dirs = 0
    # These are a place holder for the dominant path 
    theTuple_n = theTuple_e = theTuple_s = theTuple_w = (None, None, None)
    s_dom_path = n_dom_path = e_dom_path = w_dom_path = None
    n_dist = n_path = e_path = e_dist = s_dist = s_path = w_path = w_dist = None
    # base case will be when there are do more directions to go or 
    # that all the directions to go have been visited
    if player.current_room.id in visited:
        return 
    

    # Add to the visited
    visited.add(player.current_room.id)

    if len(player.current_room.get_exits()) < 1:
        return 
    # doing the movement in each of the four directions
    # north
    if player.travel("n"):
        go_back= "s"
        num_dirs += 1
        theTuple_n = get_traversal_path(visited)    
    if player.travel("s"):
        go_back="n"
        num_dirs += 1
        theTuple_s = get_traversal_path(visited)
    if player.travel("e"):
        go_back="w"
        num_dirs += 1
        theTuple_e = get_traversal_path(visited)
    if player.travel("w"):
        go_back = "e"
        num_dirs += 1
        theTuple_w = get_traversal_path(visited)
    # will now inrement the depth of the paths down one of
    # the directions
    # going back from the direction the player came down
    if player.current_room.id != 0:
        player.travel(go_back)
        distance +=1
        path += [player.current_room]
    # will do the loop if there are at least two directions
    if num_dirs >=2:
        # finding the longest path or the dominant path
        theList =  [theTuple_n, theTuple_s, theTuple_e, theTuple_w]
        longest = -1, longest_path_num = 
        for i, tup,  in enumerate(theList):
            if tup[0] is not None:
                if tup[0] > longest:
                    longest = tup[0]
                    longest_path_num = i
        # Will now loop through again and will build the path and also 
        # will make the distance
        for i tup in enumerate(theList):
            if tup[0]: # checking to see if it is None or not
                if i !=  #TODO need to add the path and then the reverse of the path



         or player.current_room.
    print("This is the current room")
    print(player.current_room.get_exits_string())
    print("this is the just the exits or the current room")
    print(player.current_room.get_exits())
    print("This is the what is the direction north")
    print(player.current_room.get_room_in_direction("n"))
    print(player.current_room)
    print(f"this is the current room id  {player.current_room.id}")



#trying to run the function
get_traversal_path()
# # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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
