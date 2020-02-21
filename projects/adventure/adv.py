from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval


def reverse(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    else:
        return 'e'

def new_entry(room):
    visited_rooms[room.id] = {}

    for exit in room.get_exits():
            visited_rooms[room.id][exit] = '?'

def bfs():
    print("you're in bfs")
    room = player.current_room
    q = Queue()
    q.enqueue([room.id])
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        last = path[-1]

        if last not in visited:
            visited.add(last)

            for exit in visited_rooms[room.id]:
                if (visited_rooms[room.id][exit] == '?'):
                    return path
                new_path = path + [visited_rooms[room.id][exit]]
                q.enqueue(new_path)
    return path

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
# map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# TRAVERSAL TEST
s = Stack()
s.push(player.current_room)
visited_rooms = {}
new_entry(player.current_room)

while len(visited_rooms) < len(room_graph):
    print("START---visited rooms", visited_rooms) 
    room = s.pop()
    
    if room is None:
        print(player.current_room.id)
        path = bfs()
        print(path)
        # tranlate room id to direction
        for id in path:
            for exit in visited_rooms[player.current_room.id]:
                if (visited_rooms[player.current_room.id][exit] == id and player.current_room.id != id):
                    traversal_path.append(exit)
                    player.travel(exit)
                    print("BFS Current room", player.current_room.id)
                    # s.push(player.current_room)
                    break
    
    unexplored = []
    for exit in visited_rooms[room.id]:
            if (visited_rooms[room.id][exit] == '?'):
                unexplored.append(exit)
    
    for exit in visited_rooms[room.id]:
        if (visited_rooms[room.id][exit] == '?'):

            traversal_path.append(exit)

            new_room = room.get_room_in_direction(exit)

            visited_rooms[room.id][exit] = new_room.id

            new_entry(new_room)

            visited_rooms[new_room.id][reverse(exit)] = player.current_room.id

            player.travel(exit)
            print(player.current_room.id)
            s.push(player.current_room)

            unexplored.remove(exit)

print("END---visited rooms", visited_rooms)    


print(traversal_path)

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
