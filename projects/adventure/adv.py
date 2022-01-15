import sys
sys.path.append('../graph')

from util import Stack, Queue

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

#construct a  traversal graph
#do dft for finding all the possible  room player can move
#do bfs for finding unexplored direction

# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()


player = Player(world.starting_room)
player.current_room = world.starting_room



opposit_dic = {'n': 's',
               's': 'n',
               'e': 'w',
               'w': 'e'
               }

traversal_path = []

def bfs(current_room):
    """
    BFS for the unexplored room, then 
    Return the path to it
    """
    #add the visited room
    visited = set() 
    #rooms to check
    q =[]
    q.append((current_room, []))
    count = 0
    #create a visited vertex
    while len(q)>0:
        #dequeue the current room exist
        (room, path) = q.pop(0)
        if room in visited :
            continue
        else:
            visited.add(room)
        for  direction in visited_room[room]:
            if visited_room[room][direction] == '?':
                return [path, direction]
            elif visited_room[room][direction] is not None:
                update_path = path.copy()
                update_path.append(direction)
                next_room = visited_room[room][direction]
                q.append((next_room, update_path))
    return None
import random
def dft(unexplored_dir):
    #create an empty  stack and add the starting room exists directions
    stack = Stack()
    stack.push(unexplored_dir)

    #while stack is not empty
    while stack.size() >0:
        #pop the current room exits direction
        current_exit = stack.pop()
        move_dir =current_exit[-1]
        # if this direction is not explored
        if move_dir not in visited_room[player.current_room.id]:
             continue
        elif  visited_room[player.current_room.id][move_dir] =='?':
            previous_room = player.current_room.id
            #move player in that direction
            player.travel(move_dir)
            # store the movement in the traversal path
            traversal_path.append(move_dir)
            # update the unexplored direction in the dictionary
            visited_room[previous_room][move_dir] = player.current_room.id
            opposite_value = opposit_dic[move_dir]
            if player.current_room.id not in visited_room:
            #if visited_room[player.current_room.id]
                visited_room[player.current_room.id] = {opposite_value:previous_room}
            else:
                visited_room[player.current_room.id][opposite_value]= previous_room
            # get all the neighbour room direction
            for direction in player.current_room.get_exits():
                if direction not in visited_room[player.current_room.id]:
                    visited_room[player.current_room.id][direction]='?'
                new_dir = []
                new_dir.append(direction)
                stack.push(new_dir)
    unexplored_dir = bfs(player.current_room.id)
    if unexplored_dir !=None:
        for direction in unexplored_dir[0]:
            player.travel(direction)
            traversal_path.append(direction)
        dft([unexplored_dir[1]])

starting_dir = random.choice(player.current_room.get_exits())

visited_room ={player.current_room.id :{}}
for direction in player.current_room.get_exits():
    visited_room[player.current_room.id][direction] ='?'

dft([starting_dir])



# Fill this out with directions to walk
#traversal_path = ['n', 'n']



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
# # queue = Queue()
# #create dic for visited vertex and path
# visited = {}  # Note that this is a dictionary, not a set
# #enqueue the queue with the starting user_id as a path
# queue.enqueue([player.current_room])
# #while queue is not empty
# while queue.size()>0:
#     #dequeue the current path
#     current_path = queue.dequeue()
#     #get the current vertex from end of the path
#     current_room = current_path[-1]
#     if current_room not in visited:
#         visited[current_room] = current_path
#         #queue up all the neighbours as path
#         for direction  in player.current_room.get_exits():

#             new_path = current_path.copy()
#             new_path.append(direction)
#             queue.enqueue(new_path)


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
