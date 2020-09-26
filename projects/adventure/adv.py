from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
import os
from collections import deque

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = os.path.join(os.path.realpath(__file__), "..","maps", "test_line.txt")
# map_file = "maps/test_cross.txt"
#map_file = os.path.join(os.path.realpath(__file__),  "..", "maps", "test_cross.txt")
# map_file = "maps/test_loop.txt"
map_file = os.path.join(os.path.realpath(__file__),  "..", "maps", "test_loop_fork.txt")
# map_file = "maps/test_loop_fork.txt"
#map_file = os.path.join(os.path.realpath(__file__),  "..", "maps", "main_maze.txt")
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
def get_traversal_path(path=None, visited=None, dom_path=None, startingPoint=None, prevRoom=None, cycle=None, theDir=None):

    
    if not visited:
        visited = set() # making the set that will keep track of the where visited
    if path == None: # getting the path that will be sent to the method
        path = []
    if dom_path == None:
        dom_path = deque()
    if startingPoint == None:
        startingPoint = player.current_room.id
    

    go_back = None # This is the the direction that should go back
    num_dirs = 0
    theTuple = None
    # These are a place holder for the dominant path 
    # (dist, path, dom_path, cycle) cycle is a dictionary 
    # key is the point already in visited
    # val is the point on the path that found the key
    theTuple_n = theTuple_e = theTuple_s = theTuple_w = (0, None, None, None)
    #s_dom_path = n_dom_path = e_dom_path = w_dom_path = None
    #n_dist = n_path = e_path = e_dist = s_dist = s_path = w_path = w_dist = None
    # base case will be when there are do more directions to go or 
    # that all the directions to go have been visited
    if player.current_room.id in visited:
        # a tupel is returned that has the following
        # (dist, path, dominantPath, cycle)  The dominantPath is a double linked list
        if prevRoom:
            if not cycle:
                # making the dictionary to contain the cycle
                cycle = dict()
            cycle[player.current_room.id] = (prevRoom, theDir)
        return (0, path, dom_path, cycle)
    

    # Add to the visited
    visited.add(player.current_room.id)

    curRoom = player.current_room.id
    #theDist = 1 # counting the room that they are in as the distance
    path.append((curRoom, theDir))
    dom_path.append((curRoom, theDir)) # this is the deque double linked list
    
    if len(player.current_room.get_exits()) == 1: # returns a tuple (dist, path, dom_path)
        # on each return a tuple will be returned which has
        # (dist, path, dominant_path)
        return (1, path, dom_path, cycle)
    # doing the movement in each of the four directions
    # north
    if player.travel("n"):
        go_back= "s"
        newPath = []
        newDeque = deque()
        theTuple_n = get_traversal_path(newPath, visited, newDeque,
                                         startingPoint, curRoom, cycle, "n")
        if theTuple_n[0] != 0:
            num_dirs += 1
        # bringing the player back to the same room
        player.travel(go_back)
            
    if player.travel("s"):
        go_back="n"
        newPath = []
        newDeque = deque()
        theTuple_s = get_traversal_path(newPath, visited, newDeque,
                                        startingPoint, curRoom, cycle, "s")
        if theTuple_s[0] != 0:  
            num_dirs += 1
        player.travel(go_back)

    if player.travel("e"):
        go_back="w"
        newPath = []
        newDeque = deque()
        theTuple_e = get_traversal_path(newPath, visited, newDeque,
                                        startingPoint, curRoom, cycle, "e")
        if theTuple_e[0] != 0:      
            num_dirs += 1
        player.travel(go_back)

    if player.travel("w"):
        go_back = "e"
        newDeque = deque()
        newPath = []
        theTuple_w = get_traversal_path(newPath, visited, newDeque, 
                                         startingPoint, curRoom,  cycle, "w")
        if theTuple_w[0] != 0:
            num_dirs += 1   
        player.travel(go_back)

    # will now inrement the depth of the paths down one of
    # the directions
    # going back from the direction the player came down
    # if player.current_room.id != 0:
    #     player.travel(go_back)
    #     distance +=1
    #     path += [player.current_room]

    theList =  [theTuple_n, theTuple_s, theTuple_e, theTuple_w]
    # will do the loop if there are at least two directions
    if num_dirs >=2:
        # finding the longest path or the dominant path
        # each tuple will contain 
        # (dist_from_whence_returning, path_down_to_where_return, dominant_path)
        # The dominant path will not have branches on it
        
        
        longest = -1
        longest_path_num = None
        dom_path_list = None
        distance = 1
        doing_cycle = False
        cycleNum = None
        opp_directions = {"n":"s",  "s":"n", "e":"w", "w":"e"}
        the_dom_path = None # this will hold the dominant path from n, s, e, or w
        # this is finding which of the n, s, e, w paths is the longest
        # checking to see if there are cycles
        
        for i, tup  in enumerate(theList):
            if tup[0] != 0:
                if tup[0] > longest:
                    longest = tup[0]
                    longest_path_num = i

        if cycle:
            if curRoom in cycle:
                # will try to build the cycle
                # make dom_path = just the current room
                
                
                # finding out if the longest is the cycle
                if cycle[curRoom] == theList[longest_path_num][2][-1][0]:
                    doing_cycle = True
                    
                    # need to find a new longest path
                    # longest = 0
                    # cycleNum = longest_path_num
                    # for i , tup in enumerate(theList):
                    #     if tup[0] != 0 and i != cycleNum:
                    #         if tup[0] > longest:
                    #             longest = tup[0]
                    #             longest_path_num = i
        # Will now loop through again and will build the path and also 
        # will make the distance
        newPath = path[:] # this is a tuple of the path and the direction
        # all the things appended here are on the same cut point
        for i, tup in enumerate(theList):
            if tup[0] != 0: # checking to see if it is None or not
                if i !=  longest_path_num:  # this is for the non dominant paths
                    endOfCurPath = newPath[-1]
                    newPath += tup[1]
                    # making the distance right
                    #distance += len(tup[1]) * 2 
                    # now walking back from the tup path
                    tup[2].reverse()
                    for i, elem in enumerate(tup[2]):
                        if i != len(tup[2])-1:  # skipping the first element because we are already there
                            toAppend = (tup[2][i+1][0], opp_directions[tup[2][i][1]])
                            newPath.append(toAppend)
                        else:
                            toAppend = (curRoom, tup[2][i][1])
                            newPath.append(toAppend)
                    # appending again the current room
                    #newPath.append(curRoom)
                else:
                    # getting the dominant path
                    the_dom_path = tup[2] # this is a doubly linked list
                    dom_path_list = tup[1] # both of these are a tuple 
        
        else:    
            # now doing the appending of the dominant path
            for elem in dom_path_list:
                newPath.append(elem)

            # if doing_cycle:
            #     # putting the cycle into the the 
            #     distance = 1
            #     dom_path = curRoom
            #else:    
            # building the domPath 
            dom_path.extend(the_dom_path)
            distance = len(dom_path)

            # theTuple being build again
            theTuple = (distance, newPath, dom_path, cycle)        

    
    else: # This is where there is just a straight line--no splits
        # in here is where we will increment the distance
        for dist, thePath, the_dom_path, cycle in theList:
            if dist != 0: # Not None
                # need to increment the distance, and the dom_path
                dist +=1
                path = path + thePath
                dom_path.extend(the_dom_path)
                # will now return the with the tuple
                theTuple = (dist, path, dom_path, cycle)
                break # breaking out of the loop to go to the end of this function
        if theTuple == None:
            # need to just return what you have currently if 
            # nothing has been added   
            theTuple = (1, path, dom_path, cycle)

    # checking if this is the end of the graph or the starting point
    if player.current_room.id == startingPoint:      
        # will be returning the theTuple[1]
        # returning just the directions
        newList = []
        
        
        for i in range(len(theTuple[1])):
            if i != 0:
                newList.append(theTuple[1][i][1])
        #     newList.append(t[1])
        # return newList # this will return the directions
        theTuple = newList    
               
    return theTuple


       
    # print("This is the current room")
    # print(player.current_room.get_exits_string())
    # print("this is the just the exits or the current room")
    # print(player.current_room.get_exits())
    # print("This is the what is the direction north")
    # print(player.current_room.get_room_in_direction("n"))
    # print(player.current_room)
    # print(f"this is the current room id  {player.current_room.id}")



#trying to run the function

thePath = get_traversal_path()
print(f"My path length is: {len(thePath)}")
print(thePath)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
print(f"The starting room is: {player.current_room.id}")
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
