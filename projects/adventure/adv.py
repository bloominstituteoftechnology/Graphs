from room import Room
from player import Player
from world import World
from util import Stack, Queue

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

graph = {}

backwards_path = []

def add_vertex(room, prev_room_id=None, dir=None):
    e = {}
    for exit in room.get_exits():
        if dir == 'n' and exit == 's':
            e[exit] = prev_room_id
        elif dir == 's' and exit == 'n':
            e[exit] = prev_room_id
        elif dir == 'e' and exit == 'w':
            e[exit] = prev_room_id
        elif dir == 'w' and exit == 'e':
            e[exit] = prev_room_id
        else:
            e[exit] = '?'
    graph[room.id] = e

def get_neighbors(room):
    neighbors = []

    for exit in room.get_exits():
        neighbors.append(room.get_room_in_direction(exit))

    return neighbors

def get_opposite_exit(exit):
    if exit == 'n':
        return 's'
    elif exit == 's':
        return 'n'
    elif exit == 'w':
        return 'e'
    elif exit == 'e':
        return 'w'

def direction(room, visited):
    # array of exits from your current room
    exits = []
    for exit in room.get_exits():
        if graph[room.id][exit] == '?':
            exits.append(exit)
    if len(exits) > 0:
        # finds a random exit from that array
        i = random.randrange(0, len(exits))
        next_room = room.get_room_in_direction(exits[i])
        graph[room.id][exits[i]] = next_room.id
        player.travel(exits[i])
        # put in traversal map
        traversal_path.append(exits[i])
        # form the backwards path
        backwards_path.append(get_opposite_exit(exits[i]))
        if next_room not in visited:
            add_vertex(next_room, room.id, exits[i])
        else:
            # print("Already in vertex", graph[next_room.id])
            graph[next_room.id][get_opposite_exit(exits[i])] = room.id
        # print(graph)
        return next_room

    return None

def all_paths_explored(room):
    for exit in room.get_exits():
        if graph[room.id][exit] == '?':
            return False

    return True

def backtrack_v2(room):

    while len(backwards_path) > 0:
        path = backwards_path.pop()
        traversal_path.append(path)
        player.travel(path)
        room_id = player.current_room.id
        for exit in player.current_room.get_exits():
            if graph[room_id][exit] == '?':
                return player.current_room

def traverse_map(starting_room):

    q = Queue()
    q.enqueue([starting_room])

    backtrack_rooms = []
    visited = set()
    print(len(world.rooms))
    while len(visited) < len(world.rooms):
        while q.size() > 0:
            rooms = q.dequeue()
            room = rooms[-1]

            if room not in visited:
                print(room.id)
                visited.add(room)

            # choose direction in room to move to
            next_room = direction(room, visited)
            if next_room:
                q.enqueue(rooms + [next_room])
            else:
                # backtrack till you find a room with exits
                next_room = backtrack_v2(room)
                if next_room:
                    q.enqueue(rooms + [next_room])


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

add_vertex(player.current_room)

traverse_map(player.current_room)

# print(len(graph), graph)
# print(traversal_path)

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