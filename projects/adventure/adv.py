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

def search_path(graph, start_room):
    
    path_queue = Queue()
    explored = set()
    
    path_queue.enqueue([start_room.id])

    while path_queue.size() > 0 :
        
        path = path_queue.dequeue()       
        current_room = path[-1]
        if current_room not in explored:
            explored.add(current_room)

            for room in graph[current_room]:
                if graph[current_room][room] == "?":
                    return path
                else:
                    new_room = graph[current_room][room]
                    new_path = path.copy()
                    new_path.append(new_room)
                    path_queue.enqueue(new_path)

def transform(graph,path):
    directions = []
    if len(path) == 0 :
        return directions
    else:
        for index in range(0,len(path)-1):      
            
            dirt = get_key(graph[path[index]],path[index + 1])       
            directions.append(dirt)
            
        return directions
        

                        
    
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
        
        if i not in our_graph[current_room.id]:
            break
        if our_graph[current_room.id][i] == "?":
            traversal_path.append(i)
            player.travel(i)
            new_room = player.current_room #traveled

            add_room(new_room,our_graph)

            our_graph[current_room.id][i] = new_room.id
            our_graph[new_room.id][opposite(i)] = current_room.id   

            current_room = new_room
            print("___________")
            print(current_room.id)
            print(our_graph)
            print(len(our_graph))
            print("___________")
            
      
    path = search_path(our_graph, current_room)
    directions = transform(our_graph,path)
    if directions is not None:
        
        traversal_path.extend(directions)
    
        for i in directions:
            if i in our_graph[current_room.id]:
                player.travel(i)
    current_room = player.current_room
            
            

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
