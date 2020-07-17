from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
'''
USEFUL FUNCTIONS: player.current_room.id, player.current_room.get_exits() and player.travel(direction)

GOAL: You are provided with a pre-generated graph consisting of 500 rooms. You are responsible for filling
traversal_path with directions that, when walked in order, will visit every room on the map at least once.

STARTING STRATEGY: Start by writing an algorithm that picks a random unexplored direction from the player's
current room, travels and logs that direction, then loops. This should cause your player to walk a
depth-first traversal. When you reach a dead-end (i.e. a room with no unexplored paths), walk back to the
nearest room that does contain an unexplored path.

You can find the path to the shortest unexplored room by using a breadth-first search for a room with a
'?' for an exit. If you use the bfs code from the homework, you will need to make a few modifications.

1. Instead of searching for a target vertex, you are searching for an exit with a '?' as the value. If an
exit has been explored, you can put it in your BFS queue like normal.

2. BFS will return the path as a list of room IDs. You will need to convert this to a list of n/s/e/w
directions before you can add it to your traversal path.
'''

traversal_path = []

graph = {
  0: {'n': '?', 's': '?', 'w': '?', 'e': '?'}
}

class Queue():
    # Queue is for BFT and Stack is for DFT
    # 
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            # here is the difference- for Queue we pop the value thats
            # at the beginning of the list, whereas with Stack we pop
            # the last value in the list
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


# direction goes in the queue, and room_id can be called with player.current_room.id
# q_path[-1] is the last direction we moved

def reverse(a):
        if a == "n":
            return 's'
        elif a == "s":
            return 'n'
        elif a == 'e':
            return 'w'
        elif a == 'w':
            return 'e'

def bfs(starting_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # need to keep track of each path and the minimum path length
        # create an empty queue
        q = Queue()
        d = Queue()

        # create a set to store the visited directions
        visited = set()        #USE GRAPH INSTEAD

        # init enqueue the starting node
        q.enqueue([starting_vertex])

        d_path = []
        

        

        while q.size() > 0:
            
            # Dequeue the first item- q path is a queue of room ids
            q_path = q.dequeue()
            #last_room = q_path[-1]
            print('q',q_path)

            # If it's not been visited:
            #if last_d not in graph:
            


            exits = graph[player.current_room.id]
            
            #print(exits)
            # mark as visited
            if player.current_room.id not in visited:
                visited.add(player.current_room.id)
            

            # NEED TO CHANGE THE ORDER SO THAT MOVING INTO A NEW ROOM IS THE FIRST THING DONE AFTER
            # DEQUEUING Q_PATH

            # Add all neighbors to the queue
            for direction, next_room in exits.items():
                #print(next_room)
                # copy the path
                if next_room == '?':
                    last_room = player.current_room.id

                    player.travel(direction)
                    #add a direction to the path
                    print('found new room',player.current_room.id)
                    d_path.append(direction)

                    graph[last_room][direction] = player.current_room.id

                    if player.current_room.id not in graph:
                        graph[player.current_room.id] = {}

                    graph[player.current_room.id][reverse(direction)] = last_room

                    for dirs in player.current_room.get_exits():
                        #print(dirs)
                        
                        if dirs not in graph[player.current_room.id]:
                            graph[player.current_room.id][dirs] = '?'
                        # print(d_path)
                    #print('g',graph)

                    return d_path

                else:
                    if next_room not in visited:
                        #d.enqueue([direction])
                        #d_path.append(direction)
                        #print('d',d)
                        temp_path = list(q_path)
                        temp_path.append(next_room)
                        q.enqueue(temp_path)
                        #print('t',temp_path)
                        #print('q',q)
                        

                    else:
                        backtrack = direction

                

                
                # temp_path = list(q_path)
                # temp_path.append(next_room)

                # #print('q',q_path)
                # # d_path.append(direction)
                # #temp_d = list()
                # d.enqueue(direction)            # its just bouncing back and forth, must not be recording any
                #                                 # previously visited places. Need to record and check these with
                #                                 # the graph, and make sure d_path is queueing correctly
                # #print('d',d_path)
                
                # q.enqueue(temp_path)

        return None

while len(graph) < 501:
    print('cur room',player.current_room.id)
    path = bfs(player.current_room.id)    #need to convert the room_id output 
    print('path',path)
    print('g',graph)

# direction = 'n'

# # THIS IS THE "NEXT PATH" LOOP
# while len(graph) < 501:
    
#     # create an empty queue to store the current path
#     q = Queue()

#     # create a set to store the visited rooms
#     #visited = set()

#     # init enqueue the starting node
#     q.enqueue([direction])

#     # while the size of the queue is greater than 0

#     # THIS IS THE BFS LOOP
#     while q.size() > 0:
        
#         # Dequeue the first path
#         q_path = q.dequeue()
#         #print('qpath', q_path)

#         # set d = the last value in q_path, ie the last direction moved
#         last_d = q_path[-1]
#         #print('last', last_d)

#         # move the player in a new direction
#         player.travel(last_d)

#         #player room id and graph need to be linked
#         # identify current room, loop through the get_exits options, store them in the graph,
#         # then move the player into one, then identify the next room and reset the loop

#         cur_room_id = player.current_room.id
#         print('id,',cur_room_id)

#         exits = player.current_room.get_exits()
#         print(exits)

#         def reverse(a):
#             if a == "n":
#                 return 's'
#             elif a == "s":
#                 return 'n'
#             elif a == 'e':
#                 return 'w'
#             elif a == 'w':
#                 return 'e'

#         graph[cur_room_id] = {}
#         for x in exits:
#             # if we haven't visited this room before, then move into it, record it, and move back to the
#             # original room
#             if graph[cur_room_id][x] == '?':
                
#                 #print(graph[cur_room_id])
#                 # player.travel(x)
#                 # cur_room_id = player.current_room.id
#                 # graph[cur_room_id][x] = '?'

#                 # player.travel(reverse(x))
                
#             else:
#                 # else we queue the room to enter later
#                 q.enqueue(graph[cur_room_id][x])
                

        

#                     # SELF.VISITED NEEDS TO BE RESET OR INITIATED ELSEWHERE
#         # If it's not been visited:
#         #if v not in visited:
        
#         # if this is a new room
#         if graph[cur_room_id] == '?':
            
#             # IF SO, RETURN the PATH we took to get to the new room
#             traversal_path.append(q_path)
            
#             # and set last direction
#             direction = q_path[-1]
#             player.travel(direction)

#             # fill in the graph
#             graph[cur_room_id] = player.current_room.get_exits()
#             print('exits',player.current_room.get_exits())
            
#         # Mark as visited (i.e. add to the visited set)
#         visited.add(v)
        
#         # Add all neighbors to the queue
#         for next_direction in player.current_room.get_exits():
#             # copy the path
#             # temp_path = list(q_path)
#             # # this adds a new room onto temp path(q_path)
#             # temp_path.append(next_room)
            
#             # q.enqueue(temp_path)
#             direction = next_direction      # NEED TO START A NEW QUEUE FOR DIRECTIONS



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
