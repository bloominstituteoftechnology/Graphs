from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from queue import Queue

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = r"projects\adventure\maps\test_line.txt"
# map_file = r"projects\adventure\maps\test_cross.txt"
map_file = r"projects\adventure\maps\test_loop.txt"
# map_file = r"projects\adventure\maps\test_loop_fork.txt"
# map_file = r"projects\adventure\maps\main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

print('Room Graph: ', room_graph) 
print('Type: ', type(room_graph))
print('Length: ', len(room_graph))

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Start by writing an algorithm that picks a random unexplored direction from the player's current room, travels and logs that direction, then loops. This should cause your player to walk a depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the nearest room that does contain an unexplored path.

# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

explored = {}
visited_rooms = {}

# while len(visited_rooms) < len(room_graph): 

#     # player in current room 
#     player.current_room.id() 
#     # get exits 
#     player.current_room.get_exits() 
#     player.travel(direction)
#     if yes: 
#         path.append[direction]
#         check exits 
#     if no: 
#         travel 

for room in room_graph.keys(): 
    explored[room] = {}    
    print('Room Key:', room)
    for direction in room_graph[room][1]: 
        print('Direction: ', direction, ': ', room_graph[room][1][direction])
        if direction == 'n': 
            print(room_graph[room][1][direction])
            explored[room][direction] = False
        elif direction == 's': 
            print(room_graph[room][1][direction])
            explored[room][direction] = False
        elif direction == 'e': 
            print(room_graph[room][1][direction])
            explored[room][direction] = False
        elif direction == 'w': 
            print(room_graph[room][1][direction])
            explored[room][direction] = False
        else:
            print('No exits in room ', room_graph[room])

print('New length: ', len(explored))
print('New graph', explored)

# To solve this path, you'll want to construct your own traversal graph. You start in room `0`, which contains exits `['n', 's', 'w', 'e']`. Your starting graph should look something like this:

# ```
# {
#   0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
# }
# ```

# Try moving south and you will find yourself in room `5` which contains exits `['n', 's', 'e']`. You can now fill in some entries in your graph:

# ```
# {
#   0: {'n': '?', 's': 5, 'w': '?', 'e': '?'},
#   5: {'n': 0, 's': '?', 'e': '?'}
# }
# ```

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
