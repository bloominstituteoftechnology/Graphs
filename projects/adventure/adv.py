from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval
import time

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



def explore(player, moves_cue):
    # create queue
    q = Queue()
    # create set for visited rooms
    visited = set()
    # add current room to queue
    q.enqueue([player.current_room.id])
    while q.size() > 0:
        # as path is explored remove from queue
        path = q.dequeue()
        # keep track of last room visited
        last_room = path[-1]
        # if the last room was not in previously visited
        if last_room not in visited:
            # add to list of visited
            visited.add(last_room)
            # find all the exits for the room
            for exit in graph[last_room]:
                # if we find an exit in the room that is unexplored
                if graph[last_room][exit] == "?":
                    # add path to list to explore
                    return path
                    # otherwise remove path as already explored
                else:
                    lost = list(path)
                    lost.append(graph[last_room][exit])
                    q.enqueue(lost)
    return []


def q_moves(player, moves_q):
    #saves current_exit as current room
    current_exits = graph[player.current_room.id]
    #creates list
    untried_exits = []
    #loops through current_exits
    for direction in current_exits:
        #checks if current exit is a ?
        if current_exits[direction] == "?":
            #appends direction to untried_exits
            untried_exits.append(direction)
    #checks if untried exits is equal to 0
    if len(untried_exits) == 0:
        #adds unexplored as explore function
        unexplored = explore(player, moves_q)
        #saves room_num as current_room id
        room_num = player.current_room.id
        #loops through unexplored
        for next in unexplored:
            #loops through graph
            for direction in graph[room_num]:
                #checks if graph is equal to next
                if graph[room_num][direction] == next:
                    #enqueues the direction
                    moves_q.enqueue(direction)
                    #saves rm_num as next
                    room_num = next
                    break
    else:
        #enqueues untried_exits
        moves_q.enqueue(
            untried_exits[random.randint(0, len(untried_exits) - 1)])

start_time = time.time()

attempts = 500000
best_length = 997
best_path = []
trial = 0
# loops through different attempts
for x in range(attempts):
    #initializes player as player from world
    player = Player(world.starting_room)
    #initializes graph and fresh_room as a dictionary
    graph = {}
    fresh_room = {}
    #loop through direction in get_exits
    for direction in player.current_room.get_exits():
        #
        fresh_room[direction] = "?"
    #save fresh_room in the graph
    graph[world.starting_room.id] = fresh_room
    #initialize move_q as a Queue
    moves_q = Queue()
    #initialize total_moves as list
    total_moves = []
    #goes through function q_moves
    q_moves(player, moves_q)
    #initialize reverse_compass
    reverse_compass = {"n": "s", "s": "n", "e": "w", "w": "e"}
    #loops while something in queue
    while moves_q.size() > 0:
        #keeps track of starting
        starting = player.current_room.id
        #dequeue net path
        next = moves_q.dequeue()
        #moves player
        player.travel(next)
        #adds move
        total_moves.append(next)
        #saves end as current_room.id
        end = player.current_room.id
        #put into dictionary
        graph[starting][next] = end
        # checks if end is in graph dictionary
        if end not in graph:
            #put dict at graph[end]
            graph[end] = {}
            #loop through get_exits
            for exit in player.current_room.get_exits():
                #adds ? to graph
                graph[end][exit] = "?"
        #reverses the direction of starting
        graph[end][reverse_compass[next]] = starting
        #checks if moves_q is empty
        if moves_q.size() == 0:
            #goes through function q_moves
            q_moves(player, moves_q)
    # checks if the total moves is less than best_length
    if len(total_moves) < best_length:
        #saves a new best_path
        best_path = total_moves
        #saves a new best_length
        best_length = len(total_moves)
        #sets new trial
        trial = x
        #once passing for a 3, stops loop
        if best_length<957: #960 957 to beat score
            break



traversal_path = best_path
print(f"Trial: {trial}")
end_time = time.time()
print(f"Time to find {end_time - start_time}")



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
