from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

import sys
sys.path.append(r"C:\Users\Samuel\repos\Graphs\projects\graph")

from util import Stack
import operator

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\test_line.txt"
map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\test_cross.txt"
# map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\test_loop.txt"
# map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\test_loop_fork.txt"
# map_file = r"c:\Users\Samuel\repos\Graphs\projects\adventure\maps\main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Passed Line Test:

# while player.current_room.n_to:
#     player.current_room = player.current_room.n_to
#     traversal_path.append('n')


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# Pass Cross Test:

# Implement DFT using dictionary as a graph

# Create adjacency_dict
adjacency_dict = {}

# adjacency_dict[player.current_room.id] = {
#     "n": player.current_room.n_to.id,
#     "s" : player.current_room.s_to.id,
#     "e" : player.current_room.e_to.id,
#     "w" : player.current_room.w_to.id
#     }

# adjacency_dict[player.current_room.id] = {}

# attributes = ["n_to", "s_to", "e_to", "w_to"]
# for attr in attributes:
#     if operator.attrgetter(f"current_room.{attr}")(player):
#         adjacency_dict[player.current_room.id][attr[0]] = operator.attrgetter(f"current_room.{attr}.id")(player)
#     else:
#         adjacency_dict[player.current_room.id][attr[0]] = operator.attrgetter(f"current_room.{attr}")(player)

# for direction in adjacency_dict[player.current_room.id]:
#     print(direction, adjacency_dict[player.current_room.id][direction])

# Use a stack to store values
# s = Stack()
# # push current room on to stack
# s.push(player.current_room.id)
# # while stack.size() > 0:
# while s.size() > 0:
#     # pop current room off
#     current = s.pop()
#     adjacency_dict[current] = {}
#     attributes = ["n_to", "s_to", "e_to", "w_to"]
#     for attr in attributes:
#         if operator.attrgetter(f"current_room.{attr}")(player):
#             adjacency_dict[current][attr[0]] = operator.attrgetter(f"current_room.{attr}.id")(player)
#         else:
#             adjacency_dict[current][attr[0]] = operator.attrgetter(f"current_room.{attr}")(player)

#     random.seed(random.randint(0, 100))
#     val = random.choice(attributes)
#     if operator.attrgetter(f"current_room.{val}")(player):
#         traversal_path.append(val[0])

#     current = player.current_room
#     s.push(current.id)



# Refactoring the above code to be recursive:)

def traverse_map(current_room, traversal_path, adjacency_dict, limit):
    if len(visited_rooms) == len(room_graph):
        return

    if len(traversal_path) > limit:
        return

    adjacency_dict[player.current_room.id] = {}
        
    attributes = ["n_to", "s_to", "e_to", "w_to"]

    for attr in attributes:
        print(operator.attrgetter(f"current_room.{attr}")(player))
        if operator.attrgetter(f"current_room.{attr}")(player):
            adjacency_dict[player.current_room.id][attr[0]] = operator.attrgetter(f"current_room.{attr}.id")(player)
        else:
            adjacency_dict[player.current_room.id][attr[0]] = operator.attrgetter(f"current_room.{attr}")(player)

    current_adj = adjacency_dict

    current_room = player.current_room

    if player.current_room.n_to:
        current_room = current_room.n_to
        traversal_path.append('n')

    if player.current_room.s_to and player.current_room.n_to is None:
        current_room = current_room.s_to
        traversal_path.append('s')
    
    if player.current_room.e_to and player.current_room.n_to is None and player.current_room.s_to is None:
        current_room = current_room.e_to
        traversal_path.append('e')

    if player.current_room.w_to and player.current_room.n_to is None and player.current_room.s_to is None and player.current_room.e_to is None:
        current_room = current_room.e_to
        traversal_path.append('w')

    current_path = traversal_path
    print(current_path)
    print(player.current_room.n_to)
    
    traverse_map(current_room, current_path, current_adj, limit - 1)

traverse_map(player.current_room, traversal_path, adjacency_dict, 14)    


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
