from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval #<-- What is that? Check Python Docs

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

# traversal_path = ['n', 'n']
traversal_path = []

#Problem:
#The goal is to move from one room to the next in under 2000 steps (Goal is actually 950), the strategy is to only visit one room going in one direction around the map.  The problem is if we go in 1 direction, how do we backtrack if the player reaches a dead end?

#Strategy:
#MOVEMENTS!!!!
#1. Move to the east
    #Is room unvisited or is there a dead end?
        #If unvisited, add to uv queue
        #If deadend, mark room as visited and dequeue

#2. Move to the west
    #Is room unvisited or is there a dead end?
    #If unvisited, add to uv queue
    #If deadend, mark room as visited and dequeue

#3. Move to the south
    #Is room unvisited or is there a dead end?
    #If unvisited, add to uv queue
    #If deadend, mark room as visited and dequeue

#4. Move to the south
    #Is room unvisited or is there a dead end?
    #If unvisited, add to uv queue
    #If deadend, mark room as visited and dequeue

#5. Now does len(room_graph) == len(visited) 
    #If false, repeat process
    # If true, traversal path complete 
     



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# while True:
#       cmds = input("-> ").lower().split(" ")
#        if cmds[0] in ["n", "s", "e", "w"]:
#             player.travel(cmds[0], True)
#         elif cmds[0] == "q":
#             break
#         else:
#             print("I did not understand that command.")


# if n < limit:
    #     room_list = list(world.print_rooms())
    #     i = 0
    #     complete = False

    #     while i < len(room_list) and not complete:
    #         #If visited is none, we're going initialize it to equal set
    #         if visited is None:
    #             visited = set()
    #             traversal_path.append(n)
    #     #If the room has not been visited, add to visited
    #         if player not in visited:
    #             visited.add(player.current_room)
    #             Room.get_exits()
    #             complete = adventure_moves(n+1, traversal_path, room_list[i],limit)
    #         i + 1



    

