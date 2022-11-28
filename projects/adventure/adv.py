from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


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


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Global variables
player_starting_room = player.current_room
stack = Stack()
queue = Queue()
queue_two = Queue()
visited = {}
# bfs_visited = {}
path_taken = []
opposite_dir_dict = {'n': 's', 'e': 'w', 'w': 'e', 's': 'n'}
first = True
# key_count = len(bfs_visited.keys())

def get_random_course(room):
    # get random direction to start traversing
    random_array = room.get_exits()
    random.shuffle(random_array)
    going_to = room.get_room_in_direction(random_array[-1])

    return (going_to, random_array[-1])


def deal_with_exits_from_room(room):
    exits = room.get_exits()
    opposite_dir = opposite_dir_dict[path_taken[-1]]

    exits_string = 'nswe'
    # --- WE ARE NOT AT THE END OF A PATH ---- 
    if len(exits) > 1:
        for x in exits_string:
            if x not in exits:
                visited[room.id][x] = None

        # add it to the dictionary for the previous direction as the previous room
        visited[room.id][opposite_dir] = room.get_room_in_direction(opposite_dir).id

        # loop through the exits until finding an unexplored path
        for x in exits:
            if visited[room.id][x] == '?':
                return (False, x)

        # ---- IF WE NEED A PLACE TO HANDLE AN EXCEPTION FOR A ROOM THAT HAS NO UNEXPLORED PATHS -----
        return ('special', 'special')


    # --- WE ARE AT THE END OF A PATH ----  
    else:
        for x in exits_string:
            if x not in exits:
                visited[room.id][x] = None
        return(True, exits[0])

def find_question_mark_in_room(room):
    for xit in visited[room.id]:
        if visited[room.id][xit] == '?':
            return xit


def convert_rooms_to_path_and_travel_path(path):
    for room in path:
        for direct in visited[player.current_room.id]:
            room_to_go_to = player.current_room.get_room_in_direction(direct)
            if room_to_go_to == room:
                player.travel(direct)
                path_taken.append(direct)
                break

def deal_with_newly_found_unexplored_after_bfs(path):
    convert_rooms_to_path_and_travel_path(path)
    direction = find_question_mark_in_room(player.current_room)

    room_to_go = player.current_room.get_room_in_direction(direction)
    
    stack.push(room_to_go)

    visited[player.current_room.id][direction] = room_to_go.id

    player.travel(direction)

    path_taken.append(direction)




def traverseWorld():
    # creating dict entry for starting room
    visited[player_starting_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

    # get random room to start traversing
    starting_route = get_random_course(player_starting_room)

    # get the next room and move the player there
    going_to_room = starting_route[0]

    # get the direction were going and append it to the path
    direction_to = starting_route[1]
    visited[player_starting_room.id][direction_to] = going_to_room.id

    path_taken.append(direction_to)
    player.travel(direction_to)

    result = traverse_path(player.current_room)
    return result


def traverse_path(room):
    stack.push(room)
    while stack.size() > 0:
        current_room = stack.pop()

        if current_room.id not in visited:
            visited[current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

        exits = deal_with_exits_from_room(current_room)


        # WE ARE CONTINUING TO DO A DFT AT THIS POINT
        if exits[0] == False:
            # add that direction to the path
            path_taken.append(exits[1])
            # move your player if it's a place he has not yet been
            player.travel(exits[1])

            # add the room to the dictionaries direction
            visited[current_room.id][exits[1]] = player.current_room.id

            # add the room to the stack
            stack.push(player.current_room)

        # WE HAVE REACHED THE END OF THE PATH
        elif exits[0] == True:
            visited[current_room.id][exits[1]] = current_room.get_room_in_direction(exits[1]).id
            find_unexplored_room(player.current_room)

        else:
            ok = find_unexplored_room(current_room)
            if ok == 'ho':
                return path_taken

            
    return path_taken


def find_unexplored_room(room):
    queue.queue = []
    queue_two.queue = []
    queue.enqueue([room])
    path = []
    bfs_visited = {}

    if room.id == 188:
        print("")


    if room.id not in bfs_visited:
        bfs_visited[room.id] = []


    while queue.size() > 0:
        if len(bfs_visited) == 400:
            return

        path = queue.dequeue()
        current_location = path[-1]
        
        # CHECK IF THE CURRENT LOCATION IS ALREADY in our visited list
        if current_location.id not in bfs_visited:
            bfs_visited[current_location.id] = []

        exits = current_location.get_exits()

        if len(path) > 1:
            bfs_visited[path[-2].id].append(current_location.id)
            


        # print(f"PATH: {path} ---- CURRENT_LOCATION: {current_location.id} ---- EXITS: {exits} ---- BFS_VISITED: {bfs_visited}")
        print("\n")


        # CHECKING IF THE LEN OF EXITS IS GREATER THAN ONE SO THAT WE CAN DEAL WITH IT
        if len(exits) > 1:
            for xit in exits:
                room_for_exit = current_location.get_room_in_direction(xit)
                if visited[current_location.id][xit] == '?':
                    bfs_visited[current_location.id].append(room_for_exit.id)
                    deal_with_newly_found_unexplored_after_bfs(path)
                    return
                    # print(f"PATH: {ids} ---- CURRENT_LOCATION: {current_location.id} ---- EXITS: {exits} ---- BFS_VISITED: {bfs_visited} ------ EXIT :) {xit}")

                else:
                    room_for_exit = current_location.get_room_in_direction(xit)
                    if room_for_exit.id not in bfs_visited: 
                        new_path = list(path)
                        new_path.append(room_for_exit)
                        queue.enqueue(new_path)


        # IF THE EXIT LENGTH IS ONLY ONE THEN WE need to modify accordingly
        else:
            room_in_direction = current_location.get_room_in_direction(exits[0])
            if room_in_direction.id not in bfs_visited[current_location.id]:
                new_path = list(path)
                new_path.append(room_in_direction)
                queue.enqueue(new_path)
                bfs_visited[current_location.id].append(room_in_direction.id)
            



        print("\n")
    ok = []
    for x in path: 
        ok.append(x.id)
    print(f"PATH --- {ok}")

    return False

traversal_path = traverseWorld()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

print(traversal_path)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
