from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
reversed_path = []
rooms = {}
opposite_Directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

rooms[0] = player.current_room.get_exits()
'''
rooms:  {0: ['n', 's', 'w', 'e']} 

  room_graph:  {
   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
   1: [(3, 6), {'s': 0, 'n': 2}],
   2: [(3, 7), {'s': 1}],
   3: [(4, 5), {'w': 0, 'e': 4}],
   4: [(5, 5), {'w': 3}],
   5: [(3, 4), {'n': 0, 's': 6}], 
   6: [(3, 3), {'n': 5}],
   7: [(2, 5), {'w': 8, 'e': 0}], 
   8: [(1, 5), {'e': 7}]} 


rooms:  {0: ['s', 'w', 'e']} 

  room_graph:  {
   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
   1: [(3, 6), {'s': 0, 'n': 2}],
   2: [(3, 7), {'s': 1}],
   3: [(4, 5), {'w': 0, 'e': 4}],
   4: [(5, 5), {'w': 3}],
   5: [(3, 4), {'n': 0, 's': 6}], 
   6: [(3, 3), {'n': 5}], 
   7: [(2, 5), {'w': 8, 'e': 0}], 
   8: [(1, 5), {'e': 7}]} 


rooms:  {0: ['s', 'w', 'e'], 1: []} 

  room_graph:  {0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
   1: [(3, 6), {'s': 0, 'n': 2}],
   2: [(3, 7), {'s':    1
   ], 3: [(4, 5)   , {'w': 0, 'e': 4}],
   4: [(5, 5), {'w':
    3}], 5: [(3, 4), {'n': 0, 's': 6}], 
   6: [(3, 3), {
       'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 
   8: [(1, 5), {'e': 7}]} 


rooms:  {0: ['w', 'e'], 1: [], 2: []} 

  room_graph:  {
   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
   1: [(3, 6), {'s': 0, 'n': 2}],
   2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}],
   4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 
   6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 
   8: [(1, 5), {'e': 7}]} 


rooms:  {0: ['w', 'e'], 1: [], 2: [], 5: []} 

  room_graph:  {
   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
   1: [(3, 6), {'s': 0, 'n': 2}],
   2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}],
   4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 
   6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 
   8: [(1, 5), {'e': 7}]} 


rooms:  {0: ['e'], 1: [], 2: [], 5: [], 6: []} 

  room_graph:  {
   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
   1: [(3, 6), {'s': 0, 'n': 2}],
   2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}],
   4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 
   6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 
   8: [(1, 5), {'e': 7}]} 


rooms:  {0: ['e'], 1: [], 2: [], 5: [], 6: [], 7: []} 

  room_graph:  {
   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
   1: [(3, 6), {'s': 0, 'n': 2}],
   2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}],
   4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 
   6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 
   8: [(1, 5), {'e': 7}]} 


rooms:  {0: [], 1: [], 2: [], 5: [], 6: [], 7: [], 8: []} 

  room_graph:  {
   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
   1: [(3, 6), {'s': 0, 'n': 2}],
   2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}],
   4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 
   6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 
   8: [(1, 5), {'e': 7}]} 
'''
while len(rooms) < len(room_graph) - 1:
    print("rooms: ", rooms, "\n\n", " room_graph: ", room_graph, "\n\n")
    if player.current_room.id not in rooms:
        rooms[player.current_room.id] = player.current_room.get_exits()
        lastRoom = reversed_path[-1]
        rooms[player.current_room.id].remove(lastRoom)

    # while room is empty
    while len(rooms[player.current_room.id]) < 1:
        reverse = reversed_path.pop()
        traversal_path.append(reverse)
        player.travel(reverse)

    exit_dir = rooms[player.current_room.id].pop(0)
    traversal_path.append(exit_dir)
    reversed_path.append(opposite_Directions[exit_dir])
    player.travel(exit_dir)


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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
