from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, Queue


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#will need to functions: DFT and BFS

#DFT(starting_room) --cahnged to player so could get methods off of player
def dft(player):
    #create a stack
    stack = Stack()
    #add starting room to stack to be searched
    stack.push(player.current_room)
    #create visit as a set
    visit = set()
    #REPL
    #while stack is not empty:
    while len(stack) > 0:
        #remove that room
        room = stack.pop()
        #check if it's been visited. If not:
        if room not in visit:
            #add room to visit
            visit.add(room)
            #for all neighrboring rooms in get exits:
            for neighboring_room in player.current_room.get_exits():
                #add room to stack
                stack.push(neighboring_room)
                #need to choose random direction??
        
#BFs(starting room):
def BFS(starting_room, ):
    #create empty queue
    #add starting room to the path in the queue
    #create visited set
    #while queue is not empty:
        #create variable for removing from queue
        #create variable for last room in path
        #if that room has not been visited:
            #mark as visited
            #for neighboring rooms in get exit:
                #make a copy of the path
                #add neighbor to end of path
                #enqueue path copy







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