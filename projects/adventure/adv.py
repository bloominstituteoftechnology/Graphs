from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
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

while len(graph) < num_rooms:  
    print(f'Length of graph: {len(graph)}')
    # get a list of exits from the current room
    current_room = player.current_room.id
    print(f"You are in Room {current_room}")

    exits = player.current_room.get_exits() # returns list of exits
    print(f"The exits are {exits}")

    if current_room not in graph:
        graph[current_room] =  {}

    unexplored_exits = [d for d in exits if d not in graph[current_room]]
    print(f"You haven't explored {unexplored_exits}")
    
    # check if there are unexplored exits

    #if there aren't, backtrack until there are
    if len(unexplored_exits) == 0:
        steps_back = 0
        traversal_copy = traversal_path.copy()
        
        while len(unexplored_exits) == 0:
            # if not, backtrack to the closest one with BFS (eventually)
            # for now lets brute force it
            '''
            Breadth First Search
            Backtracking
            '''
            steps_back -= 1
            reverse_direction = opposite[traversal_copy[steps_back]]
            print(f"The reverse direction is {reverse_direction}")
            player.travel(reverse_direction)
            print(f"Backtracked to {reverse_direction}")
            traversal_path.append(reverse_direction)
            current_room = player.current_room.id
            print(f"Current room is {current_room}")
            
            exits = player.current_room.get_exits() # returns list of exits
            unexplored_exits = [d for d in exits if d not in graph[current_room]]
        
        
    direction = random.choice(unexplored_exits)

    # randomly select an exit and travel in that direction
    player.travel(direction)
    print(f'travelled {direction}')
    traversal_path.append(direction)
    # print(f"Traversal path: {traversal_path}")

    # record the connections
    new_room = player.current_room.id
    graph[current_room][direction] = new_room
    graph[new_room] = {}
    graph[new_room][opposite[direction]] = current_room
    


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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
