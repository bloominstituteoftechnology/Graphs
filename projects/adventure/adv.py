from room import Room
from player import Player
from world import World
from utils import Queue, Stack
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

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#helper function to get reverse of given direction
def reverse_dir(dir):
    if dir == "n":
        return "s"
    elif dir == "s":
        return "n"
    elif dir == "e":
        return "w"
    elif dir == "w":
        return "e"



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
moves = Stack()
while len(visited_rooms) < len(world.rooms):
    exits = player.current_room.get_exits()
    dirs = []
    # checks all exits in a room
    # if the room in the direction of the exit has not been visited
    # append to dirs
    for exit in exits:
        if exit is not None and player.current_room.get_room_in_direction(exit) not in visited_rooms:
            dirs.append(exit)
    # add room visited set
    visited_rooms.add(player.current_room)
    # if there are directions to move in
    # pick a random one available
    # push that dir onto moves stack
    # move the player in that direction
    # append move to travarseral path
    if len(dirs) > 0:
        rand_dir = random.randint(0, len(dirs) -1)
        moves.push(dirs[rand_dir])
        player.travel(dirs[rand_dir])
        traversal_path.append(dirs[rand_dir])
    # if there are no directions to move in
    # get the last move made
    # move the player in the reveres direction of last move
    # append move to traversal path
    else:
        last_move = moves.pop()
        player.travel(reverse_dir(last_move))
        traversal_path.append(reverse_dir(last_move))



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
