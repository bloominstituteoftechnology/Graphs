from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


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



def opposite(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'
#QUEUE:
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def get_key(dic,val):
    for key,value in dic.items():
        if val == value:
            return key
    return "Key doesnt exit"

def search_path(room_graph, start_room):

    path_queue = Queue()
    explored = set()

    path_queue.enqueue([start_room.id])
    path_dir = []
    while path_queue.size() > 0 :
        path = path_queue.dequeue()
        
        
        current_room_id = path[-1]

        if current_room_id in explored:
            continue
        else:
            explored.add(current_room_id)
            rooms = room_graph[current_room_id].values()
            
            for room in rooms:
                if room == "?":
                    
                    return path_dir #goes to the point where there is a ?
                else:
                    next_path = path.copy()
                    next_path.append(room)
                    path_queue.enqueue(next_path)
                    dirt = get_key(room_graph[current_room_id],room)
                    oppo_dirt = opposite(dirt)
                    path_dir.append(oppo_dirt)



our_graph = {}
def add_room(room,graph):
    if room.id not in graph:
        graph[room.id] = {}
        for exit in room.get_exits():
            graph[room.id][exit] = "?"

while len(our_graph) < len(room_graph):
    
    current_room = player.current_room

    add_room(current_room,our_graph)
    
    for i in our_graph[current_room.id]:
        print(current_room)
        print(i)
        print(our_graph)
        if i not in our_graph[current_room.id]:
            break
        if our_graph[current_room.id][i] == "?":
            
            traversal_path.append(i)
            player.travel(i)
            new_room = player.current_room #traveled

            add_room(new_room,our_graph)
            
            #put id of 2 room into each others connection
            our_graph[current_room.id][i] = new_room.id
            # print(our_graph[current_room.id][i])
            our_graph[new_room.id][opposite(i)] = current_room.id
            # print(our_graph[new_room.id][opposite(i)])
            current_room = new_room
            
      
    track = search_path(our_graph, current_room)
    if track is not None:
        traversal_path.extend(track)
        
        for i in track:
            if i in our_graph[current_room.id]:
                player.travel(i)
    current_room = player.current_room
            
            







        

# search_path(room_graph, world.starting_room)



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
