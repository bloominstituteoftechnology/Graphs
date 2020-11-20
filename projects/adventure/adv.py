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

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
opp = {
    "n": "s",
    "e": "w",
    "s": "n",
    "w": "e",
}

graph = {
    player.current_room.id: {
        d: "?" for d in player.current_room.get_exits()
    }
}

matrix = [
    ["?" for _ in range(60)]
    for _ in range(60)
]
ic = {
    "n": (-1, 0),
    "e": (0, 1),
    "s": (1, 0),
    "w": (0, -1),
}
matrix[30][30] = 0
loc = (30, 30)

traversal_path = []

def bfs(room_id):
    visited = set()
    q = [[(room_id, "_")]]
    while q:
        p = q.pop(0)
        curr, dir = p[-1]
        if curr in visited:
            continue
        visited.add(curr)
        for d, r in graph[curr].items():
            if r == "?":
                return p[1:]
            q.append(p + [(r, d)])
    return []

def update(last, curr, d):

    global loc

    # update traversal path
    traversal_path.append(d)

    # update location
    lat, lon = loc
    lat_t, lon_t = ic[d]
    lat += lat_t
    lon += lon_t
    loc = (lat, lon)

    if curr in graph:
        return

    # update graph
    exits = player.current_room.get_exits()
    random.shuffle(exits)
    graph[curr] = {
        d: "?" for d in exits
    }
    graph[last][d] = curr
    graph[curr][opp[d]] = last

    # update matrix
    if matrix[lat][lon] != "?":
        print(f"warning: matrix not updated properly: {matrix[lat][lon]}, {curr}")
        for line in matrix:
            print(" ".join([str(x) for x in line]))
    matrix[lat][lon] = curr

    for d, (lat_t, lon_t) in ic.items():
        loc_t = (loc[0] + lat_t, loc[1] + lon_t)
        room_t = matrix[loc_t[0]][loc_t[1]]
        if room_t == "?":
            continue
        if d in graph[curr]:
            graph[curr][d] = room_t
            graph[room_t][opp[d]] = curr


path = None
for step in range(2000):

    room = player.current_room.id
    #print(f"Current room: {room}")
    has_moved = False

    if path:
        next_room, next_dir = path.pop(0)
        player.travel(next_dir)
        update(room, next_room, next_dir)
        #print(f"moving by path: {room} to {next_room}, {next_dir}")
        continue

    for d, v in graph[room].items():
        if v == "?":
            player.travel(d)
            new_room = player.current_room.id
            update(room, new_room, d)
            has_moved = True
            #print(f"moving into unknown: {room} to {new_room}, {d}")
            break
    if has_moved:
        continue

    # perform bfs
    path = bfs(room)
    if not path:
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