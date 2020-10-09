from room import Room
from player import Player
from world import World
from util import Queue
import random
from ast import literal_eval

# Load world
world = World()
def get_neigbor(coord):
    neighbor = []

    n,s,w,e = coord
    if n > 0 and room_graph[n-1][s][w][e]== '?':
        neighbor.append((n-1, s, w, e))
    if n < len(room_graph) - 1 and room_graph[n+1][s][w][e] == '?':
        neighbor.append((n+1, s, w, e))
    if s > 0 and room_graph[n][s-1][w][e] == '?':
        neighbor.append((n, s-1, w, e))
    if s< len(room_graph[n][s][w][e]) and room_graph[n+1][s][w][e] == '?':
        neighbor.append((n+1, s, w, e))

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
visited = set()
path = []
room = {}
reverse_room = {'n': 's','s': 'n','e': 'w','w': 'e'}
counter = 0

# while we haven't visited all the rooms
while len(visited) < len(room_graph):
    # Get the id of the current room
    current_room = player.current_room.id
    # Check if we've visited that room.
    if current_room not in visited:
        # if not add it to visited.
        visited.add(current_room)
        # get list of all possible exits (or edges or neighbors)
        can_visite_direction = player.current_room.get_exits()
        # add them to our dictionary
        room[current_room] = can_visite_direction

    # loop all the possible directions in the current room
    while len(room[current_room]) >= 0:
        # if still directions to visit. 
        if len(room[current_room]) > 0: 
            # take move from the room queue.
            move = room[current_room].pop()

            get_room = move[-1]
            # get_room = player.current_room.get_room_in_direction(move).id
            # if the id of that room to be visited not  in visited yet.
            if get_room not in visited:
                # add it to the path tracker
                path.append(move)
                # save the move
                traversal_path.append(move)
                # add the move to the room
                player.travel(move)
                counter += 1
               
                break
            # if there are no directions left to move, move back
        elif len(room[current_room]) == 0:
            # take our last move from the path tracker
            last_move = path.pop()
            # find the return direction.
            prior_direction = reverse_room[last_move]
            # save the move
            traversal_path.append(prior_direction)
            # make the move
            player.travel(prior_direction)
            counter += 1
            break


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
