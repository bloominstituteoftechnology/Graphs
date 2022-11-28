from room import Room
from player import Player
from world import World

import random
from random import choice
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "/home/ubuntu/Github/CS/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# We'll Instantiate all necessary variables, lists, etc
rooms_seen = set()
# rooms_been = list() <-- List for tracing purposes
player.current_room = world.starting_room
rooms_seen.add(player.current_room.id)
# rooms_been.append(player.current_room.id)
last_move = ''
next_move = ''
fourway_rooms = dict()

#  We'll set our first move as east.
next_move = 'e'
traversal_path.append(next_move)

# Our while loop will continue until all rooms have been visitted
while len(rooms_seen) < 500:
    # We move in the chosen dir. and add the room to our visitted set
    player.travel(next_move)
    rooms_seen.add(player.current_room.id)
    # rooms_been.append(player.current_room.id) 

    last_move = next_move

    # This automates our 'right hand on the wall' traversal
    if last_move == 'e':
        if 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        else: 
            next_move = 'w'
    
    elif last_move == 'n':
        if 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        else: 
            next_move = 's'
    
    elif last_move == 'w':
        if 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        else: 
            next_move = 'e'

    elif last_move == 's':
        if 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        else: 
            next_move = 'n'

    # Four way intersections can cause eternal looping in a maze
    # This will ensure that all paths are traversed
    if len(player.current_room.get_exits()) == 4:
        current = player.current_room.id

        # create a dictionary for the intersection in question
        if current not in fourway_rooms:
            fourway_rooms[current] = []
        
        # add next move to the dictionary if the move is not already present
        if next_move not in fourway_rooms[current]:
            fourway_rooms[current].append(next_move)
        
        # if the next move is present, make a random choice of untraveled directions
        elif len(fourway_rooms[current]) < 4:
            next_move = choice([i for i in ['n', 's', 'e', 'w'] if i not in fourway_rooms[current]])
            fourway_rooms[current].append(next_move)
        
        # if we have traveled in all directions, then repeat the moves in order
        else:
            next_move = fourway_rooms[current][len(fourway_rooms[current])%4] #choice([i for i in ['n', 's', 'e', 'w']])
            fourway_rooms[current].append(next_move)
        
        # print(current, rooms_been[-10:], next_move, len(traversal_path), len(rooms_seen))


    # Add next_move to the traversal path
    traversal_path.append(next_move)

    if len(traversal_path) > 2000:
        break

# print(len(traversal_path))

print('Total Rooms traversed:', len(rooms_seen))
print('Length of Traversal Path:', len(traversal_path))
rooms_missed = []
for i in range(500):
    if i not in (rooms_seen):
        rooms_missed.append(i)

# print(rooms_missed) 



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    print(player.current_room.id, player.current_room.get_exits())

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
