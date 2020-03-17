from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Graph, Queue, Stack
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

graph = Graph()


# Populate graph by traversing through all the rooms
def populate_graph():
    stack = Stack()
    stack.push(world.starting_room)
    visited = set()

    while stack.size() > 0:
        room = stack.pop()
        room_id = room.id

        if room_id not in graph.vertices: 
            graph.add_vertex(room_id)

        exits = room.get_exits()
        for direction in exits:
            # find next rooms to add to graph
            next_rooms = room.get_room_in_direction(direction)
            next_rooms_id = next_rooms.id

            if next_rooms_id not in graph.vertices:
                graph.add_vertex(next_rooms_id)

            # connect rooms as edges with direction
            graph.add_edge(room_id, next_rooms_id, direction)

            if next_rooms_id not in visited:
                stack.push(next_rooms)
        visited.add(room_id)


def find_next_path(room_id, visited, g=graph):
    v = set()
    v.add(room_id)

    q = Queue()
    q.enqueue({room_id: []})

    while q.size() > 0:
        room_info = q.dequeue()
        # Room is current room, moves is what moves it took to get here
        room = list(room_info.keys())[0]
        moves = room_info[room]

        # Grab neighbors of room
        neighbors = g.get_neighbors(room)

        # Grabs keys. These are directions
        neighbors_keys = list(neighbors.keys())

        # This is a new dead end. Return set of directions for player to traverse
        if len(neighbors_keys) == 1 and neighbors[neighbors_keys[0]] not in visited:
            dead_end = list(moves) + [neighbors_keys[0]]
            return dead_end


        else:
            # Keep going through the graph until we hit a dead end
            for direction in neighbors:
                next_room = neighbors[direction]
                new_moves = moves + [direction]

                if next_room not in visited:
                    return new_moves

                if next_room not in v:
                    q.enqueue({next_room: new_moves})
                    v.add(next_room)



populate_graph()

traversal_path = []

visited = set()
visited.add(world.starting_room.id)

current_room_id = world.starting_room.id
total_rooms = len(graph.vertices)

while len(visited) < total_rooms:
    moves = find_next_path(current_room_id, visited)
    # Traverse the returned list of moves
    for direction in moves:
        player.travel(direction)
        traversal_path.append(direction)
        visited.add(player.current_room.id)
    # update current room
    current_room_id = player.current_room.id
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
