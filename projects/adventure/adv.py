from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval #<-- What is that? Check Python Docs

#Problem:
#The goal is to move from one room to the next in under 2000 steps (Goal is actually 950), the strategy is to only visit one room going in one direction around the map.  The problem is if we go in 1 direction, how do we backtrack if the player reaches a dead end?

#Solution:
#If the player hits a dead-end (meaning no other attached rooms), mark the dead end room as `unvisited`.  This enables the player to backtrack to the previous room and explore another adjacent room which will enable the player to traverse to the other adjacent room and find another path around the map until all rooms have been visited

#Questions:
#What function moves player around the map? 
'''
def travel(self, direction, show_rooms = False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")
'''

#visit

#Need to use helper functions an place them inside the DFT
#Say what needs to be done each time you visit a room
#1. Add visited room to stack
#2. Check for exits (display exits)
#3. If there is an exit, check for connected rooms (find the helper function for that in world graph)
#4. If there is no connected room for 'n', then visited_room == 

def adventure_moves(n, traversal_path, u):
    # Load world
    world = World()
    room = Room(self, id=0, x=None)
    player = Player(world.starting_room)
    s = Stack()
    limit = 500
    # n, the current depth in the search tree
    # traversal_path, a list of vertices visited up to this point
    # u, the room in the graph we wish to explore
    # limit, the number of rooms in the path.
    
    if n < limit:
        room_list = list(world.print_rooms())
        i = 0
        complete = False

        while i < len(room_list) and not complete:
            #If visited is none, we're going initialize it to equal set
            if visited is None:
                visited = set()
                traversal_path.append(n)
        #If the room has not been visited, add to visited
            if player not in visited:
                visited.add(player.current_room)
                Room.get_exits()
                complete = adventure_moves(n+1, traversal_path, room_list[i],limit)
            i + 1

        if not complete:
            traversal_path.pop()  #Backtrack
            player not in visited

    else:
        complete = True
    
    return complete
    
 
 # Loads the map into a dictionary

    #map_file = "maps/main_maze.txt"
    # You may uncomment the smaller graphs for development and testing purposes.
    # map_file = "maps/test_line.txt"
    # map_file = "maps/test_cross.txt"
    # map_file = "maps/test_loop.txt"
    # map_file = "maps/test_loop_fork.txt"
    room_graph = literal_eval(open(map_file, "r").read())
    world.load_graph(room_graph)

    # Print an ASCII map


    
    # Fill this out with directions to walk
    # traversal_path = ['n', 'n']
    # s.push([world.starting_room])
    # traversal_path = []
    # v = traversal_path[-1]
    # #What does this mean?  Just put n,s,e,and w? 

    # # TRAVERSAL TEST

    # player.current_room = world.starting_room

    # while s.size() > 0:
    #     #Player needs to move.
    #     #Pop the first (current) room
    #     traversal_path = s.pop()
    #     v = traversal_path[-1]
        #Place in the stack
        #If room has not been visited
        
    
    



# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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

