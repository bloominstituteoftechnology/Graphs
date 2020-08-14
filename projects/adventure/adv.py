from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
'''
I need to get to all rooms at least once

By playing around I figured out I would need to do a while loop
For as long as len(visited) < len(room_graph) I need to do some work

    Starting in room 000
    Need to get the id of the room I am in
    Make sure I add this room to visited right away
    Then I need to get the exits in that room. Store them? Dataset?

    Yes because if that dataset has stuff in it
        Get the direction in that dataset
        Add it to the path
        HUGE PART -> Make a store of opposites (Make opposites dict and previous list)
        Have the dude walk that path

    Otherwise
        We need to go backward and we get that direction from the previous list
        Add that direction to the path
        Make the dude walk that
'''

'''
SETTING UP VARIABLES
'''

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

'''
PLAYING AROUND TO FIND WHAT PRINTS WHAT
# players_current_room = player.current_room
# current_rooms_id = player.current_room.id
# current_rooms_exits = player.current_room.get_exits()
# number_of_rooms_in_map = len(list(room_graph.keys()))

# print(players_current_room)
# # print(f"CURRENT ROOM ID: {current_rooms_id}")
# # print(f"CURRENT EXITS: {current_rooms_exits}")
# print("")
# print(f"NUMBER OF ROOMS IN MAP: {number_of_rooms_in_map}")
'''

# Set up opposite directions
opposite_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}

# Keep track of previous room
previous_room = [None]

room_and_exit_dataset = {}
visited = set()

'''
LOGIC
'''
# This is like the get_neighbors model
def get_exits(roomId):
    directions = []
    if 'n' in room_graph[roomId][1].keys():
        directions.append('n')
    if 'e' in room_graph[roomId][1].keys():
        directions.append('e')
    if 's' in room_graph[roomId][1].keys():
        directions.append('s')
    if 'w' in room_graph[roomId][1].keys():
        directions.append('w')
    return directions

# def get_opposite(direction):
#     cardinal = []
#     if direction is 'n':
#         cardinal.append('s')
#     if direction is 's':
#         cardinal.append('n')
#     if direction is 'e':
#         cardinal.append('w')
#     if direction is 'w':
#         cardinal.append('e')
#     return cardinal
    

# I want to check the length of my visited against the length of the graph.
while len(visited) < len(room_graph):

    # Getting room id
    room_id = player.current_room.id

    # If this room not in the queue
    if room_id not in visited:

        # Add to visited
        visited.add(room_id)

        # Add to room queue as well
        room_and_exit_dataset[room_id] = get_exits(room_id)
        # room_and_exit_dataset.append(player.current_room.get_exits())

    # Eventually would have no more directions
    if len(room_and_exit_dataset[room_id]) is not 0:

        # Get the next direction to go in. Get it from the room Q
        next_direction = room_and_exit_dataset[room_id].pop(0)

        # Add that direction to the traversal path
        traversal_path.append(next_direction)

        # Add to my previous room from opposite directions dictionary
        previous_room.append(opposite_directions[next_direction])

        # Then travel
        player.travel(next_direction)

    else:
        # So we go back and get those directions from our previous room list
        previous_direction = previous_room.pop()

        # We add those move to the path
        traversal_path.append(previous_direction)

        # Tell the player to travel back
        player.travel(previous_direction)


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