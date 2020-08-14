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
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# where have we been
traveled_rooms = set()

# initalize the starting room
player.current_room = world.starting_room

# if we visit a room add it to the list
traveled_rooms.add(player.current_room.id)

# need to track our moves
# need to track both last move and the next one (next_room is confusing but current move doesnt seem right either )
prev_move = ''
next_move = ''
 # so if you go into a room with all four directions avail it will break need to fix that... 
all_ways_room = dict()

# set our initial move to e because I read the directions for the most part this time
next_move = 'e'

# need to add our moves to the traversal path 
traversal_path.append(next_move)

# we have to hit all 500 rooms for the test honestly i should make this scalable to any list ***** come back to this ********
#  found right hand on wall slides from stanford https://cs.stanford.edu/people/eroberts/courses/cs106b/handouts/16-RecursiveBacktracking.pdf
while len(traveled_rooms) < 500:
    # based on the last direction i need to see what directions are available and then chose one from there
    # move the player
    player.travel(next_move)
    # add room to traveled_rooms
    traveled_rooms.add(player.current_room.id)
    # when you move you need to set that next move to your last move
    prev_move = next_move
   

    # we need to check for what ways we can move per each prev move, repeat it for each possible move
    # probably is a better way to do this...... i wonder if this method is just not the best from the start
    if prev_move == 'e':
        if 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        else: 
            next_move = 'w'

    elif prev_move == 'n':
        if 'e' in player.current_room.get_exits():
            next_move = 'e'
        elif 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        else: 
            next_move = 's'

    elif prev_move == 'w':
        if 'n' in player.current_room.get_exits():
            next_move = 'n'
        elif 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        else: 
            next_move = 'e'

    elif prev_move == 's':
        if 'w' in player.current_room.get_exits():
            next_move = 'w'
        elif 's' in player.current_room.get_exits():
            next_move = 's'
        elif 'e' in player.current_room.get_exits():
            next_move = 'e'
        else: 
            next_move = 'n'

# this causes a infinite loop sometimes.........
# if the room has all the exit directions available, need to log that room, then when i go a specific direction in that room at it to the list, when i get back to that room check that list to make sure that I havent gone that way before and repeat.
# think about this like marking what way i have already gone with chalk on the door. That way we dont just go in circles
    if len(player.current_room.get_exits()) == 4:
        current = player.current_room.id

        if current not in all_ways_room:
            all_ways_room[current] = []
    # set up the dict using curr as in i and then below this add the next move if it wasnt already in there that way we keep track
        if next_move not in all_ways_room[current]:
            all_ways_room[current].append(next_move)
    # if the next move is in there we need to have it go a different route. look up random choice from list, https://pynative.com/python-random-choice/ found that before going to bed ****** look at this in the morning
    # need to figure out what to do when we go through all the options aswell going to have to go back
        elif len(all_ways_room[current] ) < 4:
            next_move = choice([i for i in ['n', 's', 'e', 'w'] if i not in all_ways_room[current]])
            all_ways_room[current].append(next_move)
        else:
            next_move = all_ways_room[current][len(all_ways_room[current])%4] #choice([i for i in ['n', 's', 'e', 'w']])
            all_ways_room[current].append(next_move)
    traversal_path.append(next_move)
    if len(traveled_rooms) >2000:
        print('didnt pass')
        break
print("all the rooms I went too", len(traveled_rooms))
print(len(traversal_path))
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
