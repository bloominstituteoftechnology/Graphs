from room import Room
from player import Player
from world import World
import collections
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

traversal_path = []
reverse = {"n": "s", "s": "n", "e": "w", "w": "e"}
maze_graph = {}

def starting_room():
    direction_dict = {}
    room = player.current_room
    exits = player.current_room.get_exits()
    for way_out in exits:
        direction_dict[way_out] = "?"
    maze_graph[room.id] = direction_dict
    print(maze_graph)

def explore(direction):
    direction_dict = {}
    current = player.current_room.id
    room = player.current_room.get_room_in_direction(direction)
    player.travel(direction)
    
    maze_graph[current][direction] = room.id
    if room.id not in maze_graph:
        for way_out in room.get_exits():
            some_room = room.get_room_in_direction(way_out)
            if some_room.id not in maze_graph:
                direction_dict[way_out] = "?"
            elif way_out is reverse[direction]:
                direction_dict[way_out] = current
            elif maze_graph[some_room.id][reverse[way_out]] == "?":
                maze_graph[some_room.id][reverse[way_out]] = room.id
        maze_graph[room.id] = direction_dict
    traversal_path.append(direction)

def closest_unexplored_path(room_id):
    queue = collections.deque([])
    path = []
    queue.append([(room_id, None)])
    checked_rooms = set()
    while queue:
        path = queue.popleft()
        room_tuple = path[-1]
        for direction, room in maze_graph[room_tuple[0]].items():
            if room not in checked_rooms:
                shortest = list(path)
                shortest.append((room, direction))
                checked_rooms.add(room)
                queue.append(shortest)
                if room == "?":
                    shortest.pop(0)
                    path = [item[1] for item in shortest]
                    print(f"Players Current Room: {player.current_room.id}")
                    return path
    return []

def complete_maze(start):
    stack = collections.deque([])
    stack.append(start)
    starting_room()
    while stack:
        direction = stack.pop()
        room = player.current_room
        next_room = room.get_room_in_direction(direction)
        print(f"Players Current Room: {player.current_room.id}")
        exits = set(room.get_exits())
        if next_room:
            explore(direction)
            print(f"Players Current Room: {player.current_room.id}")
            stack.append(direction)
        if not stack:
            for way_out in exits:
                if maze_graph[room.id][way_out] == "?":
                    explore(way_out)
                    print(f"Players Current Room: {player.current_room.id}")
                    stack.append(way_out)
                    break
        if not stack:
            if len(maze_graph.keys()) is len(room_graph.keys()):
                return 
            path_to_unexplored = closest_unexplored_path(player.current_room.id)
            for i in range(len(path_to_unexplored)):
                explore(path_to_unexplored[i])
                if i is len(path_to_unexplored) - 1:
                    stack.appendleft(path_to_unexplored[i])
    print(f"Length of maze graph: {len(maze_graph.keys())}")
complete_maze("n")


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