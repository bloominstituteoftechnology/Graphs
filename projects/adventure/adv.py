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
map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

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

#create a visited room dic

#do bfs for unexplored room
def bfs(current_room):
    """
    BFS for the unexplored room, then 
    Return the path to it
    """
    #add the visited room
    visited = set() 
    # player.current_room = current_room
    # current_dir = player.current_room.get_exits()
    # exits = current_dir[-1]
    # #get room in that direction
    # new_room = player.current_room

    #print('new_room', new_room.id)
    #player.travel(current_dir)
    #traversal_path.append(current_dir)
    #rooms to check
    q =[]
    #visited_room=set()
    # explored_room = []
    # explored_dir=[]
    # room_dir = []
   
    #print('bfs room', player.current_room.get_exits())
    #enqueue with player current room exits direction
    #empty list is the path to the list
    q.append((current_room, []))
    count = 0
    #create a visited vertex
    while len(q)>0:
        #dequeue the current room exist
        (room, path) = q.pop(0)
        # current_dir = current_exit[-1]
        # print('bfsssssssssss',current_dir)
        # print('room_id', new_room.id)
        # print(explored_room)
        if room in visited :
            continue
        else:
            visited.add(room)
            #explored_dir.append(current_dir)
            #track_room.append((new_room.id,current_dir))
            #new_room = new_room.get_room_in_direction(current_dir)
            #explored_room.append(new_room.id)
            #room_dir.append(current_dir)
            #print('expl ', explored_room)
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
#print('choiccccccccccccc', unexplored_dir)
def dft(unexplored_dir):
    #create an empty  stack and add the starting room exists directions
    stack = Stack()
    stack.push(unexplored_dir)

    #while stack is not empty
    while stack.size() >0:
        #pop the current room exits direction
        current_exit = stack.pop()
        print(current_exit)
        #print(visited_room)
        move_dir =current_exit[-1]
        # if this direction is not explored
        print('key_error', move_dir)
        #print(visited_room[player.current_room.id])
        if  visited_room[player.current_room.id][move_dir] =='?':
            previous_room = player.current_room.id
            #print(previous_room)
            #move player in that direction
            player.travel(move_dir)
            # store the movement in the traversal path
            traversal_path.append(move_dir)
            #print('temp vis', visited_room)
            # update the unexplored direction in the dictionary
            visited_room[previous_room][move_dir] = player.current_room.id
            #print(player.current_room.id)
            opposite_value = opposit_dic[move_dir]
            if player.current_room.id not in visited_room:
            #if visited_room[player.current_room.id]
                visited_room[player.current_room.id] = {opposite_value:previous_room}
            else:
                visited_room[player.current_room.id][opposite_value]= previous_room

            #print(visited_room)
            # get all the neighbour room direction
            print('current room', player.current_room.id)
            
            #print(visited_room[player.current_room.id])
            for direction in player.current_room.get_exits():
                if direction not in visited_room[player.current_room.id]:
                    visited_room[player.current_room.id][direction]='?'
                    #print('second room', player.current_room.id)
                new_dir = current_exit.copy()
                new_dir.append(direction)
                stack.push(new_dir)
            #count =+1
            #print(visited_room)
   # print(player.current_room.get_exits())
    #player.travel(player.current_room.get_exits())
    print('*************************')
    unexplored_dir = bfs(player.current_room.id)
    print('unexplored_dir',unexplored_dir)
    
    #print('bfs return',bfs())
    if unexplored_dir !=None:
        for direction in unexplored_dir[0]:
            player.travel(direction)
            traversal_path.append(direction)
            #print('bfs result ', unexplored_dir[1][-1])
        #print('player current room', player.current_room.id)
        dft([unexplored_dir[1]])

starting_dir = random.choice(player.current_room.get_exits())

visited_room ={player.current_room.id :{}}
for direction in player.current_room.get_exits():
    visited_room[player.current_room.id][direction] ='?'
#print(unexplored_dir)
dft([starting_dir])
# print(traversal_path)           
# print(visited_room)
        


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
