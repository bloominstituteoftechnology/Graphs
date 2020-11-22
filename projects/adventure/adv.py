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
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map≥
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


def bfs(starting_vertex):
    q = []
    visit = set()
    path = [starting_vertex]
    travel = []
    q.append(path)
    # is the node in graph
    # while queue isn't empty
    while len(q) > 0:
        # dequeue the node at the front of the line
        current_path = q.pop(0)
        current_node = current_path[-1]
        # print("current_node bfs", current_node)
    # if this node is a target node, return true
        if has_exits(current_node):
            # print("has exits", has_exits(current_node))
            # print("travel", travel)
            # print("traversal p before", traversal_path)
            traversal_path.extend(travel)
            # print("traversal p after", traversal_path)
            return current_path

            # return current_path
        if current_node not in visit:
            visit.add(current_node)
            neighbors = player.current_room.get_exits()

            for i in neighbors:
                # print("visited nodes", visit)
                # print("ALL THE STUFFS", i, graph[player.current_room.id],
                #   current_node)
                if graph[current_node][i] == "?":
                travel.append(i)
                player.travel(i)
                q.append(current_path + [player.current_room.id])
                
        else:
            print("whoopsie,", current_node)


def has_exits(vertex):
    free = []
    # print('has exits vertex', graph[vertex], vertex)
    # print("get room id", player.current_room.id)
    # print("get room exits", player.current_room.get_exits())
    for key, value in graph[vertex].items():
        if value == "?":
            free.append(key)
            print("free", free)
    # for i in player.current_room.get_exits():
    #     if graph[vertex][i] == "?":
    #         free.append(i)
        # print("free in the appaned", free)
    if len(free) > 0:
        # print("free", free)
        return free
    # print("false on has exits")
    return False


traversal_path = []
graph = {}
current = player.current_room.id
visited = []
nodes = []
last = ''

s = []
s.append(current)
print(current, "current")
print(len(world.rooms))

while len(visited) != len(world.rooms):
    vertex = s.pop()
    nodes.append(vertex)
    # print("vertex", vertex)
    exits = player.current_room.get_exits()
    index = random.randint(0, len(exits)-1)
    random_dir = exits[index]
    free_exits = []

    if vertex not in visited:
        graph[vertex] = {}
        visited.append(vertex)
        # print("visited", visited)
        for i in exits:
            graph[vertex][i] = "?"
        if len(traversal_path) > 0:
            last = traversal_path[-1]
            # print("traversal path", traversal_path)
            # print("Nodes", nodes)
            if last == "n":
                if graph[vertex]['s'] == "?":
                    graph[vertex]['s'] = nodes[-2]
            elif last == "s":
                if graph[vertex]['n'] == "?":
                    graph[vertex]['n'] = nodes[-2]
            elif last == "w":
                if graph[vertex]['e'] == "?":
                    graph[vertex]['e'] = nodes[-2]
            elif last == "e":
                if graph[vertex]['w'] == "?":
                    graph[vertex]['w'] = nodes[-2]
        for i in exits:
            if graph[vertex][i] == "?":
                free_exits.append(i)
                # print("free exits", free_exits)
        if len(free_exits) > 1:
            index = random.randint(0, len(free_exits)-1)
            random_dir = free_exits[index]
            player.travel(random_dir)
            traversal_path.append(random_dir)
            graph[vertex][random_dir] = player.current_room.id
            s.append(player.current_room.id)
        elif len(free_exits) == 1:
            player.travel(free_exits[0])
            traversal_path.append(free_exits[0])
            graph[vertex][free_exits[0]] = player.current_room.id
            s.append(player.current_room.id)
        else:
            if len(visited) == len(world.rooms):
                break

            new_vertex = bfs(player.current_room.id)
            print(graph)
            print("new vertex", new_vertex)
            print("traversal length", len(traversal_path))
            s.append(new_vertex[-1])
    else:
        if len(traversal_path) > 0:
            last = traversal_path[-1]
            if last == "n":
                if graph[vertex]['s'] == "?":
                    graph[vertex]['s'] = nodes[-2]
            elif last == "s":
                if graph[vertex]['n'] == "?":
                    graph[vertex]['n'] = nodes[-2]
            elif last == "w":
                if graph[vertex]['e'] == "?":
                    graph[vertex]['e'] = nodes[-2]
            elif last == "e":
                if graph[vertex]['w'] == "?":
                    graph[vertex]['w'] = nodes[-2]
        for i in exits:
            if graph[vertex][i] == "?":
                free_exits.append(i)
        if len(free_exits) > 0:
            index = random.randint(0, len(free_exits)-1)
            random_dir = free_exits[index]
            player.travel(random_dir)
            traversal_path.append(random_dir)
            graph[vertex][random_dir] = player.current_room.id
            s.append(player.current_room.id)
        else:
            # find an open exit vertex and travel there.
            if len(visited) == len(world.rooms):
                break
            # print("not visited vertex", vertex)
            # print("not visited current room", player.current_room.id)
            # print("bfs not visited", bfs(player.current_room.id))
            new_vertex = bfs(player.current_room.id)
            # print("new vertex to be added", new_vertex[-1])
            s.append(new_vertex[-1])
        # print(vertex)
        # print(free_exits)


print("final graph", graph)
print("final len visited", len(visited))
print("final len rooms", len(world.rooms))
print(has_exits(graph[0])

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
